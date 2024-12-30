# -*- coding: utf-8 -*-

import pytest
from config import setting

args = [
    '-sv',
    f'--html={setting.HTML_REPORT_PATH}',
    '--self-contained-html',  # 静态html, 不需要额外的资源文件
    f'--log-file={setting.LOG_PATH}',
    '-W', 'ignore:Module already imported:pytest.PytestWarning'
]

if __name__ == '__main__':

    # 执行测试
    pytest.main(args)
