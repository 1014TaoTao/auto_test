# coding:utf8


from common import setting
from tools.assert_tools.api_tool_assert import Assert
from tools.common_tools.api_tool_headers import HeadersPack, read_token
from tools.logs_tools.public_tool_log import logger
from tools.requests_tools.api_tool_reponse import Response
from tools.requests_tools.api_tool_request import Requests


class Login:

    def __init__(self, BASEHOST: str, LOGINHOST: str, LOGINDATA: dict, USERNAME: str):
        # 登录地址
        self.url = BASEHOST + LOGINHOST
        # 登录入参,读取到str转为dict
        self.data_dict = LOGINDATA
        # 登录用户username
        self.assert_username = USERNAME
        # 请求头
        self.headers = {'Content-Type': 'application/json;charset=UTF-8'}

        self.logger = logger(setting.API_LOG_PATH)

    def api_login(self):
        """
        :return:
        """
        self.logger.info('【开始获取token...start】')
        res = Response().result(
            Requests().send_request(method="get", url=self.url, data=self.data_dict, headers=self.headers,
                                    parametric_key='params', file=None))
        print(res)
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
            raise f"登录异常，请检查平台连接情况：{e}\n"  # 'NoneType' object is not subscriptable 平台连接不上

if __name__ == '__main__':
    BASEHOST='http://10.0.34.13:18603'
    LOGINHOST='/uaa/oauth/token'
    LOGINDATA={
      "grantType": "password",
      "accountType": "mobile",
      "scope": "trust",
      "password": "eede6d66c93b0340342c18f8c5c76a87",
      "mobile": "18192408293",
      "clientId": "saas_op",
      "clientSecret": "dc278c7ba8b3ddedbde7361fcedb70ee",
      "username": "18192408293",
    }
    USERNAME='18192408293'
    Login(BASEHOST, LOGINHOST, LOGINDATA, USERNAME).api_login()
