# -*- coding:utf-8 -*-
import os
import time

import yaml
from selenium.webdriver.common.by import By

from common import setting
from tools.public_tool_log import logger

logger = logger(setting.UI_LOG_PATH)

# 元素定位的类型
LOCATE_MODE = {
    'css': By.CSS_SELECTOR,
    'xpath': By.XPATH,
    'name': By.NAME,
    'id': By.ID,
    'class': By.CLASS_NAME
}


def inspect_element():
    """审查所有的元素是否正确"""
    start_time = time.time()
    for i in os.listdir(setting.UI_YAML_DIR):
        _path = os.path.join(setting.UI_YAML_DIR, i)
        if os.path.isfile(_path):
            with open(_path, encoding='utf-8') as f:
                data = yaml.safe_load(f)
                for k in data.values():
                    pattern, value = k.split('==')
                    if pattern not in LOCATE_MODE:
                        raise AttributeError('【%s】路径中【%s]元素没有指定类型' % (i, k))
                    if pattern == 'xpath':
                        assert '//' in value, '【%s】路径中【%s]元素xpath类型与值不配' % (
                            i, k)
                    if pattern == 'css':
                        assert '//' not in value, '【%s】路径中【%s]元素css类型与值不配' % (
                            i, k)
                    if pattern in ('id', 'name', 'class'):
                        assert value, '【%s】路径中【%s]元素类型与值不匹配' % (i, k)
    end_time = time.time()

    logger.info(f"ui自动化，校验元素定位data格式【END！用时 %.3f秒！" % (end_time - start_time))

# if __name__ == '__main__':
#     inspect_element()
