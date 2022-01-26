# coding:utf-8
import yaml

from common import setting


class Config:
    def __init__(self):
        self.config_yaml = setting.CONFIG_YAML
        # 读取yaml内容
        with open(self.config_yaml, 'rb') as f:
            self.data = yaml.safe_load(f)

    # 获取所有数据
    def all_data(self):
        all_data_dict = self.data
        return all_data_dict

    def get_email_info(self):
        email_info = self.data['email']
        return email_info

    def get_databases_info(self):
        databases_info = self.data['databases']
        return databases_info

    # 获取环境名称
    def get_environment(self):
        environment_list = []
        environment = self.data['environment']
        for k, v in environment.items():
            environment_list.append(k)
        return environment_list

    # 获取环境下所有信息
    def get_environment_info(self):
        environment = self.data['environment']
        return environment

    # 获取apihost
    def get_apihoet(self, environment_name):
        api_host = self.get_environment_info()[environment_name]['apihost']
        return api_host

    # 获取basehost
    def get_basehost(self, environment_name):
        base_host = self.get_environment_info()[environment_name]['basehost']
        return base_host

    # 获取登录地址
    def get_loginHost(self, environment_name):
        login_host = self.get_environment_info()[environment_name]['loginHost']
        return login_host

    # 获取登录入参
    def get_login_info(self, environment_name):
        login_info = self.get_environment_info()[environment_name]['loginInfo']
        return login_info

    # 获取登录入参
    def get_login_username(self, environment_name):
        login_username = self.get_environment_info()[environment_name]['username']
        return login_username

    # 是否删除旧的测试数据
    def get_delete_report_on_off(self):
        delete_report_on_off = self.data['delete_report_on_off']
        return delete_report_on_off

    # 是否生成测试报告
    def get_run_report_on_off(self):
        run_report_on_off = self.data['run_report_on_off']
        return run_report_on_off

    # 是否压缩测试报告
    def get_zip__report_on_off(self):
        zip__report_on_off = self.data['zip__report_on_off']
        return zip__report_on_off

    # 是否发送邮件
    def get_send_email_on_off(self):
        send_email_on_off = self.data['send_email_on_off']
        return send_email_on_off

    # 是否结束测试自动打开测试报告html
    def get_open_report_on_off(self):
        open_report_on_off = self.data['open_report_on_off']
        return open_report_on_off

    # 是否开启控制台输出日志
    def get_log_control_on_off(self):
        log_control_on_off = self.data['log_control_on_off']
        return log_control_on_off

    # 是否开启数据库
    def get_databases_on_off(self):
        get_databases_on_off = self.data['get_databases_on_off']
        return get_databases_on_off

    # 获取执行测试人员信息
    def get_testers(self):
        testers = self.data['testers']
        return testers

    # 钉钉
    def get_send_dingding_news_on_off(self):
        send_dingding_news_on_off = self.data['send_dingding_news_on_off']
        return send_dingding_news_on_off

    # 钉钉secret
    def get_dingding_secret(self):
        dingding_secre = self.data['dingding']['secret']
        return dingding_secre

    # 钉钉secret
    def get_dingding_webhook(self):
        dingding_webhook = self.data['dingding']['webhook']
        return dingding_webhook

# 测试
# if __name__ == '__main__':
#     from common import setting
#
#     C = Config()

# 如果要切换环境，只需要修改索引下标值['environment_195', 'environment_115', 'environment_122', 'environment_34_13']
# ENVIRONMENT = C.get_environment()[1]
# print(ENVIRONMENT)
# all_ENVIRONMENT = C.get_apihoet(ENVIRONMENT)
# print(all_ENVIRONMENT)
# print(C.get_dingding_webhook())
