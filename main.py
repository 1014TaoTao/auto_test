'''
Author: ZhangTao 948080782@qq.com
Date: 2022-11-30 13:53:50
LastEditors: ZhangTao 948080782@qq.com
LastEditTime: 2022-11-30 14:00:17
FilePath: \pytest_auto_uitest_apitest\main.py
# Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# coding: utf-8
import os

from tools.tool_run import RunTest

"""

1、执行前确认pytest.ini文件中testpath的路径

2、请输入正确的自动化测试类型:type_test = ['API', 'Api', 'api','UI', 'Ui', 'ui']
"""

if __name__ == '__main__':
    # type_test = 'UI'
    # type_test = 'API'

    type_test: str = os.environ['TESTTYPE']
    print(type_test)

    Go = RunTest(type_test=type_test)
    Go.run()
