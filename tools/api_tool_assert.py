# coding:utf8
from common import setting
from tools.public_tool_log import logger


class Assert:
    def __init__(self):
        self.logger = logger(setting.API_LOG_PATH)
        self.pass_num = 0
        self.fail_num = 0

    def assert_code(self, expected_code, code):
        try:
            assert code == expected_code
            self.logger.info(f"【断言status_code:successed】期望状态码: {expected_code} 【==】 实际状态码: {code}")
            return True
        except Exception as e:
            self.logger.error(f"【断言status_code:failed】期望状态码: {expected_code} 【!=】 实际状态码: {code}")
            return False

    def assert_msg(self, expected_msg, msg):
        try:
            assert msg == expected_msg
            self.logger.info(f"【断言msg:successed】期望msg: {expected_msg} 【==】 实际msg: {msg}")
            return True
        except Exception as e:
            self.logger.error(f"【断言msg:failed】期望msg: {expected_msg} 【!=】 实际msg: {msg}")
            return False

    def assert_in_body(self, expected_msg, body):
        try:
            assert expected_msg in body
            self.logger.info(f"【断言msg:successed】期望msg: {expected_msg} 【in】 实际body: {body}")
            return True
        except Exception as e:
            self.logger.error(f"【断言msg:failed】期望msg: {expected_msg} 【not in】 实际body: {body}")
            return False

    def assert_body(self, expected_msg, body):
        try:
            assert body == expected_msg
            self.logger.info(f"【断言msg:successed】期望状态码: {expected_msg} 【==】 实际状态码: {body}")
            return True
        except Exception as e:
            self.logger.error(f"【断言msg:failed】期望状态码: {expected_msg} 【!=】 实际状态码: {body}")
            return False

    def assert_time(self, expected_time, time):
        try:
            assert time < expected_time
            self.logger.info(f"【断言expected_time:successed】期望expected_time: {expected_time} 【>】 实际time: {time}")
            return True
        except Exception as e:
            self.logger.error(f"【断言expected_time:successed】期望expected_time: {expected_time} 【<=】 实际time: {time}")
            return False
