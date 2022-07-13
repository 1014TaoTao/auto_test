# coding:utf-8
# ==============================
#       EXCEL读取出来的数据处理封装
# ==============================
import re
from typing import Tuple, Union, Any, List, Dict

from requests import Response

from common import setting
from tools.assert_tools.api_tool_assert import Assert
from tools.common_tools.api_tool_global_var import global_var
from tools.common_tools.api_tool_headers import read_token
from tools.common_tools.api_tool_login import Login
from tools.excel_tools.api_tool_read_excel import ReadExcel
from tools.requests_tools.api_tool_reponse import Response
from tools.requests_tools.api_tool_request import Requests
from tools.logs_tools.public_tool_log import logger


class ExcelPack(ReadExcel):
    def __init__(self, file_name: str, sheet_id: int):
        super().__init__(file_name, sheet_id)
        self.logger = logger(setting.API_LOG_PATH)
        self.runs = Requests()

        self.pass_num = 0
        self.fail_num = 0

    # 生成依赖列表
    def get_case_list(self, row: int) -> list:
        """
        :param row:
        :return:
        """
        case_depend = self.get_case_depend_info(row)
        case_depend_list = []
        if case_depend != "":
            case_depend_list = case_depend.split(";")
        return case_depend_list

    # 获取所依赖的用例响response
    def get_case_line(self, case_str: str, row: int) -> any:
        """
        :param case_str:
        :param row:
        :return:
        """
        for num in range(2, row):
            if case_str == self.get_case_id(num):
                response_data = self.get_response_info(num)
                return response_data
        return u"【excel无法找到对应依赖的响应内容】"

    # 生成要修改的值列表
    def get_revise_list(self, row: int) -> list:
        """
        :param row:
        :return:
        """
        case_col = global_var().get_filed_depend()
        case_depend = self.get_cell_data(row, case_col)
        case_depend_list = []
        if case_depend != "":
            case_depend_list = case_depend.split(",")
        return case_depend_list

    # 断言相等并写测试结果
    def assert_eq_write_result(self, row: int, res: dict) -> str:
        """
        :param row:
        :param res:
        :return:
        """
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
                    Assert().assert_in_body(self.get_expected_data(row), str(res['body'])):
                self.write_cell_data(row, global_var().get_result(), "PASS", cell_style=3)
                self.logger.info(
                    f"【测试用例：{self.get_new_case_name(row)}】===============>> 【PASS！】\n")
                self.pass_num += 1
                result = "pass"
                return result

            else:
                self.write_cell_data(row, global_var().get_result(), "FAIL", cell_style=4)
                self.logger.error(f"【测试用例：{self.get_new_case_name(row)}】===============>> 【FAIL！】\n")
                self.fail_num += 1
                result = "fail"
                return result
        except Exception as e:
            self.logger.info(f'【响应内容为空，无法断言，断言异常：{e}】')
            self.write_cell_data(row, global_var().get_result(), "FAIL", cell_style=4)
            self.logger.error(f"【测试用例：{self.get_new_case_name(row)}】===============>> 【FAIL！】\n")
            self.fail_num += 1
            result = "fail"
            return result

    # 输出测试总结
    def write_test_summary(self):
        """
        :return:
        """
        all_num = self.pass_num + self.fail_num
        success_rate = round(self.pass_num / all_num, 2) * 100
        failure_rate = round(self.fail_num / all_num, 2) * 100
        res_str = f"【共执行{all_num}条】-【成功{self.pass_num}条】-【失败{self.fail_num}条】-【成功率{success_rate}%】-【失败率{failure_rate}%】"
        self.logger.info(f"【测试结果】======>{res_str}")
        return res_str

    # 处理用例名称
    def get_new_case_name(self, row: int) -> str:
        """
        :param row:
        :return:
        """
        # 拼接用例名称为：id+title
        case_name = self.get_case_id(row) + self.get_case_title(row)
        return case_name

    # 处理url,获取需要匹配的字符串并返回url
    def get_new_url(self, row: int, APIHOST: str, ENVIRONMENTPORT: str) -> Union[
        Union[str, Tuple[Union[str, Any], Exception]], Any]:
        """
        :param row:
        :return:
        """
        api_url = self.get_url_api(row)
        base_url = self.get_base_url_info(row)
        if base_url == '':
            url = APIHOST + ENVIRONMENTPORT + api_url
        else:
            url = base_url + api_url
        try:
            # 如果url中有{{}}类符号被识别为变量，获取所依赖得值到url中
            value = re.search("{{(.+?)}}", url).group()
            if value:
                self.logger.info('【url中存在依赖关系，开始处理...】')
                list_url_params = value.replace("{{", "").replace("}}", "").split(":")
                case_id = list_url_params[0]
                response = self.get_case_line(case_id, row)

                if response != u"【excel无法找到对应依赖的响应内容】":

                    try:
                        # new_str = eval(response)['body']['data']['list'][0][case_str]  # 获取响应值
                        # url = url.replace(value, str(new_str))
                        case_str = list_url_params[1]
                        new_str = re.search(f'{case_str:}.*?(?=,)', response).group().replace(f"{case_str}",
                                                                                              "").replace(
                            "': ", "")
                        url = url.replace(value, new_str)
                        self.logger.info(f'【url依赖处理完成...】')

                        return url
                    except Exception as e:
                        self.logger.error(f'【url依赖处理失败，无法匹配...】')
                        return url, e
                else:
                    self.logger.error('【excel无法找到url所需依赖字段】')
            else:
                pass
        except AttributeError:
            self.logger.info(f'【url中没有依赖正常执行...】')
            return url

    # 处理data
    def get_new_data(self, row: int) -> Any:
        """
        :param row:
        :return:
        """
        # 获取data,类型是str
        global data
        str_data = self.get_data_info(row)
        # 处理data,如果依赖不为空，说明有需要得依赖，加入到入参中。
        # 入参不为空
        if str_data != "":
            # 有依赖
            if self.get_case_depend_info(row) != "":
                # 字典依赖
                if type(eval(str_data)) == dict:
                    data = self.get_case_json(row)
                # 列表依赖
                elif type(eval(str_data)) == list:
                    self.logger.error("列表类型入参，且有依赖情况没有做，遇到具体问题再处理。")  # 列表类型入参，依赖暂时没有做,
                    data = str_data
            # 无依赖
            else:
                # 字典入参
                if type(eval(str_data)) == dict:
                    data = eval(str_data)
                # 列表入参
                elif type(eval(str_data)) == list:
                    data = str_data
        # 入参为空
        else:
            # 有依赖（目前统一按字典处理）
            if self.get_case_depend_info(row) != "":
                data = self.get_case_json(row)
            # 无依赖
            else:
                data = None
        return data

    # 返回加入依赖后的json
    def get_case_json(self, row: int) -> Any:
        """
        :param row:
        :return:
        """
        str_data = self.get_data_info(row)  # 获取入参。并由str转为dict
        if str_data == '':
            str_data = '{}'
            dict_data = eval(str_data)
        else:
            dict_data = eval(str_data)
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
                        # res_str = eval(response)['body']['data']['list'][0][case_str]  # 获取响应值
                        # dict_data[revise_str] = str(res_str)  # {id:9},在response获取得字段加入json_data字典中

                        res_str = re.search(f'{case_str:}.*?(?=,)', response).group().replace(f"{case_str}",
                                                                                              "").replace(
                            "': ", "")
                        dict_data[revise_str] = res_str  # {id:9},在response获取得字段加入json_data字典中


                    except Exception as e:
                        self.logger.error(f'【在响应中获取依赖异常：{e}】')
                else:
                    self.logger.error('【excel无法找到对应依赖的响应内容】')
        # 写入返回数据
        deal_str = str(dict_data).replace(r"', '", "',\n  '").replace("{'", "{\n  '").replace("'}", "'\n}")  # 格式化字典
        self.write_cell_data(row, global_var().get_data(), deal_str, cell_style=6)
        return dict_data

    # 处理headers
    def get_new_headers(self, row: int) -> Any:
        """
        :param row:
        :return:
        """
        # 处理header,字符串str转为字典dict
        global headers_dict
        headers_str = self.get_headers(row)
        if headers_str != '':
            headers_dict = eval(headers_str)
            # 处理headers, 如果是yes，说明headers中需要加入token
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
        else:
            if self.get_statue_token(row) == 'yes':  # 读cookie
                headers_dict = {}
                self.logger.info(f"【该用例需要加入token】")
                try:
                    token = read_token()
                    headers_dict["Authorization"] = token
                    self.logger.info(f"【读取token于./data/api/token.txt文件，并加入headers成功】")
                except Exception as e:
                    self.logger.error(f"【读取token错误！{e}】】")
            else:
                headers_dict = None

        return headers_dict

    # 批量执行，执行excel测试用例
    def run_excel_case(self, APIHOST: str, ENVIRONMENTPORT: str, BASEHOST: str, LOGINHOST: str, LOGINDATA: dict,
                       USERNAME: str) -> Union[
        str, List[Dict[str, Union[Union[str, Tuple[Union[str, Any], Exception]], Any]]]]:
        """
        :return:
        """
        all_case = []  # 存储所有的请求数据，用于传输给pytest的参数
        # 参数2标识从excel第3行开始执行
        for row in range(2, self.get_lines()):

            if self.get_run_status(row) == "yes":  # 是否运行
                # 用例标题
                case_name = self.get_new_case_name(row)
                self.logger.info(f"【测试用例：{case_name}】===============>> 【start】")
                # 处理method
                method = self.get_new_method(row)
                # 获取参数类型
                parametric_key = self.get_excel_type_data(row)
                # 获取data
                data = self.get_new_data(row)
                # 获取file路径
                file = self.get_upload_file_path(row)
                # 处理url
                url = self.get_new_url(row, APIHOST, ENVIRONMENTPORT)
                # 处理header,字符串str转为字典dict
                headers = self.get_new_headers(row)
                # 处理断言
                expected_status_code = self.get_expected_status_code(row)
                expected_msg = self.get_expected_msg(row)
                expected_data = self.get_expected_data(row)
                # 发请求
                res = Response().result(
                    self.runs.send_request(method=method, url=url, data=data, headers=headers, file=file,
                                           parametric_key=parametric_key))
                try:
                    if res['body'] != 'response获取响应data异常':

                        if res['body']['msg'] != '未经授权的访问':
                            pass
                        else:
                            Login(BASEHOST, LOGINHOST, LOGINDATA, USERNAME).api_login()
                            headers = self.get_new_headers(row)
                            res = self.runs.send_request(method=method, url=url, data=data, headers=headers, file=file,
                                                         parametric_key=parametric_key)
                        # 结果写入excel测试结果()==》断言
                        result = self.assert_eq_write_result(row, res)
                    else:
                        # 在excel中写入结果
                        try:
                            write_str = str(res)
                        except Exception as e:
                            write_str = str(u"响应结果转字符串格式错误！")
                            self.logger.error(f'响应结果转字符串格式错误:{e}')
                        self.write_cell_data(row, global_var().get_response(), write_str, cell_style=2)  # 写响应结果
                        self.logger.info(f"【响应结果写入excel：{res}】")
                        self.write_cell_data(row, global_var().get_result(), "FAIL", cell_style=4)
                        self.logger.error(f"【测试用例：{self.get_new_case_name(row)}】===============>> 【FAIL！】\n")
                        self.fail_num += 1
                        result = "fail"

                except Exception as e:
                    return f'更新token异常：{e}'

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
            elif self.get_run_status(row) == "no":
                self.logger.info(f"【测试用例：{self.get_new_case_name(row)}】===============>> 【不执行】\n")
                self.write_cell_data(row, global_var().get_result(), "SKIP", cell_style=5)  # excel结果列写入跳过
                # self.write_cell_data(row, global_var().get_response(), "", cell_style=2)  # 清空响应
            else:
                self.logger.error(f"【测试用例：{self.get_new_case_name(row)}】===============>> 【请确认执行状态是yes或no】\n")
        self.write_test_summary()  # 输出测试结果
        return all_case

# # 测试
# if __name__ == '__main__':
#     from common.setting import API_EXCEL_FILE
#
#     excel = ExcelPack(file_name=API_EXCEL_FILE, sheet_id=0)
#     # 批量执行
#     excel.run_excel_case()
