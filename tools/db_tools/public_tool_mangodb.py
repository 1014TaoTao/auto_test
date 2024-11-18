# -*- coding: utf-8 -*-

import sys
from typing import Any

import pymongo
from loguru import logger

"""
注意mongodb的版本，这里我使用pymongo~=3.11.4 版本，如果最新会报错，python-dateutil~=2.8.2
"""


class MongodbHandle:
    def __init__(self, host: str, port: int, db_name: str, user: str, password: str):
        """
        :param host: 连接地址
        :param port: 端口
        :param db_name: 数据库名称
        :param user: 用户
        :param password: 密码
        """
        logger.info(
            f"""
                host:{host},
                port:{port},
                db_name:{db_name},
                user:{user},
                password:{password}
            """
        )
        self.conn = pymongo.MongoClient(host, port)
        self.db = eval(f'self.conn.{db_name}')
        self.db.authenticate(user, password)

    def insert_collection(self, collection_name: str, value: Any) -> int:  # 单个插入
        """
        :param collection_name:
        :param value:
        :return:
        """
        mycol = self.db[collection_name]
        mycol_id = mycol.insert_one(value)
        return mycol_id.inserted_id  # 返回insert_id，即插入文档的id值

    def insert_batch_collection(self, collection_name: str, value_list: list) -> list:  # 批量插入
        """
        :param collection_name:
        :param value_list:
        :return:
        """
        mycol = self.db[collection_name]
        mycol_id = mycol.insert_many(value_list)
        return mycol_id.inserted_ids  # 返回insert_id集合，即插入文档的id值

    def select_one_collection(self, collection_name: str, search_col: dict = None) -> Any:  # 获取一条数据
        """
        :param collection_name:
        :param search_col:
        :return:
        """
        """search_col：只能是dict类型,key大于等于一个即可，也可为空
        可使用修饰符查询：{"name": {"$gt": "H"}}#读取 name 字段中第一个字母 ASCII 值大于 "H" 的数据
        使用正则表达式查询：{"$regex": "^R"}#读取 name 字段中第一个字母为 "R" 的数据"""
        my_col = self.db[collection_name]
        try:
            result = my_col.find_one(search_col)  # 这里只会返回一个对象，数据需要自己取
            return result
        except TypeError as e:
            logger.error('查询条件只能是dict类型')
            return None

    def select_all_collection(self, collection_name: str, search_col: dict = None, limit_num: int = sys.maxsize,
                              sort_col: str = 'None_sort',
                              sort='asc'):
        """
        :param collection_name:
        :param search_col:
        :param limit_num:
        :param sort_col:
        :param sort:
        :return:
        """
        """search_col：只能是dict类型,key大于等于一个即可，也可为空
        可使用修饰符查询：{"name": {"$gt": "H"}}#读取 name 字段中第一个字母 ASCII 值大于 "H" 的数据
        使用正则表达式查询：{"$regex": "^R"}#读取 name 字段中第一个字母为 "R" 的数据
        limit_num:返回指定条数记录，该方法只接受一个数字参数(sys.maxsize:返回一个最大的整数值)"""
        my_col = self.db[collection_name]
        try:
            if sort_col == False or sort_col == 'None_sort':
                results = my_col.find(search_col).limit(
                    limit_num)  # 这里只会返回一个对象，数据需要自己取
            else:
                sort_flag = 1
                if sort == 'desc':
                    sort_flag = -1
                results = my_col.find(search_col).sort(
                    sort_col, sort_flag).limit(limit_num)  # 这里只会返回一个对象，数据需要自己取
            result_all = [i for i in results]  # 将获取到的数据添加至list
            return result_all
        except TypeError as e:
            logger.error('查询条件只能是dict类型')
            return None

    def select_count_collection(self, collection_name: str, search_col: dict = None):
        """
        统计查询数量
        :param collection_name:
        :param search_col:
        :return:
        """
        my_col = self.db[collection_name]

        results_count = my_col.count_documents(
            search_col)  # 这里只会返回一个对象，数据需要自己取

        return results_count

    def update_one_collecton(self, collection_name: str, search_col: dict, update_col: dict):
        """
        :param collection_name:
        :param search_col:
        :param update_col:
        :return:
        """
        """该方法第一个参数为查询的条件，第二个参数为要修改的字段。
            如果查找到的匹配数据多余一条，则只会修改第一条。
            修改后字段的定义格式： { "$set": { "alexa": "12345" } }"""
        my_col = self.db[collection_name]
        try:
            relust = my_col.update_one(search_col, update_col)
            return relust
        except TypeError as e:
            logger.error('查询条件与需要修改的字段只能是dict类型')
            return None

    def update_batch_collecton(self, collection_name: str, search_col: dict, update_col: dict):
        """
        :param collection_name:
        :param search_col:
        :param update_col:
        :return:
        """
        """批量更新数据"""
        my_col = self.db[collection_name]
        try:
            relust = my_col.update_many(search_col, update_col)
            return relust
        except TypeError as e:
            logger.error('查询条件与需要修改的字段只能是dict类型')
            return None

    def delete_one_collection(self, collection_name: str, search_col: dict):  # 删除集合中的文档
        """
        :param collection_name:
        :param search_col:
        :return:
        """
        my_col = self.db[collection_name]
        try:
            relust = my_col.delete_one(search_col)
            return relust
        except TypeError as e:
            logger.error('查询条件与需要修改的字段只能是dict类型')
            return None

    def delete_batch_collection(self, collection_name: str, search_col: dict):  # 删除集合中的多个文档
        """
        :param collection_name:
        :param search_col:
        :return:
        """
        """删除所有 name 字段中以 F 开头的文档:{ "name": {"$regex": "^F"} }
        删除所有文档：{}"""
        my_col = self.db[collection_name]
        try:
            relust = my_col.delete_many(search_col)
            return relust
        except TypeError as e:
            logger.error('查询条件与需要修改的字段只能是dict类型')
            return None

    def drop_collection(self, collection_name: dict):
        """
        :param collection_name:
        :return:
        """
        """删除集合，如果删除成功 drop() 返回 true，如果删除失败(集合不存在)则返回 false"""
        my_col = self.db[collection_name]
        result = my_col.drop()
        return result

    def get_connections(self):  # 获取所有的connections
        """
        :return:
        """
        return self.db.list_collection_names()

    def close_db(self) -> str:
        """
        :return:
        """
        self.conn.close()
        logger.info('mongo连接已关闭')
        return 'mongo连接已关闭'

