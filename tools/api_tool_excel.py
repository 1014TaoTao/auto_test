# coding:utf-8
# ==============================
#         EXCEL处理封装
# ==============================

import re

import xlrd
import xlwt
from xlutils.copy import copy

from common import setting
from tools.api_tool_assert import Assert
from tools.api_tool_global_var import global_var
from tools.api_tool_headers import headersPack, read_token
from tools.api_tool_request import Requests
from tools.public_tool_log import logger
from common import consts
from tools.api_tool_login import Login


class ExcelPack:
    def __init__(self, file_name, sheet_id):
        self.logger = logger(setting.API_LOG_PATH)
        self.runs = Requests()

        self.sheet_id = sheet_id
        self.file_name = file_name

        self.pass_num = 0
        self.fail_num = 0

        self.sheet_data = self.get_sheet_data()  # 获取表数据

    # 获取sheet的内容
    def get_sheet_data(self):
        book = xlrd.open_workbook(self.file_name, formatting_info=True)
        sheet = book.sheet_by_index(self.sheet_id)
        return sheet

    # 获取行数
    def get_lines(self):
        return self.sheet_data.nrows

    # 获取某个单元格内容
    def get_cell_data(self, row, col):
        return self.sheet_data.cell(row, col).value

    # 向单元格写内容
    def write_cell_data(self, row, col, value, cell_style=0):
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

    # 生成依赖列表
    def get_case_list(self, row):
        case_col = global_var().get_case_depend()  # 获取依赖项
        case_depend = self.get_cell_data(row, case_col)
        case_depend_list = []
        if case_depend != "":
            case_depend_list = case_depend.split(";")
        return case_depend_list

    # 返回加入依赖后的json
    def get_case_json(self, row):
        json_data = eval(self.get_cell_data(row, global_var().get_data()))  # 获取入参。并由str转为dict
        depend_list = self.get_case_list(row)  # 获取依赖列表
        revise_list = self.get_revise_list(row)  # 获取依赖字段
        for i in range(len(depend_list)):
            case_str_list = depend_list[i].split(":")[1].split(",")
            case_id = depend_list[i].split(":")[0]
            revise_str = revise_list[i]
            for case_str in case_str_list:
                self.sheet_data = self.get_sheet_data()
                response = self.get_case_line(case_id, row)
                if response != u"【excel无法找到对应依赖的响应内容】":
                    try:
                        res_str = eval(response)['body']['data']['list'][0][case_str]  # 获取响应值
                        json_data[revise_str] = str(res_str)  # {id:9},在response获取得字段加入json_data字典中
                    except Exception as e:
                        return f'【在响应中获取依赖失败：{e}】'
                else:
                    self.logger.error('【excel无法找到对应依赖的响应内容】')
        # 写入返回数据
        deal_str = str(json_data).replace(r"', '", "',\n  '").replace("{'", "{\n  '").replace("'}", "'\n}")  # 格式化字典
        self.write_cell_data(row, global_var().get_data(), deal_str, cell_style=6)
        return json_data

    # 获取所依赖的用例响应值
    def get_case_line(self, case_str, row):
        for num in range(2, row):
            if case_str == self.get_cell_data(num, global_var().get_id()):
                response_data = self.get_cell_data(num, global_var().get_response())
                return response_data
        return u"【excel无法找到对应依赖的响应内容】"

    # 生成要修改的值列表
    def get_revise_list(self, row):
        case_col = global_var().get_filed_depend()
        case_depend = self.get_cell_data(row, case_col)
        case_depend_list = []
        if case_depend != "":
            case_depend_list = case_depend.split(",")
        return case_depend_list

    # 断言相等并写测试结果
    def assert_eq_write_result(self, row, res):
        # 在excel中写入结果
        try:
            write_str = str(res)
        except Exception as e:
            write_str = str(u"响应结果转字符串格式错误！")
            self.logger.error(f'响应结果转字符串格式错误:{e}')
        self.write_cell_data(row, global_var().get_response(), write_str, cell_style=2)  # 写响应结果
        self.logger.info(f"【响应结果写入excel：{res}】")
        # 断言加入列表，遍历列表
        try:
            if Assert().assert_code(int(self.get_expected_status_code(row)), res['code']) and \
                    Assert().assert_msg(self.get_expected_msg(row), res['body']['msg']) and \
                    Assert().assert_in_body(self.get_expected_data(row), str(res['body']['data'])):
                self.write_cell_data(row, global_var().get_result(), "PASS", cell_style=3)
                self.logger.info(
                    f"【测试用例：{self.get_case_name(row)}】===============>> 【PASS！】\n")
                self.pass_num += 1
                result = "pass"
                return result

            else:
                self.write_cell_data(row, global_var().get_result(), "FAIL", cell_style=4)
                self.logger.error(f"【测试用例：{self.get_case_name(row)}】===============>> 【FAIL！】\n")
                self.fail_num += 1
                result = "fail"
                return result
        except Exception as e:
            self.logger.info(f'【响应内容为空，无法断言，断言异常：{e}】')
            self.write_cell_data(row, global_var().get_result(), "FAIL", cell_style=4)
            self.logger.error(f"【测试用例：{self.get_case_name(row)}】===============>> 【FAIL！】\n")
            self.fail_num += 1
            result = "fail"
            return result

    # 输出测试总结
    def write_test_summary(self):
        all_num = self.pass_num + self.fail_num
        success_rate = round(self.pass_num / all_num, 2) * 100
        failure_rate = round(self.fail_num / all_num, 2) * 100
        res_str = f"【共执行{all_num}条】-【成功{self.pass_num}条】-【失败{self.fail_num}条】-【成功率{success_rate}%】-【失败率{failure_rate}%】"
        self.logger.info(f"【测试结果】======>{res_str}")
        return res_str

    # 获取用例id-title
    def get_case_name(self, row):
        # 拼接用例名称为：id+title
        case_name = self.get_cell_data(row, global_var().get_id()) + self.get_cell_data(row, global_var().get_fuction())
        return case_name

    # 处理url,获取需要匹配的字符串并返回url
    def get_new_url(self, row):

        api_url = self.get_cell_data(row, global_var().get_url())
        url = consts.APIHOST + api_url

        try:
            # 如果url中有{{}}类符号被识别为变量，获取所依赖得值到url中
            value = re.search("{{(.+?)}}", url).group()
            self.logger.info('【url中存在依赖关系，开始处理...】')
            list_url_params = value.replace("{{", "").replace("}}", "").split(":")
            case_id = list_url_params[0]
            case_str = list_url_params[1]
            response = self.get_case_line(case_id, row)
            if response != u"【excel无法找到对应依赖的响应内容】":
                try:
                    new_str = eval(response)['body']['data']['list'][0][case_str]  # 获取响应值
                    url = url.replace(value, str(new_str))
                    self.logger.info(f'【url处理完成...】')
                    return url
                except Exception as e:
                    return url, e
            else:
                self.logger.error('【excel无法找到url所需依赖字段】')
        except AttributeError:
            self.logger.info(f'【url中没有依赖正常执行...】')
            return url

    # 处理data
    def get_new_data(self, row):
        # 获取data,类型是str
        str_data = self.get_cell_data(row, global_var().get_data())
        # 处理data,如果依赖不为空，说明有需要得依赖，加入到入参中。
        if self.get_cell_data(row, global_var().get_case_depend()) != "":
            data = self.get_case_json(row)
        else:
            # dict,字符串str转为字典dict
            data = eval(str_data)
        return data

    # 处理headers
    def get_new_headers(self, row):
        # 处理header,字符串str转为字典dict
        headers_dict = eval(self.get_cell_data(row, global_var().get_header()))

        # 处理headers,如果是yes，说明headers中需要加入token
        if self.get_statue_token(row) == 'yes':  # 读cookie
            self.logger.info(f"【该用例需要加入token】")
            try:
                token = read_token()
                headers_dict["Authorization"] = token
                self.logger.info(f"【读取token于./data/api/token.txt文件，并加入headers成功】")
            except Exception as e:
                self.logger.error(f"【读取token错误！{e}】】")
        else:
            headers_dict = headers_dict
        return headers_dict

    # 处理method
    def get_new_method(self, row):
        method = self.get_cell_data(row, global_var().get_run_way())
        return method

    # 获取是否执行
    def get_run_status(self, row):
        run_status = self.get_cell_data(row, global_var().get_run())
        return run_status

    # 获取断言status_code
    def get_expected_status_code(self, row):
        expected_status_code = self.get_cell_data(row, global_var().get_status_code())
        return expected_status_code

    # 获取断言msg
    def get_expected_msg(self, row):
        expected_msg = self.get_cell_data(row, global_var().get_expect_msg())
        return expected_msg

    # 获取断言data
    def get_expected_data(self, row):
        expected_data = self.get_cell_data(row, global_var().get_expect_data())
        return expected_data

    # 是都写、读token
    def get_statue_token(self, row):
        return self.get_cell_data(row, global_var().get_token())

    # 写token状态
    def write_statue_token(self, row, res):
        try:
            # 写token
            if self.get_statue_token(row) == 'write':
                self.logger.info(f"【请求发送完成，该用例需要写入token】")
                try:
                    headersPack(res).create_headers()  # token写入文件
                    self.logger.info(f"【写入token至./data/api/token.txt文件完成】")
                except Exception as e:
                    self.logger.error(f"【写入token至./data/api/token.txt文件错误！{e}】")
            else:
                pass
        except Exception as e:
            self.logger.error(f"【写入token异常！{e}】")

    # 批量执行，执行excel测试用例
    def run_excel_case(self):

        all_case = []  # 存储所有的请求数据，用于传输给pytest的参数
        # 参数2标识从excel第3行开始执行
        for row in range(2, self.get_lines()):

            if self.get_run_status(row) == "yes":  # 是否运行
                # 用例标题
                case_name = self.get_case_name(row)
                self.logger.info(f"【测试用例：{case_name}】===============>> 【start】")
                # 处理method
                method = self.get_new_method(row)
                # 获取data
                data = self.get_new_data(row)
                # 处理url
                url = self.get_new_url(row)
                # 处理header,字符串str转为字典dict
                headers = self.get_new_headers(row)
                # 处理断言
                expected_status_code = self.get_expected_status_code(row)
                expected_msg = self.get_expected_msg(row)
                expected_data = self.get_expected_data(row)

                # 发请求
                res = self.runs.send_request(method=method, url=url, data=data, headers=headers)

                try:
                    if res['body']['msg'] != '未经授权的访问':
                        pass
                    elif res['body']['msg'] == '未经授权的访问':
                        Login().api_login()
                        headers = self.get_new_headers(row)
                        res = self.runs.send_request(method=method, url=url, data=data, headers=headers)
                except Exception as e:
                    return f'更新token异常：{e}'

                # 判断是否写入token
                self.write_statue_token(row, res)

                # 结果写入excel测试结果()==》断言
                result = self.assert_eq_write_result(row, res)

                case = {
                    "result": result,
                    "title": case_name,
                    "url": url,
                    "method": method,
                    "headers": headers,
                    "data": data,
                    "status_code": expected_status_code,
                    "expected_msg": expected_msg,
                    "expected_data": expected_data,
                    "res": res
                }
                all_case.append(case)
            else:
                self.logger.info(f"【测试用例：{self.get_case_name(row)}】===============>> 【不执行】\n")
                self.write_cell_data(row, global_var().get_result(), "SKIP", cell_style=5)  # excel结果列写入跳过
                # self.write_cell_data(row, global_var().get_response(), "", cell_style=2)  # 清空响应
        self.write_test_summary()  # 输出测试结果
        return all_case


# 测试
if __name__ == '__main__':
    from common.setting import API_EXCEL_FILE

    excel = ExcelPack(API_EXCEL_FILE, 0)
    # 批量执行
    excel.run_excel_case()
    # 执行单条
    # excel.single_excel_case(3)
