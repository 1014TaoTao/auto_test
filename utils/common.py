# -*- coding: utf-8 -*-
'''
@File  : common.py
@Date  : 2020/4/3 10:36
@Author: 
@Desc  : 
'''

import os
import yaml
from base.element_path import Element
from utils.operation_db import Opera_DB
from configparser import ConfigParser
import shutil,requests


class CommonUtil:
    def __init__(self):
        self.db = Opera_DB()

    def get_data(self,title, value):

        self.config = ConfigParser()

        data_path = Element().PARAMS
        self.config.read(data_path, encoding='utf-8')
        return self.config.get(title, value)

    def get_filePath(self,project_name,file_Path):
        curPath = os.path.abspath(os.path.dirname(__file__))
        rootPath = curPath[:curPath.find(project_name) + len(project_name)]  # 获取myProject，也就是项目的根路径
        filePath = os.path.abspath(rootPath + file_Path)  # 获取tran.csv文件的路径

        return filePath

    def write_file(self, filepath, center):
        '''
        写文件
        :param filepath: 文件路径
        :param center:写入的内容
        :return:
        '''

        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(center)


    def append_file(self, filepath, center):
        '''
        追加至文件最后一行
        :param filepath: 文件路径
        :param center:写入的内容
        :return:
        '''

        with open(filepath, 'a+', encoding='utf-8') as file:
            file.write(center)

    def insert_file(self, filepath, center):
        '''
        插入文件第一行
        :param filepath: 文件路径
        :param center:写入的内容
        :return:
        '''
        with open(filepath, 'r+', encoding='utf-8') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(center + '\n' + content)

    def read_file(self, file_path):
        '''
        读取文件内容
        :param file_path: 文件路径
        :return:
        '''

        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def read_yaml(self, yaml_path):
        """
        读取yaml文件
        :param name: yml文件路径
        :return:
        """
        with open(yaml_path, 'r', encoding='utf-8') as file:
            return yaml.load(file)

    def read_params(self, file_name):
        """
        读取测试数据文件
        :param file_name:
        :return:
        """
        yaml_path = os.path.join(Element.PARAMS, file_name + '.yml')
        return self.read_yaml(yaml_path)

    def read_assert_sql(self):
        """
        读取整个sql文件
        :return:
        """
        print(Element.ASSERT_SQL)
        return self.read_yaml(Element.ASSERT_SQL)

    def get_sql(self, key):
        """
        通过关键字获取对应的sql
        :param key: yml 文件中的关键字
        :return:
        """

        return self.read_assert_sql()[key]['sql']

    def get_sql_data(self, key, way='one'):
        """
        通过关键字获取对应的sql执行后返回的数据
        :param key: 关键字
        :param way: 定义返回多少条数据，one一条，all是所有
        :return:
        """
        return self.db.select_data(self.get_sql(key), way)

    def execute_sql(self, sql):
        """
        执行增删改操作
        :param sql:sql
        :return:
        """
        return self.db.commit_data(sql)

    def remore_filedir(self, path):
        """
        删除文件夹下的所有文件
        :param path:
        :return:
        """
        if os.path.isdir(path):
            filelist = []
            filelist = os.listdir(path)  # 列出该目录下的所有文件名
            for f in filelist:
                filepath = os.path.join(path, f)
                if os.path.isfile(filepath):
                    os.remove(filepath)  # 若为文件，则直接删除
                    print(str(filepath) + " removed!")
                elif os.path.isdir(filepath):
                    shutil.rmtree(filepath, True)  # 若为文件夹，则删除该文件夹及文件夹内所有文件
                    print("dir " + str(filepath) + " removed!")
            shutil.rmtree(path, True)  # 最后删除path总文件夹

    def generate_environment(self, env_data):
        """
        生成运行环境xml文件
        :param data:
        :return:
        """
        message = []
        for key, values in env_data.items():
            message.append("""<parameter>
                            <key>{}</key>
                            <value>{}</value>
                            </parameter>
            """.format(key, values))
        xml = "<environment>" + ''.join(message) + "</environment>"
        self.write_file(Element.ENVIRONMENT,xml)



if __name__ == '__main__':
    c = CommonUtil()
    # data = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    # print(c.generate_environment(data))
    # print(c.read_assert_sql())
    f = c.get_filePath(project_name='potato-common',file_Path='params/image/')
    print(f)
