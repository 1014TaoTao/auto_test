# -*- coding: utf-8 -*-
'''
@File  : operation_db.py
@Date  : 2020/4/3 10:36
@Author: 
@Desc  : 
'''


# coding = utf-8
import traceback
import logging

import pymysql
from config.config import Config

class Opera_DB:
    def __init__(self):
        self.conf = Config()

    def to_connect(self):
        try:
            self.db = pymysql.connect(
                host=self.conf.mysql_host,
                port=int(self.conf.mysql_port),
                user=self.conf.mysql_user,
                passwd=self.conf.mysql_password,
                db=self.conf.mysql_db,
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor
            )
            # self.cursor = self.db.cursor()
            return self.db
        except Exception as e:
            logging.error('数据库连接失败{}'.format(e))


    def commit_data(self, sql):
        """
        进行增删改操作
        :param sql:需要执行的sql
        :return: 影响行数
        """
        self.cursor = self.to_connect().cursor()
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
        finally:
            data = self.cursor.rowcount
            self.cursor.close()
            self.db.close()
            return int(data)

    def select_data(self, sql, way='one'):
        '''
        :param sql: 输入SQL
        :param way: 默认为one，只查出一条数据，way=all查出所有数据，以数组形式体现
        :return: 返回查询结果  ===》 all=>[{'id': 48}，{'id': 78}]     one => {'id': 48}
        '''
        self.cursor = self.to_connect().cursor()
        try:
            with self.cursor as cursor:
                cursor.execute(sql)
                data = {}
                if way == 'one':
                    data = cursor.fetchone()
                elif way == 'all':
                    data = cursor.fetchall()
                return data
                # self.connection.close()
        except Exception as e:
            traceback.print_exc()



        # try:
        #     self.cursor.execute(sql)
        #     if way == 'one':
        #         # data 返回的是字典
        #         data = self.cursor.fetchone()
        #
        #     elif way == 'all':
        #         # data 返回的是列表
        #         data = self.cursor.fetchall()
        #         # print(type(data))
        #         # for row in data:
        #         #     print(row)
        #         # print ("成功 {0}条数据,Database version : {1}，)".format(len(data),data))
        #
        #     else:
        #         data = 'type错误'
        # except Exception as e:
        #     data = e
        # finally:
        #     self.to_connect().close()
        #     self.cursor.close()

        # return data


if __name__ == '__main__':
    db = Opera_DB()
    sql = """SELECT * FROM mc_projects WHERE id =3;"""
    # sql = """delete from employee where empno = '1'"""
    way = 'all'
    data = db.select_data(sql, way=way)
    print(data)