# if __name__ == '__main__':
    #     import uuid
    #     import bson
    #     from dateutil import parser
    #
    #     host = '10.0.34.13'
    #     port = 37017
    #     db_name = 'potato_kube'
    #     user = 'potatokube'
    #     password = 'ecbe95b861'
    #
    #     M = MongodbHandle(host, port, db_name, user, password)
    #
    #     table_list = M.get_connections()
    # ['tekton_task', 'argo_operator', 'argo_workflow', 'potato_kube', 'tekton_pipeline']

    # # 删除流程
    # M.delete_batch_collection(collection_name='argo_workflow',
    #                           search_col={"name": {"$regex": "^workflow-form-"}})
    #
    # operator = M.select_all_collection(collection_name='argo_workflow',
    #                                    search_col={"name": {"$regex": "^workflow-form-"}})
    # # {"name": { $regex: / operator - form - /}}
    # operator_count = M.select_count_collection(collection_name='argo_workflow',
    #                                            search_col={"name": {"$regex": "^workflow-form-"}})
    # print(operator)
    # print(operator_count)

    # 删除算子
    # M.delete_batch_collection(collection_name='argo_operator',
    #                           search_col={"name": {"$regex": "^operator-code-"}})
    #
    # operator = M.select_all_collection(collection_name='argo_operator',
    #                                    search_col={"name": {"$regex": "^operator-code-"}})
    # # {"name": { $regex: / operator - form - /}}
    # operator_count = M.select_count_collection(collection_name='argo_operator',
    #                                            search_col={"name": {"$regex": "^operator-code-"}})
    # print(operator)
    # print(operator_count)

    # M.insert_collection('argo_workflow', biaodan)
    # M.insert_collection('argo_workflow', daima)
    # logger.info(f"插入条数：{i * 2}")
