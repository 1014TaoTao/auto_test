# coding:utf-8
# ==============================
#         邮件类的封装
# ==============================
import smtplib
import time
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from common.readConfigYaml import Config
from tools.allure_tools.public_tool_allurereport import (AllureFileClean,
                                                         CaseCount)
from tools.logs_tools.public_tool_log import logger


class EmailPack:
    # 初始化发件人，密码，收件人列表
    def __init__(self, REPORT_END_PATH, server_host=None, fromaddr=None, password=None, toaddrs=None):
        """
        :param REPORT_END_PATH:
        :param server_host:
        :param fromaddr:
        :param password:
        :param toaddrs:
        """

        if fromaddr is None:
            self.fromaddr = Config().get_email_info().get('sender')
            self.password = Config().get_email_info().get('password')

        else:
            self.fromaddr = fromaddr
            self.password = password

        if toaddrs is None:
            self.toaddrs = Config().get_email_info().get('receiver')
        else:
            self.toaddrs = toaddrs

        if server_host is None:  # 设置邮件服务器默认值
            self.server = smtplib.SMTP(
                Config().get_email_info().get('smtpserver'))
        else:
            self.server = smtplib.SMTP(server_host)
        self.message = MIMEMultipart()  # 邮件体

        self.allureData = CaseCount()
        self.PASS = self.allureData.passCount(REPORT_END_PATH)
        self.FAILED = self.allureData.failedCount(REPORT_END_PATH)
        self.BROKEN = self.allureData.brokenCount(REPORT_END_PATH)
        self.SKIP = self.allureData.skippedCount(REPORT_END_PATH)
        self.TOTAL = self.allureData.totalCount(REPORT_END_PATH)
        self.RATE = self.allureData.passRate(REPORT_END_PATH)
        self.CaseDetail = AllureFileClean().getFailedCasesDetail(REPORT_END_PATH)

    # 设置发件人名称，主题，内容，附件
    def set_message(self, name: str, title: str, content: str, filelist: list):
        """
        :param name:
        :param title:
        :param content:
        :param filelist:
        :return:
        """
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.message['From'] = Header(
            f"{name}<{self.fromaddr}>", 'utf-8')  # 发件人名称和地址
        self.message['Subject'] = Header(title + "_" + tm, 'utf-8')  # 邮件主题
        self.message.attach(MIMEText(content))  # 邮件内容
        if filelist is not None:  # 邮件附件
            for file in filelist:
                fileApart = MIMEApplication(
                    open(file, 'rb').read(), file.split('.')[-1])
                fileApart.add_header(
                    'Content-Disposition', 'attachment', filename=file.split("\\")[-1])
                self.message.attach(fileApart)

    # 发送邮件
    def send_message(self, log_path: str):
        """
        :param log_path:
        :return:
        """
        try:
            self.server.login(self.fromaddr, self.password)
            self.server.sendmail(self.fromaddr, self.toaddrs,
                                 self.message.as_string())
            logger(log_path).info(f'【邮件发送成功！收件人：{self.toaddrs}】')
            self.server.quit()
        except smtplib.SMTPException as e:
            logger(log_path).error(f'【邮件发送异常！{e}】')

    # 默认发送邮件
    def send_default_email(self, log_path: str, file_list: list):
        """
        :rtype: object
        :param file_list: 邮件附件
        :param log_path:
        :return:
        """
        logger(log_path).info("开始==>发送邮件")
        self.set_message(
            name="接口自动化测试",
            title="Hi！测试执行完毕提醒！",
            content=f'''
                各位同事, 大家好:
                自动化用例执行完成，执行结果如下:
                    **********************************
                    用例运行总数: {self.TOTAL} 个
                    通过用例个数: {self.PASS} 个
                    失败用例个数: {self.FAILED} 个
                    异常用例个数: {self.BROKEN} 个
                    跳过用例个数: {self.SKIP} 个
                    成  功   率: {self.RATE} %
                    失败详情信息: {self.CaseDetail}
                    **********************************
                    jenkins地址：https://121.xx.xx.47:8989/login
                    详细情况可登录jenkins平台查看，非相关负责人员可忽略此消息。谢谢。
                    ''',
            filelist=file_list
        )
        self.send_message(log_path)
        logger(log_path).info("完成==>发送邮件")


# 测试
# if __name__ == '__main__':
#     H = EmailPack()
#     from common import setting
#
#     log_path = setting.API_LOG_PATH
#     file_list = setting.API_FILE_LIST
#     H.send_default_email(log_path, file_list)
