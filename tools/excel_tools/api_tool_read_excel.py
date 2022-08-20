#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ==============================
#         EXCEL读取封装
# ==============================
"""
@Time    : 2022/2/12 13:56
@Author  : ZhangTAO
@File    : api_tool_read_excel.py
@Software: PyCharm
"""
import os.path

import filetype  # 判断上传文件类型
import xlrd
import xlwt
from xlutils.copy import copy

from common.setting import upload_file
from tools.common_tools.api_tool_global_var import global_var


class ReadExcel:
    def __init__(self, file_name: str, sheet_id: int):
        """
        :param file_name:
        :param sheet_id:
        """
        self.file_name = file_name
        self.sheet_id = sheet_id

        self.sheet_data = self.get_sheet_data()  # 获取表数据

    # 获取sheet的内容
    def get_sheet_data(self):
        """
        :return:
        """
        book = xlrd.open_workbook(self.file_name, formatting_info=True)
        sheet = book.sheet_by_index(self.sheet_id)
        return sheet

    # 获取行数
    def get_lines(self):
        """
        :return:
        """
        return self.sheet_data.nrows

    # 获取某个单元格内容
    def get_cell_data(self, row: int, col: int):
        """
        :param row:
        :param col:
        :return:
        """
        return self.sheet_data.cell(row, col).value

    # 向单元格写内容
    def write_cell_data(self, row: int, col: int, value: str, cell_style: int = 0):
        """
        :param row:
        :param col:
        :param value:
        :param cell_style:
        :return:
        """
        al = xlwt.Alignment()
        style = xlwt.XFStyle()
        font = xlwt.Font()
        if cell_style == 1:
            al.vert = 0x01  # 设置垂直居中
            al.wrap = 1  # 自动换行
        elif cell_style == 2:
            al.vert = 0x01  # 设置垂直居中
        elif cell_style == 3:
            al.vert = 0x01  # 设置垂直居中
            font.bold = True  # 设置粗体
            font.colour_index = 3  # 设置绿色
        elif cell_style == 4:
            al.vert = 0x01  # 设置垂直居中
            font.bold = True  # 设置粗体
            font.colour_index = 2  # 设置红色
        elif cell_style == 5:
            al.vert = 0x01  # 设置垂直居中
            font.bold = True  # 设置粗体
            font.colour_index = 40  # 设置蓝色 # 参考：http://www.javashuo.com/article/p-sfvgazwx-c.html
        elif cell_style == 6:
            al.vert = 0x01  # 设置垂直居中
            font.bold = True  # 设置粗体
            font.colour_index = 4  # 设置紫色 # 参考：http://www.javashuo.com/article/p-sfvgazwx-c.html
        style.alignment = al

        style.font = font

        book = xlrd.open_workbook(self.file_name, formatting_info=True)

        book_copy = copy(book)

        sheet = book_copy.get_sheet(self.sheet_id)

        sheet.write(row, col, value, style)

        book_copy.save(self.file_name)

    # 获取用例id
    def get_case_id(self, row: int):
        """
        :param row:
        :return:
        """
        return self.get_cell_data(row, global_var().get_id())

    # 获取用例模块名称
    def get_case_mode(self,row:int):
        """
        :param row:
        :return:
        """
        case_mode = self.get_cell_data(row, global_var().get_module())
        return case_mode

    # 获取用例功能名称
    def get_case_title(self, row: int):
        """
        :param row:
        :return:
        """
        return self.get_cell_data(row, global_var().get_fuction())

    # 获取method
    def get_new_method(self, row: int):
        """
        :param row:
        :return:
        """
        method = self.get_cell_data(row, global_var().get_run_way())
        return method

    # 获取header
    def get_headers(self, row: int):
        """
        :param row:
        :return:
        """
        return self.get_cell_data(row, global_var().get_header())

    # 获取是否执行
    def get_run_status(self, row: int):
        """
        :param row:
        :return:
        """
        run_status = self.get_cell_data(row, global_var().get_run())
        return run_status

    # 获取断言status_code
    def get_expected_status_code(self, row: int):
        """
        :param row:
        :return:
        """
        expected_status_code = self.get_cell_data(row, global_var().get_status_code())
        return expected_status_code

    # 获取断言msg
    def get_expected_msg(self, row: int):
        """
        :param row:
        :return:
        """
        expected_msg = self.get_cell_data(row, global_var().get_expect_msg())
        return expected_msg

    # 获取断言data
    def get_expected_data(self, row: int):
        """
        :param row:
        :return:
        """
        expected_data = self.get_cell_data(row, global_var().get_expect_data())
        return expected_data

    # 获取是否写、读token
    def get_statue_token(self, row: int):
        """
        :param row:
        :return:
        """
        return self.get_cell_data(row, global_var().get_token())

    # 获取请求data
    def get_data_info(self, row: int):
        """
        :param row:
        :return:
        """
        return self.get_cell_data(row, global_var().get_data())

    # 获取url
    def get_url_api(self, row: int):
        """
        :param row:
        :return:
        """
        return self.get_cell_data(row, global_var().get_url())

    # 获取依赖
    def get_case_depend_info(self, row: int):
        """
        :param row:
        :return:
        """
        return self.get_cell_data(row, global_var().get_case_depend())

    # 获取修改的依赖列表
    def get_case_filed_depend(self, row: int):
        """
        :param row:
        :return:
        """
        return self.get_cell_data(row, global_var().get_filed_depend())

    # 获取响应结果列
    def get_response_info(self, row: int):
        """
        :param row:
        :return:
        """
        return self.get_cell_data(row, global_var().get_response())

    # 获取base_url
    def get_base_url_info(self, row: int):
        """
        :param row:
        :return:
        """
        return self.get_cell_data(row, global_var().get_base_url())

    # 获取参数类型
    def get_excel_type_data(self, row: int):
        """
        :param row:
        :return:
        """
        return self.get_cell_data(row, global_var().get_type_data())

    # 获取上传文件地址
    def get_upload_file_path(self, row: int):
        """
        :param row:
        :return:
        """
        file_name = self.get_cell_data(row, global_var().get_upload_path())
        if file_name != '':
            file_path = os.path.join(upload_file, file_name)
            # 暂时只是单文件上传，待优化为多文件上传
            if file_path != '':
                file = [
                    ('file', (file_name, open(file_path, 'rb'), filetype.guess(file_path)))
                ]
            else:
                file = None
        else:
            file = None
        return file
