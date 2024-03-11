'''
Author: ZhangTao 948080782@qq.com
Date: 2022-11-30 13:53:50
LastEditors: ZhangTao 948080782@qq.com
LastEditTime: 2022-11-30 14:14:42
FilePath: \pytest_auto_uitest_apitest\tools\excel_tools\ui_tool_read_excel.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# -*- coding:utf-8 -*-

import os

import openpyxl

from common import setting
from tools.logs_tools.public_tool_log import logger


class ExcelOperate:
    # 向excel中写入数据
    """
    @ param Result
    @ param RowNum
    @ param ColNum
    @ param Path
    @ param SheetName
    """

    def __init__(self):
        self.logger = logger(setting.UI_LOG_PATH)

    # 使用openpyxl读取单元格值
    def read_cell(self, excel_path, sheet_name, row_num, cell_num):
        wb = openpyxl.load_workbook(excel_path)
        s1 = wb[sheet_name]
        result = s1.cell(row_num, cell_num).value
        self.logger.info("使用openpyxl读取EXCEL单元格,单元格值为[{0}]".format(result))
        return result

    # 使用openpyxl写excel_path路径的sheet_name中的第row_num行第cell_num列，写入value值
    def write_cell(self, excel_path, sheet_name, row_num, cell_num, value):
        if not os.path.exists(excel_path):
            wb = openpyxl.Workbook()
            sh = wb.create_sheet(sheet_name)
        else:
            wb = openpyxl.load_workbook(excel_path)
            sh = wb[sheet_name]
        sh.cell(row_num, cell_num).value = value
        wb.save(excel_path)
        self.logger.info("使用openpyxl写入EXCEL单元格成功")
        