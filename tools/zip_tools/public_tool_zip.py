# -*- coding: utf-8 -*-#

import os
import zipfile


# 解压缩工具类
from tools.logs_tools.public_tool_log import logger


class ZipPath:
    def __init__(self):
        pass

    def zipDir(self, log_path, dirpath, outFullName):
        """
        压缩指定文件夹
        :param dirpath: 目标文件夹路径
        :param outFullName: 压缩文件保存路径+xxxx.zip
        :return: 无
        """
        logger(log_path).info("开始==>压缩测试报告")
        zp = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
        for path, dirnames, filenames in os.walk(dirpath):
            # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
            fpath = path.replace(dirpath, '')

            for filename in filenames:
                zp.write(os.path.join(path, filename), os.path.join(fpath, filename))
        zp.close()
        logger(log_path).info("完成==>压缩测试报告")

# 测试
# if __name__ == "__main__":
#     from common import setting
#
#     zip_path().zipDir(setting.API_REPORT_END_PATH, setting.API_FILE_LIST_PATH)
