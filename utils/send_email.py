#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/2/4
# @Author  : Mcen (mmocheng@163.com)
# @Name    : send_email

import time
import smtplib
from functools import reduce
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from base.element_path import Element
from base import consts
import logging
from config.config import Config


class SendMail:

    def __init__(self):
        self.config = Config()


    def get_pass_fail(self):
        time_list = consts.TIMES_LIST
        total = len(time_list)
        time_count = reduce(lambda x, y: x + y, time_list)
        if total:
            ave_time = time_count / len(time_list)
        else:
            ave_time = 0

        success_count = len(consts.RESULT_LIST)
        fail_count = len(time_list) - success_count
        success_rate = float('%.4f' % (success_count / total))
        # 返回用例总数，成功总数，失败总数，成功率，平均时间
        return [total, success_count, fail_count, success_rate, ave_time]

    def send_mail(self):

        file_new = "E:/PycharmProjects/Autotest_API/reports/html/index.html"

        # 定义发送及接收邮箱
        sender = self.config.mail_sender
        receiver = self.config.mail_receiver.split(';')
        subject = '接口自动化测试报告'
        content = "此次一共运行接口个数为 {0} 个，通过个数为 {1} 个，失败个数为 {2} 个，通过率为 {3} %，平均时间为 {4} ms " \
            .format(self.get_pass_fail()[0], self.get_pass_fail()[1], self.get_pass_fail()[2], self.get_pass_fail()[3],
                    self.get_pass_fail()[4])

        # 配置第三方 SMTP 服务，如qq
        smtpserver = self.config.mail_smtpserver
        username = self.config.mail_username
        password = self.config.mail_password

        # 创建一个带附件的实例
        msg = MIMEMultipart('related')
        msg['From'] = formataddr([str(self.config.mail_name), sender])
        # msg['To']=formataddr(["收件人",receiver])
        msg['To'] = ";".join(receiver)

        msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
        msg['Subject'] = Header(subject, 'utf-8')
        msg.attach(MIMEText(content, 'plain', 'utf-8'))

        # 构造附件1，传送report目录下的report.html文件
        att1 = MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # filename为邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="report.html"'
        msg.attach(att1)

        try:
            smtp = smtplib.SMTP_SSL(smtpserver, 465)
            smtp.login(username, password)
            smtp.sendmail(sender, receiver, msg.as_string())
            logging.info('===成功发送邮件===')
        except Exception as e:
            logging.error('===无法发送邮件，请检查==={}'.format(e))
        finally:
            smtp.quit()


if __name__ == '__main__':
    SendMail().send_mail()
