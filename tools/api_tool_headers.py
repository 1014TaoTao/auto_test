# coding:utf8
from common import setting
from tools.public_tool_log import logger

logger = logger(setting.API_LOG_PATH)


# 请求头处理
class headersPack:
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

    # 生成headers
    def create_headers(self):
        """
        :return:
        """
        token_id = self._get_login_token()
        try:
            with open(file=setting.TOKEN_FILE, mode='w+', encoding='utf-8') as f:
                f.write(str("Bearer " + token_id).replace("'", '"'))
                logger.info(f"【写入token至./data/api/token.txt文件完成】")
        except Exception as e:
            logger.error(f"【写入token至./data/api/token.txt异常！{e}】")


# 读取token
def read_token() -> str:
    """
    :return:
    """
    try:
        with open(file=setting.TOKEN_FILE, mode='r', encoding='utf-8') as f:
            token_str = f.read()
            logger.info(f"【读取token成功：{token_str}】")
        return token_str
    except Exception as e:
        logger.error(f"【读取token在./data/api/token.txt异常！{e}】")


# 清空token
def clear_token():
    """
    :return:
    """
    try:
        with open(file=setting.TOKEN_FILE, mode="w+", encoding="utf-8") as f:
            logger.error(f"【清除token在./data/api/token.txt完成】")
            f.close()
    except Exception as e:
        logger.error(f"【清除token在./data/api/token.txt异常！{e}】")

# 测试
# if __name__ == '__main__':
#     print(read_token())
