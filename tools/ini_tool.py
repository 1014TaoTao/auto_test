# -*- coding: utf-8 -*-

import os
from configparser import ConfigParser


class Config:
    def __init__(self, conf_path):
        """初始化配置类"""
        self.conf_path = conf_path
        self.config = ConfigParser()
        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保Config.ini配置文件存在！")
        self.config.read(self.conf_path, encoding='utf-8')

    def get_config(self, section: str, option: str) -> str:
        """读取配置文件中的值"""
        try:
            return self.config.get(section, option)
        except (ConfigParser.NoSectionError, ConfigParser.NoOptionError) as e:
            print(f"配置文件读取错误: {e}")
            return None

    def set_config(self, section: str, option: str, value: str) -> bool:
        """修改配置文件中的值"""
        try:
            self.config.set(section, option, value)
            with open(self.conf_path, "w", encoding='utf-8') as f:
                self.config.write(f)
            return True
        except (ConfigParser.NoSectionError, ConfigParser.NoOptionError) as e:
            print(f"配置文件修改错误: {e}")
            return False

    def add_section(self, section: str) -> bool:
        """添加新的section到配置文件"""
        if not self.config.has_section(section):
            self.config.add_section(section)
            with open(self.conf_path, "w", encoding='utf-8') as f:
                self.config.write(f)
            return True
        return False

    def get_section(self, section: str) -> dict:
        """获取指定section的所有配置项"""
        try:
            return dict(self.config.items(section))
        except ConfigParser.NoSectionError as e:
            print(f"配置文件读取错误: {e}")
            return {}

    def get_all_sections(self) -> list:
        """获取所有section"""
        return self.config.sections()

