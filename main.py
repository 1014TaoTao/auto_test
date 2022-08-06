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

    Go = RunTest(type_test=type_test)
    Go.run()
