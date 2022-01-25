#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/2/5
# @Author  : Mcen (mmocheng@163.com)
# @Name    : Assert


"""
封装Assert方法

"""
# from Common import Consts
import json
from utils.logging_conf import logger


class Assertions:
    def __init__(self):
        pass

    def assert_code(self, code, expected_code, resquest_url, response_body, resquest_body=None):
        """
        验证response状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert code == expected_code
            logger.info("----success---接口返回成功")
            return True
        except:
            logger.error("----failed---接口返回失败, expected_code is %s, statusCode is %s " % (expected_code, code))
            logger.info("request_url is %s" % (resquest_url))
            logger.info("request_body is %s" % (resquest_body))
            logger.info("response_body is %s" % (response_body))
            # Consts.RESULT_LIST.append('fail')
            raise

    def assert_code_reverse(self, code, expected_code, resquest_url, response_body, resquest_body=None):
        """
        验证response状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert code != expected_code
            logger.info("----success---接口返回与预期一致")
            return True
        except:
            logger.error("----failed---接口返回与预期不一致, expected_code is %s, statusCode is %s " % (expected_code, code))
            logger.info("request_url is %s" % (resquest_url))
            logger.info("request_body is %s" % (resquest_body))
            logger.info("response_body is %s" % (response_body))
            # Consts.RESULT_LIST.append('fail')
            raise

    def assert_body(self, body_msg, expected_msg, resquest_url, response_body, resquest_body=None):
        """
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        """
        try:
            msg = body_msg
            assert msg == expected_msg
            logger.info("----success---数据校验成功")
            return True

        except:
            logger.error(
                "----failed---数据校验失败Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body_msg))
            logger.info("request_url is %s" % (resquest_url))
            logger.info("request_body is %s" % (resquest_body))
            logger.info("response_body is %s" % (response_body))
            # Consts.RESULT_LIST.append('fail')

            raise

    def assert_in_text(self, expected_msg, resquest_url, response_body, resquest_body=None):
        """
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(response_body, ensure_ascii=False)
            # print(text)
            assert expected_msg in text
            return True

        except:
            logger.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)
            logger.info("request_url is %s" % (resquest_url))
            logger.info("request_body is %s" % (resquest_body))
            logger.info("response_body is %s" % (response_body))
            # Consts.RESULT_LIST.append('fail')

            raise

    def assert_total(self,total,expected_total, resquest_url, response_body, resquest_body=None):
        """
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        """
        try:
            assert total == expected_total
            logger.info("----success---数据校验成功")
            return True

        except:
            logger.error(
                "----failed---数据校验失败Response total != expected_total, expected_total is %s, total is %s" % (expected_total, total))
            logger.info("request_url is %s" % (resquest_url))
            logger.info("request_body is %s" % (resquest_body))
            logger.info("response_body is %s" % (response_body))
            # Consts.RESULT_LIST.append('fail')

            raise


    def assert_text(self, expected_msg, resquest_url, response_body, resquest_body=None):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert response_body == expected_msg
            return True

        except:
            logger.error("Response body != expected_msg, expected_msg is %s, body is %s" % (expected_msg, body))
            logger.info("request_url is %s" % (resquest_url))
            logger.info("request_body is %s" % (resquest_body))
            logger.info("response_body is %s" % (response_body))
            # Consts.RESULT_LIST.append('fail')
            raise

    def assert_time(self, time, expected_time, resquest_url, response_body, resquest_body=None):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            return True

        except:
            logger.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))
            logger.info("request_url is %s" % (resquest_url))
            logger.info("request_body is %s" % (resquest_body))
            logger.info("response_body is %s" % (response_body))
            # Consts.RESULT_LIST.append('fail')
            raise
