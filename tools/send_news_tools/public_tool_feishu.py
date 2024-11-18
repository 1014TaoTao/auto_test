# -*- coding: utf-8 -*-#

from json import JSONDecodeError
import requests
import json
import logging
import time
import urllib3
import datetime

from common.setting import ConfigHandler
from utils.readFilesUtils.yamlControl import GetYamlData
from utils.otherUtils.allureDate.allure_report_data import CaseCount

urllib3.disable_warnings()

try:
    JSONDecodeError = json.decoder.JSONDecodeError
except AttributeError:
    JSONDecodeError = ValueError


def is_not_null_and_blank_str(content):
    """
  �ǿ��ַ���
  :param content: �ַ���
  :return: �ǿ� - True���� - False
  """
    if content and content.strip():
        return True
    else:
        return False


class FeiShuTalkChatBot(object):
    """���������֪ͨ"""
    def __init__(self):

        self.timeStamp = str(round(time.time() * 1000))
        self.devConfig = ConfigHandler()
        # ��yaml�ļ��л�ȡ����������Ϣ

        self.name = GetYamlData(ConfigHandler.config_path).get_yaml_data()['ProjectName'][0]
        self.test_name = GetYamlData(ConfigHandler.config_path).get_yaml_data()['TesterName']
        self.host = GetYamlData(ConfigHandler.config_path).get_yaml_data()['Env']
        self.tester = GetYamlData(ConfigHandler.config_path).get_yaml_data()
        self.allure_data = CaseCount()
        self.PASS = self.allure_data.pass_count()
        self.FAILED = self.allure_data.failed_count()
        self.BROKEN = self.allure_data.broken_count()
        self.SKIP = self.allure_data.skipped_count()
        self.TOTAL = self.allure_data.total_count()
        self.RATE = self.allure_data.pass_rate()

        self.headers = {'Content-Type': 'application/json; charset=utf-8'}
        self.devConfig = ConfigHandler()
        self.getFeiShuTalk = GetYamlData(self.devConfig.config_path).get_yaml_data()['FeiShuTalk']
        self.webhook = self.getFeiShuTalk["webhook"]

    def send_text(self, msg: str):
        """
    ��Ϣ����Ϊtext����
    :param msg: ��Ϣ����
    :return: ������Ϣ���ͽ��
    """
        data = {"msg_type": "text", "at": {}}
        if is_not_null_and_blank_str(msg):  # ����msg�ǿ�
            data["content"] = {"text": msg}
        else:
            logging.error("text���ͣ���Ϣ���ݲ���Ϊ�գ�")
            raise ValueError("text���ͣ���Ϣ���ݲ���Ϊ�գ�")

        logging.debug('text���ͣ�%s' % data)
        return self.post()

    def post(self):
        """
    ������Ϣ������UTF-8���룩
    :return: ������Ϣ���ͽ��
    """
        rich_text = {
            "email": "fanlv@bytedance.com",
            "msg_type": "post",
            "content": {
                "post": {
                    "zh_cn": {
                        "title": "���Զ�������֪ͨ��",
                        "content": [
                            [
                                {
                                    "tag": "a",
                                    "text": "���Ա���",
                                    "href": "https://192.168.xx.72:8080/job/helper_test_adverte/allure/#"
                                },
                                {
                                    "tag": "at",
                                    "user_id": "ou_18eac85d35a26f989317ad4f02e8bbbb"
                                    # "text":"������"
                                }
                            ],
                            [
                                {
                                    "tag": "text",
                                    "text": "����  ��Ա : "
                                },
                                {
                                    "tag": "text",
                                    "text": "{testname}".format(testname=self.test_name)
                                }
                            ],
                            [
                                {
                                    "tag": "text",
                                    "text": "����  ���� : "
                                },
                                {
                                    "tag": "text",
                                    "text": "{host}".format(host=str(self.host))
                                }
                            ],
                            [{
                                "tag": "text",
                                "text": "��   ��   �� : "
                            },
                                {
                                    "tag": "text",
                                    "text": "{rate}".format(rate=self.RATE) + " %"
                                }],  # �ɹ���

                            [{
                                "tag": "text",
                                "text": "�ɹ������� : "
                            },
                                {
                                    "tag": "text",
                                    "text": "{total}".format(total=self.PASS)
                                }],  # �ɹ�������

                            [{
                                "tag": "text",
                                "text": "ʧ�������� : "
                            },
                                {
                                    "tag": "text",
                                    "text": "{failed}".format(failed=self.FAILED)
                                }],  # ʧ��������
                            [{
                                "tag": "text",
                                "text": "�쳣������ : "
                            },
                                {
                                    "tag": "text",
                                    "text": "{failed}".format(failed=self.BROKEN)
                                }],  # ��������
                            [
                                {
                                    "tag": "text",
                                    "text": "ʱ  �� : "
                                },
                                {
                                    "tag": "text",
                                    "text": "{test}".format(test=datetime.datetime.now().strftime('%Y-%m-%d'))
                                }
                            ],

                            [
                                {
                                    "tag": "img",
                                    "image_key": "d640eeea-4d2f-4cb3-88d8-c964fab53987",
                                    "width": 300,
                                    "height": 300
                                }
                            ]
                        ]
                    }
                }
            }
        }
        try:
            post_data = json.dumps(rich_text)
            response = requests.post(self.webhook, headers=self.headers, data=post_data, verify=False)
        except requests.exceptions.HTTPError as exc:
            logging.error("��Ϣ����ʧ�ܣ� HTTP error: %d, reason: %s" % (exc.response.status_code, exc.response.reason))
            raise
        except requests.exceptions.ConnectionError:
            logging.error("��Ϣ����ʧ�ܣ�HTTP connection error!")
            raise
        except requests.exceptions.Timeout:
            logging.error("��Ϣ����ʧ�ܣ�Timeout error!")
            raise
        except requests.exceptions.RequestException:
            logging.error("��Ϣ����ʧ��, Request Exception!")
            raise
        else:
            try:
                result = response.json()
            except JSONDecodeError:
                logging.error("��������Ӧ�쳣��״̬�룺%s����Ӧ���ݣ�%s" % (response.status_code, response.text))
                return {'errcode': 500, 'errmsg': '��������Ӧ�쳣'}
            else:
                logging.debug('���ͽ����%s' % result)
                # ��Ϣ����ʧ�����ѣ�errcode ��Ϊ 0����ʾ��Ϣ�����쳣����Ĭ�ϲ����ѣ������߿��Ը��ݷ��ص���Ϣ���ͽ�������жϺʹ���
                if result.get('StatusCode') != 0:
                    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
                    error_data = {
                        "msgtype": "text",
                        "text": {
                            "content": "[ע��-�Զ�֪ͨ]�����������Ϣ����ʧ�ܣ�ʱ�䣺%s��ԭ��%s���뼰ʱ������лл!" % (
                                time_now, result['errmsg'] if result.get('errmsg', False) else 'δ֪�쳣')
                        },
                        "at": {
                            "isAtAll": False
                        }
                    }
                    logging.error("��Ϣ����ʧ�ܣ��Զ�֪ͨ��%s" % error_data)
                    requests.post(self.webhook, headers=self.headers, data=json.dumps(error_data))
                return result


# if __name__ == '__main__':
#     send = FeiShuTalkChatBot()
#     send.post()
