# coding:utf8


from common import setting, consts
from tools.api_tool_assert import Assert
from tools.api_tool_headers import headersPack
from tools.api_tool_reponse import Response
from tools.api_tool_request import Requests
from tools.public_tool_log import logger

logger = logger(setting.API_LOG_PATH)


class Login:

    def __init__(self):
        # 登录地址
        self.url = consts.BASEHOST + consts.LOGINHOST
        # 登录入参,读取到str转为dict
        self.data_dict = consts.LOGINDATA
        # 登录用户username
        self.assert_username = consts.USERNAME
        # 请求头
        self.headers = {'Content-Type': 'application/json;charset=UTF-8'}

    def api_login(self):
        """
        :return:
        """
        res = Response().result(
            Requests().send_request(method="GET", url=self.url, data=self.data_dict, headers=self.headers))
        try:

            # 断言用户名使用参数化，在配置文件中的username字段
            if Assert().assert_code(200, res['code']):
                if Assert().assert_in_body(f'{self.assert_username}', res['body']['user_name']):
                    headersPack(res).create_headers()  # token写入文件
                    logger.info(f"【登录操作token成功】\n")
                else:
                    logger.error(f"【登录断言username失败】\n")
            else:
                logger.error(f"【登录断言code失败】\n")
        except Exception as e:
            logger.error(f"登录异常，请检查平台连接情况：{e}\n")  # 'NoneType' object is not subscriptable 平台连接不上

# if __name__ == '__main__':
#     Login().api_login()
