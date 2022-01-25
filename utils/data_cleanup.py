#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/2/20
# @Author  : Mcen (mmocheng@163.com)
# @Name    : data_cleanup
"""
封装数据清理
"""

from utils.operation_db import Opera_DB
from base.element_path import Element
from utils.common import CommonUtil
from config.config import Config
from utils.logging_conf import logger
from utils.Request import Request
from utils.Assert import Assertions
from base.get_params import GetParams

class Data_Cleanup:
    # @staticmethod
    # def data_cleanup():
    #     common = CommonUtil()
    #     data = common.read_yaml(Element.CLEANUP_DATA)
    #     print(data)
    #     # 读取出来后循环执行sql
    #     for key,values in data.items():
    #         logger.info('==执行( {} )的数据清理开始=='.format(data[key]['dec']))
    #         for i,sql in values.items():
    #             if i != 'dec':
    #                 logger.info('==执行sql=={}'.format(sql))
    #                 # 判断执行影响的行数
    #                 row = Opera_DB().commit_data(sql)
    #                 if row > 0:
    #                     logger.info('清理数据条数为：{}，清理成功！'.format(row))
    #         logger.info('==结束( {} )的数据清理=='.format(data[key]['dec']))

    @staticmethod
    def data_cleanup_drone3d():
        headers = GetParams().operate_header()
        URL = Config().base_url
        expected_code = int(Config().get_conf('assertCode', 'success_code'))

        #按任务名称模糊查询
        url1 =  URL + Config().get_conf('drone_url', 'air_plan') + "?pageNo=1&pageSize=10&routeType=1&routeName=环普产业园autotest"
        res1 = Request().get_request(url=url1,data=None,header=headers)
        total = res1['body']['data']['total']
        print(total)
        ids = []

        if 200 >= total >= 1:
            url2 = URL + Config().get_conf('drone_url','air_plan') + "?pageNo=1&pageSize=%s&routeType=1&routeName=环普产业园autotest" % total
            res2 = Request().get_request(url=url2, data=None, header=headers)
            for num in range(0, total):
                id = res2['body']['data']['list'][num]['id']
                ids.append(id)
                if len(ids) ==total:
                    break
            # 删除飞行计划
            logger.info("==执行平台任务清理开始==")
            url_del = URL + Config().get_conf("drone_url", "air_plan_delete")
            res = Request().post_request(url=url_del, json=ids, header=headers)
            statusCode = res['body']['code']

            Assertions().assert_code(code=statusCode, expected_code=expected_code, resquest_url=url_del, resquest_body=ids,
                                     response_body=res)
            logger.info("==执行平台任务清理结束==")


        elif total > 200:
            url3 = URL + Config().get_conf('drone_url',
                                           'air_plan') + "?pageNo=1&pageSize=200&routeType=1&routeName=环普产业园autotest"
            res3 = Request().get_request(url=url3, data=None, header=headers)
            for num in range(0, 199):
                print(num)
                id = res3['body']['data']['list'][num]['id']
                ids.append(id)
                if len(ids) ==200:
                    break

            # 删除飞行计划
            logger.info("==执行平台任务清理开始==")
            url_del = URL + Config().get_conf("drone_url", "air_plan_delete")
            res = Request().post_request(url=url_del, json=ids, header=headers)
            statusCode = res['body']['code']

            Assertions().assert_code(code=statusCode, expected_code=expected_code, resquest_url=url_del, resquest_body=ids,
                                     response_body=res)
            logger.info("==执行平台任务清理结束==")

        else:
            logger.info("----无可删除数据")


if __name__ == '__main__':
    Data_Cleanup.data_cleanup_drone3d()



