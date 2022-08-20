# coding:utf-8
from typing import Any

import yaml

from common import setting


class Config:
    def __init__(self):
        self.config_yaml = setting.CONFIG_YAML
        # 读取yaml内容
        with open(self.config_yaml, 'rb') as f:
            self.data = yaml.safe_load(f)

    # 获取所有数据
    def all_data(self) -> dict:
        """
        :return:
        """
        all_data_dict = self.data
        return all_data_dict

    # 获取邮件配置信息
    def get_email_info(self) -> dict:
        """
        :return:
        """
        email_info = self.data['email']
        return email_info

    # 获取数据库配置信息
    def get_databases_info(self) -> dict:
        """
        :return:
        """
        databases_info = self.data['databases']
        return databases_info

    # 获取环境下所有信息
    def get_environment_info(self) -> dict:
        """
        :return:
        """
        environment = self.data['environment']
        return environment

    # 获取环境名称
    def get_environment_type(self) -> list:
        """
        :return:
        """
        environment_list = []
        environment = self.data['environment']
        for k, v in environment.items():
            environment_list.append(k)
        return environment_list

    # 获取登陆地址
    def get_login_url(self, environment_type: str) -> str:
        """
        :param environment_type:
        :return:
        """
        base_host = self.get_environment_info()[environment_type]['url']
        return base_host

    # 获取请求头
    def get_login_headers(self, environment_type: str) -> dict:
        """
        :param environment_type:
        :return:
        """
        headers = self.get_environment_info()[environment_type]['headers']
        return headers

    # 获取登录入参
    def get_login_data(self, environment_type: str) -> dict:
        """
        :param environment_type:
        :return:
        """
        login_info = self.get_environment_info()[environment_type]['data']
        return login_info

    # 获取登录入参
    def get_login_username(self, environment_type: str) -> str:
        """
        :param environment_type:
        :return:
        """
        username = self.get_environment_info()[environment_type]['data']['username']

        return username

    # 获取接口基础域名
    def get_api_host(self) -> list:
        """
        :return:
        """
        base_host = self.data['api_host']
        return base_host


    # 是否删除旧的测试数据
    def get_delete_report_on_off(self) -> str:
        """
        :return:
        """
        delete_report_on_off = self.data['delete_report_on_off']
        return delete_report_on_off

    # 是否生成测试报告
    def get_run_report_on_off(self) -> str:
        """
        :return:
        """
        run_report_on_off = self.data['run_report_on_off']
        return run_report_on_off

    # 是否发送邮件
    def get_send_email_on_off(self) -> str:
        """
        :return:
        """
        send_email_on_off = self.data['send_email_on_off']
        return send_email_on_off

    # 是否结束测试自动打开测试报告html
    def get_open_report_on_off(self) -> str:
        """
        :return:
        """
        open_report_on_off = self.data['open_report_on_off']
        return open_report_on_off

    # 获取执行测试人员信息
    def get_testers(self) -> list:
        """
        :return:
        """
        testers = self.data['testers']
        return testers

    # 钉钉
    def get_send_dingding_news_on_off(self) -> str:
        """
        :return:
        """
        send_dingding_news_on_off = self.data['send_dingding_news_on_off']
        return send_dingding_news_on_off

    # 钉钉secret
    def get_dingding_secret(self) -> str:
        """
        :return:
        """
        dingding_secre = self.data['dingding']['secret']
        return dingding_secre

    # 钉钉secret
    def get_dingding_webhook(self) -> str:
        """
        :return:
        """
        dingding_webhook = self.data['dingding']['webhook']
        return dingding_webhook

# 测试
# if __name__ == '__main__':
#     from common import setting
#
#     C = Config()
#     print(C.get_login_url('op'))
#     print(C.get_login_data('op'))
#     print(C.get_login_username('op'))
#
#     print(C.get_login_url('cp'))
#     print(C.get_login_data('cp'))
#     print(C.get_login_username('cp'))
