# coding:utf8


from common import consts, setting
from tools.asserti_tool import Assert
from tools.api_tool_headers import HeadersPack
from tools.logi_tool import logger
from tools.api_tool_reponse import Response
from tools.api_tool_request import Requests


class Login:

    def __init__(self):
        # 登录地址
        self.url: str = consts.LOGIN_URL
        # 登录入参,读取到str转为dict
        self.data_dict: dict = consts.LOGIN_DATA
        # 登录用户username
        self.assert_username = consts.LOGIN_USERNAME
        # 请求头
        self.headers = consts.LOGIN_HEADERS

        self.logger = logger(setting.API_LOG_PATH)

    def api_login(self):
        """
        :return:
        """
        self.logger.info('【开始获取token...start】')
        res = Response().result(
            Requests().send_request(method="get", url=self.url, data=self.data_dict, headers=self.headers,
                                    parametric_key='params', file=None))
        try:

            # 断言用户名使用参数化，在配置文件中的username字段
            if Assert().assert_code(200, res['code']):
                if Assert().assert_in_body(f'{self.assert_username}', res['body']['user_name']):
                    HeadersPack(res).create_headers()  # token写入文件
                    self.logger.info(f"【登录操作token成功】\n")
                else:
                    self.logger.error(f"【登录断言username失败】\n")
            else:
                self.logger.error(f"【登录断言code失败】\n")
        except Exception as e:
            # 'NoneType' object is not subscriptable 平台连接不上
            raise f"登录异常，请检查平台连接情况：{e}\n"


if __name__ == '__main__':
    Login().api_login()
