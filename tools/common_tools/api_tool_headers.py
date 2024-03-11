# coding:utf8

from common import setting


# 请求头处理
class HeadersPack:
    def __init__(self, res: dict):
        """
        :param res:
        """
        self.res = res

    # 获取登录的cookie
    def _get_login_token(self) -> str:
        """
        :return:
        """
        token_id = self.res['body']['access_token']
        return token_id

    # 获取token值
    def get_token_value(self) -> str:
        """
        :return:
        """
        return self._get_login_token().replace("'", '"')

    # 生成headers
    def create_headers(self):
        """
        :return:
        """
        token_id = self._get_login_token()
        try:
            with open(file=setting.TOKEN_FILE, mode='w+', encoding='utf-8') as f:
                f.write(str("Bearer " + token_id).replace("'", '"'))
        except Exception as e:
            raise f"【写入token至./data/api/token.txt异常！{e}】"


# 读取token
def read_token() -> str:
    """
    :return:
    """
    try:
        with open(file=setting.TOKEN_FILE, mode='r', encoding='utf-8') as f:
            token_str = f.read()
        return token_str
    except Exception as e:
        raise f"【读取token在./data/api/token.txt异常！{e}】"


# 清空token
def clear_token():
    """
    :return:
    """
    try:
        with open(file=setting.TOKEN_FILE, mode="w+", encoding="utf-8") as f:
            f.close()
    except Exception as e:
        raise f"【清除token在./data/api/token.txt异常！{e}】"
