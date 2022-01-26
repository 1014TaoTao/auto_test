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
from tools.public_tool_log import logger


class EmailPack:
    # 初始化发件人，密码，收件人列表
    def __init__(self, server_host=None, fromaddr=None, password=None, toaddrs=None):
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
            self.server = smtplib.SMTP(Config().get_email_info().get('smtpserver'))
        else:
            self.server = smtplib.SMTP(server_host)
        self.message = MIMEMultipart()  # 邮件体

    # 设置发件人名称，主题，内容，附件
    def set_message(self, name, title, content, filelist):
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.message['From'] = Header(f"{name}<{self.fromaddr}>", 'utf-8')  # 发件人名称和地址
        self.message['Subject'] = Header(title + "_" + tm, 'utf-8')  # 邮件主题
        self.message.attach(MIMEText(content))  # 邮件内容
        if filelist is not None:  # 邮件附件
            for file in filelist:
                fileApart = MIMEApplication(open(file, 'rb').read(), file.split('.')[-1])
                fileApart.add_header('Content-Disposition', 'attachment', filename=file.split("\\")[-1])
                self.message.attach(fileApart)

    # 发送邮件
    def send_message(self, log_path):
        logger(log_path).info("【开始发送邮件……】")
        try:
            self.server.login(self.fromaddr, self.password)
            self.server.sendmail(self.fromaddr, self.toaddrs, self.message.as_string())
            logger(log_path).info(f'【邮件发送成功！收件人：{self.toaddrs}】')
            self.server.quit()
        except smtplib.SMTPException as e:
            logger(log_path).error(f'【邮件发送异常！{e}】')

    # 默认发送邮件
    def send_default_email(self, log_path, FILE_LIST):
        my_email = EmailPack()
        my_email.set_message(
            name="接口自动化测试",
            title="Hi！测试执行完毕提醒！",
            content='''
                您的自动化测试报告附件已生成，请注意查收！\n
                ''',
            filelist=FILE_LIST
        )
        my_email.send_message(log_path)

# 测试
# if __name__ == '__main__':
#     H = EmailPack()
#     H.send_default_email()
