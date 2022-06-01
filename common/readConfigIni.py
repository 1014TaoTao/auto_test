# -*- coding: utf-8 -*-

import os
from configparser import ConfigParser


class Config:

    def __init__(self, conf_path):
        """
        :param conf_path:
        """
        """
        初始化
        """
        self.conf_path = conf_path
        self.config = ConfigParser()
        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保Config.ini配置文件存在！")
        self.config.read(self.conf_path, encoding='utf-8')

        # 195环境配置
        self.environment_195 = self.get_conf("environment_195", "environment")
        self.versionCode_195 = self.get_conf("environment_195", "versionCode")
        self.apihost_195 = self.get_conf("environment_195", "apihost")
        self.basehost_195 = self.get_conf("environment_195", "basehost")
        self.loginHost_195 = self.get_conf("environment_195", "loginHost")
        self.loginInfo_195 = self.get_conf("environment_195", "loginInfo")
        self.loginInfo_195 = self.get_conf("environment_195", "username")

        # 115环境配置
        self.environment_115 = self.get_conf("environment_115", "environment")
        self.versionCode_115 = self.get_conf("environment_115", "versionCode")
        self.apihost_115 = self.get_conf("environment_115", "apihost")
        self.basehost_115 = self.get_conf("environment_115", "basehost")
        self.loginHost_115 = self.get_conf("environment_115", "loginHost")
        self.loginInfo_115 = self.get_conf("environment_115", "loginInfo")
        self.loginInfo_195 = self.get_conf("environment_115", "username")

        # 120环境配置
        self.environment_120 = self.get_conf("environment_122", "environment")
        self.versionCode_120 = self.get_conf("environment_122", "versionCode")
        self.apihost_120 = self.get_conf("environment_122", "apihost")
        self.basehost_120 = self.get_conf("environment_122", "basehost")
        self.loginHost_120 = self.get_conf("environment_122", "loginHost")
        self.loginInfo_120 = self.get_conf("environment_122", "loginInfo")
        self.loginInfo_195 = self.get_conf("environment_122", "username")

        # 43_13环境配置
        self.environment_43_13 = self.get_conf("environment_34_13", "environment")
        self.versionCode_43_13 = self.get_conf("environment_34_13", "versionCode")
        self.apihost_43_13 = self.get_conf("environment_34_13", "apihost")
        self.basehost_43_13 = self.get_conf("environment_34_13", "basehost")
        self.loginHost_43_13 = self.get_conf("environment_34_13", "loginHost")
        self.loginInfo_43_13 = self.get_conf("environment_34_13", "loginInfo")
        self.loginInfo_195 = self.get_conf("environment_34_13", "username")

        # 邮件配置
        self.smtpserver = self.get_conf("email", "smtpserver")
        self.sender = self.get_conf("email", "sender")
        self.password = self.get_conf("email", "password")
        self.receiver = self.get_conf("email", "receiver")
        # 数据库配置
        self.databases_on_off = self.get_conf("databases", "sql_on_off")
        self.databases_host = self.get_conf("databases", "host")
        self.databases_user = self.get_conf("databases", "user")
        self.databases_port = self.get_conf("databases", "port")
        self.databases_passwd = self.get_conf("databases", "passwd")
        self.databases_db = self.get_conf("databases", "db")
        self.databases_charset = self.get_conf("databases", "charset")
        # 执行人员
        self.testers = self.get_conf("testers", "tester")
        # 是否开启删除历史报告功能
        self.delete_on_off = self.get_conf("delete_old_file", "delete_on_off")
        # 是否开启生成报告功能
        self.save_on_off = self.get_conf("save_report", "save_on_off")
        # 是否开启压缩报告功能
        self.zip_on_off = self.get_conf("zip_report", "zip_on_off")
        # 是否开启发送邮件功能
        self.send_on_off = self.get_conf("send_email", "send_on_off")
        # 运行结束是否直接打开报告
        self.open_on_off = self.get_conf("over_open_report", "open_on_off")
        # 控制台输出日志
        self.log_control_on_off = self.get_conf("control_log", "log_control_on_off")
        # 是否发送钉钉消息
        self.send_dingding_news_on_off = self.get_conf("send_dingding_news", "send_dingding_news_on_off")

    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def get_options_key_value(self, title):
        """
        以列表(name,value)的形式返回section中的每个值
        :param title: 某个section
        :return: list[tuple(key,value)]
        """
        return self.config.items(title)

    def get_all_section(self):
        """
        获取所有section
        """
        return self.config.sections()

    def get_options_by_section(self, title):
        """
        获取section下所有可用options
        """

        keys = self.config.options(title)
        return keys


# if __name__ == '__main__':
#     from common import setting
#
#     conf_path = setting.CONFIG_INI
#     print(Config(conf_path).apihost_43_13)
