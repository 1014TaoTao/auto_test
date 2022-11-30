#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__title__  = pandas操作Excel工具类
"""


import datetime
import inspect
import warnings

import numpy
import pandas as pd
from pandas import ExcelWriter


class Check(object):
    """
     获取对应方法的参数的key-value
      inspect.getcallargs(method,*args,**kwargs)
      结果：{'self': <__main__.LgyHandleExcel object at 0x000001C7F26B5B20>, 'columns_name': '备注2', 'value': '123'}

    """

    @staticmethod
    def check_columns(method, *args, **kwargs):
        parameter_dict = inspect.getcallargs(method, *args, **kwargs)
        # print(parameter_dict)
        if "columns_name" in parameter_dict.keys():
            temp_list = [parameter_dict["columns_name"]]
        elif "columns_name_list" in parameter_dict.keys():
            temp_list = parameter_dict["columns_name_list"]
        else:
            raise NameError("请不要修改【{}】,参数名称".format(method.__name__))

        if "self" not in parameter_dict.keys():
            raise NameError("【{}】,方法参数首个名称请使用【self】".format(method.__name__))

        # 获取传入方法的第一个参数：self
        method_self = parameter_dict["self"]

        return set(temp_list) < set(method_self.columns)

    @staticmethod
    def check_columns_exist(message):
        def decorator(method):
            def wrapper(*args, **kwargs):
                # 判断字段是否是excel中的真子集
                check_columns_result = Check.check_columns(
                    method, *args, **kwargs)
                if not check_columns_result:
                    raise Exception(message)

                return method(*args, **kwargs)

            return wrapper

        return decorator

    @staticmethod
    def check_columns_not_exist(message):
        def decorator(method):
            def wrapper(*args, **kwargs):
                # 判断字段是否是excel中的真子集
                check_columns_result = Check.check_columns(
                    method, *args, **kwargs)
                if check_columns_result:
                    raise Exception(message)

                return method(*args, **kwargs)

            return wrapper

        return decorator


class LgyHandleExcel(object):
    """
    dataFrame 更多用法参考：https://www.pypandas.cn/docs/getting_started/dsintro.html#dataframe
    如果数据是：百分比,读取出来时float,可以使用列，进行列批量操作处理
    """
    ErrorColumnsName = "列名不合法"
    ErrorIndex = "索引不合法"

    def __init__(self, filename, datetime_columns: str = False, sheet_name: str = 0, dataframe=None):
        """
        :param filename: excel文件名
        :param datetime_columns: excel日期的字段 -如果用到筛选日期方法，必须填写
        :param sheet_name: 子表名: 索引或者字符串名字【默认：第一个子表】
        :param dataframe : 可以传入该数据类型，进行操作，如果存在，则忽略excel的内容
        """
        self.__fileName = filename
        self.__time_columns = datetime_columns

        if not dataframe:
            self.excel_data = pd.read_excel(self.__fileName, sheet_name=sheet_name,
                                            parse_dates=self.__time_columns if not self.__time_columns else [
                                                self.__time_columns])
        else:
            self.excel_data = dataframe

    def save_excel(self, filename: str = None, sheet_name: str = "Sheet1"):
        """
        self.excel_data 为：dataFrame类型
        保存数据为excel：
                        filename=None：默认保存到本文件，
                        传入文件名，则保存新excel
        """
        if not filename:
            filename = self.__fileName

        if filename.rsplit(".", 1)[-1] == "xls":
            warnings.warn("建议的excel格式为：【xlsx】 结尾！", DeprecationWarning)

        self.excel_data.to_excel(filename, index=False, sheet_name=sheet_name)

    def get_excel_columns_name(self) -> list:
        """
        获取数据表的所有列名
        """
        return self.excel_data.columns

    def get_excel_line_index(self) -> list:
        """
        获取数据表的行索引
        """
        return self.excel_data.index

    def set_excel_columns_name(self, columns_dict: dict):
        """
        修改对应的列名： {"原名":"新名"}
        columns_dict={"采集时间": "a", "App名称": "b"}
        :return:
        """
        self.excel_data = self.excel_data.rename(columns=columns_dict)

    def __set_excel_index_value(self, index_dict: dict):
        """
        修改对应的列名： {"原索引值":"新索引值"}
        index_dict={0: "a", 1: "b"}
        :return:
        """
        self.excel_data = self.excel_data.rename(index=index_dict)

    def get_line_data(self, index: int) -> dict:
        """
        获取指定行的数据
        :param index:  第几行（0开始）
        :return:
        """
        return self.excel_data.loc[index]

    def get_columns_data(self, columns_name: str) -> list:
        """
        获取指定列的数据
        :param columns_name: 指定的列名
        :return:
        """
        return self.excel_data[columns_name]

    def get_cell_data(self, line_index: int, column_name: str) -> str:
        """
        获取指定单元格的数据
        :param line_index:   行数
        :param column_name:  列名
        :return:
        """
        line_data = self.get_line_data(line_index)
        return line_data[column_name]

    def set_cell_data(self, line_index: int, columns_name: str, value: any):
        """
        设置指定单元格的 数据

        """
        self.excel_data.loc[line_index, columns_name] = value

    def append_line_data(self, data: dict):
        """
            往DataFrame 最后一行追加一行数据
            如:df = df.append({"ID": 123, "name": "xiao"}, ignore_index=True)

        """
        self.excel_data = self.excel_data.append(data, ignore_index=True)

    def append_more_line_data(self, data: list[dict]):
        """
            往DataFrame 最后一行追加多行数据
            如:df = df.append([{"ID": 123, "name": "xiao"},{"ID": 124, "name": "xiao"}], ignore_index=True)

        """
        self.excel_data = self.excel_data.append(data, ignore_index=True)

    def insert_line_data(self, data: dict, target_index):
        """
        指定行插入数据
        """

        current_index_list = self.get_excel_line_index()
        if target_index not in current_index_list:
            raise IndexError(LgyHandleExcel.ErrorIndex)

        if target_index == 0:
            self.excel_data.loc[-1] = data
        else:
            # 插入目标位置前的索引均-1
            for i in range(target_index):
                self.__set_excel_index_value({i: i - 1})

            # 插入数据设置索引为-2
            self.excel_data.loc[-2] = data
            # 设置插入的数据放置目标位置
            self.__set_excel_index_value({-2: target_index - 1})
        # 重新生成索引
        self.excel_data.index = self.excel_data.index + 1
        self.excel_data = self.excel_data.sort_index()

    @Check.check_columns_not_exist(message=ErrorColumnsName)
    def append_columns(self, columns_name: str, value: any = None):
        """
        添加一列，默认值为None
        :param columns_name:
        :param value:
        :return:
        """
        self.excel_data[columns_name] = value

    @Check.check_columns_exist(message=ErrorColumnsName)
    def set_columns_value(self, columns_name: str, value: any = None):
        """
        统一设置一行的值
        统一设置列与其他列的计算：可参考:https://www.pypandas.cn/docs/getting_started/dsintro.html#dataframe
        :param columns_name:
        :param value:
        :return:
        """
        self.excel_data[columns_name] = value

    @Check.check_columns_exist(message=ErrorColumnsName)
    def del_columns(self, columns_name_list: list, inplace=True):
        """
        删除指定的列,可以多个
        :param columns_name_list:要删除的列名-列表
        :param inplace:
                inplace=False，删除操作不改变原数据，而是返回一个执行删除操作后的新dataframe；
                inplace=True，默认直接在原数据上进行删除操作，删除后无法返回
        :return:
        """
        self.excel_data.drop(columns=columns_name_list, inplace=inplace)

    @Check.check_columns_exist(message=ErrorColumnsName)
    def select_columns(self, columns_name_list: list):
        """
        获取多列的数据
        :param columns_name_list: 要选择的列名-列表
        :return:  返回选择的数据，不修改原数据
        """
        return self.excel_data[columns_name_list]

    def __del_line(self, *line_index, inplace=True):
        """
        删除指定的行  修改源数据
        :param line_index:  列的索引
        :param inplace:
                inplace=False，该删除操作不改变原数据，而是返回一个执行删除操作后的新dataframe；
                inplace=True，默认直接在原数据上进行删除操作
        :return:
        """
        self.excel_data.drop(index=list(line_index), inplace=inplace)

    def del_line(self, select_dict: dict, excel_data=None, inplace=True, ):
        """
        删除指定行数据
        :param select_dict: {"列名":"值"}
        :param excel_data:
        :param inplace: 默认为True  修改源数据
        :return:
        """
        result_index = self.select_data(select_dict, excel_data).index
        self.__del_line(*result_index, inplace=inplace)

    def select_data(self, select_dict: dict, excel_data=None):
        """
        按照列值，进行多重筛选数据,注意类型，比如excel是数字，这里就是数字类型
        提示：如果excel对应的单元格为空时
              类型：为数字、字符串     需要使用=》 numpy.float64("NaN") 进行匹配
              类型：日期类型(datetime) 需要使用=》 "NaT" 进行匹配
        :param select_dict: {"a":1,"b":""}
        :param excel_data:
        :return:
        """
        result = excel_data if excel_data else self.excel_data
        for key, value in select_dict.items():
            if value == "" and key == self.__time_columns:
                value = "NaT"
            elif value == "":
                value = numpy.float64("NaN")
            result = result.loc[self.excel_data[key].isin([value])]
        return result

    @Check.check_columns_exist(message=ErrorColumnsName)
    def select_data_range(self, columns_name: str, start_range: float, end_range: float = None, excel_data=None):
        """
        按照列值，进行筛选，主要针对的数值类型进行操作，其他可能会有问题
        :param columns_name:
        :param start_range:
        :param end_range:
        :param excel_data:
        :return:
        """
        result = excel_data if excel_data else self.excel_data
        if not end_range:
            return result[result[columns_name] >= start_range]
        else:
            return result[(result[columns_name] >= start_range) & (result[columns_name] <= end_range)]

    def select_data_time(self, start_data: tuple, end_data: tuple = None, excel_data=None):
        """
        按照日期，进行筛选     start_data <=选择时间<= end_data
        :param start_data: 开始时间（年,月,日,时,分,秒）
        :param end_data:  结束时间
        :param excel_data:
        :return:
        """

        s_data = datetime.datetime(*start_data)
        result = excel_data if excel_data else self.excel_data

        if not end_data:
            return result[result[self.__time_columns] >= s_data]
        else:
            e_data = datetime.datetime(*end_data)
            return result[(result[self.__time_columns] >= s_data) & (result[self.__time_columns] <= e_data)]

    columns = property(fget=get_excel_columns_name, doc="获取excel的列名")
    index = property(fget=get_excel_line_index, doc="获取excel的行索引")

    @Check.check_columns_exist(message=ErrorColumnsName)
    def sort_columns(self, columns_name_list: list, ascending=True, inplace=True, kind='quicksort', na_position='last'):
        """
        :param columns_name_list: 要排序的列表
        :param ascending: True为升序
        :param inplace: True为排序后代替现有的数据
        :param kind: 排序算法， {'quicksort'，'mergesort'，'heapsort'}，默认 'quicksort'
        :param na_position：排序算法， 空值，默认排在最后面 {"first","last"}
        :return:
        """
        self.excel_data.sort_values(by=columns_name_list, axis=0, ascending=ascending, inplace=inplace,
                                    kind=kind, na_position=na_position)


class LgyNewExcel(object):
    def __init__(self, filename, data_sheet_list: list[dict]):
        """

        :param filename:
        :param data_sheet_list:   [
                                    {
                                    "data":dataFrame,
                                    "sheet_name":sheet_name
                                   }
                                   ]
        example:LgyNewExcel("123.xlsx",[{"data":d1,"sheet_name":"d1"},{"data":d2,"sheet_name":"d2"}])
        """
        self.__filename = filename
        self.__data_sheet_list = data_sheet_list

    @Check.check_columns_exist(message=LgyHandleExcel.ErrorColumnsName)
    def save_excel(self):
        with ExcelWriter(self.__filename) as writer:
            for temp_list in self.__data_sheet_list:
                temp_list["data"].to_excel(
                    writer, index=False, sheet_name=temp_list["sheet_name"])


class LgyGroupData(object):

    def __init__(self, dataframe, columns_name_list: list, sort=True):
        self.data = dataframe
        self.handle_result_data = None
        self.__group_by_columns(columns_name_list, sort)

    def __group_by_columns(self, columns_name_list: list, sort=True):
        """

        :param columns_name_list: 根据列进行分组
        :param sort: 默认升序
        :return: 返回分组对象
        """
        self.data = self.data.groupby(by=columns_name_list, sort=sort)

    def print_data(self):
        for name, group in self.data:
            print(name)
            print(group)

    def select_group(self, group_columns_key: tuple):
        """

        :param group_columns_key:  按照数据分组选择
                                    一个列的分组  (“列名1的值”)
                                    多个列的分组  (“列名1的值”,"列名2的值” )
        :return:  分组后的数据
        """

        return self.data.get_group(group_columns_key)

    def handle_group_data(self, handle_columns_name_list: list, func_list=None):
        """

        :param handle_columns_name_list:   需要统计的字段
        :param func_list:  max  min  sum   mean(平均数)  std(标准差) var(方差)
                    使用： func_list=["max"]   func_list=["max","min"]
        :return:  DataFrame对象
        """
        if func_list is None:
            func_list = ["sum"]
        self.handle_result_data = self.data[handle_columns_name_list].agg(
            func_list)
        return self.handle_result_data

    def get_handle_data(self, handle_columns_name: str, group_columns_key: tuple, func_name: str = "sum", ):
        """

        :param handle_columns_name:  处理的字段名称 如：handle_group_data方法中，handle_columns_name_list的一个值
        :param group_columns_key:    分组的key(初始化对象时，列的分组名称对应的值)
                                        一个列的分组  (“列名1的值”)
                                        多个列的分组  (“列名1的值”,"列名2的值” )
        :param func_name:           统计函数的名称
        :return:
        """
        return self.handle_result_data[handle_columns_name][func_name][group_columns_key]


def get_empty_excel(columns):
    """

    :param columns:  excel中的行标题
    :return:
    """
    return pd.DataFrame(columns=columns)
