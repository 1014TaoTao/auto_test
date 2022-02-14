# -*- coding: utf-8 -*-#

# 钉钉发送消息模块
import time

from dingtalkchatbot.chatbot import DingtalkChatbot

from common import consts
from common import setting, readConfigYaml
from tools.public_tool_log import logger

logger = logger(log_path=setting.API_LOG_PATH)


class DingTalk:

    # 发送钉钉消息
    def send_dingding(self):
        """
        :return:
        """
        # 获取当前日期
        tile = time.strftime("%Y-%m-%d %H:%M:%S")

        secret = readConfigYaml.Config().get_dingding_secret()
        webhook = readConfigYaml.Config().get_dingding_webhook()
        ding_news = DingtalkChatbot(webhook=webhook, secret=secret, pc_slide=False, fail_notice=False)
        d = {}  # 先声明，后边用哪了自己看
        file = setting.PROMETHEUSDATA
        with open(file, "r") as file:  # 打卡刚说的监控数据文件
            for lines in file:  # 遍历他的值
                launch_name = lines.strip('\n').split(' ')[0]  # 他是个文本肯定有换行符用strip干掉他，干掉后用split根据空格进行切割，取第一个值
                num = lines.strip('\n').split(' ')[1]  # 这个就取第二个值
                d.update({launch_name: num})  # 现在把娶到的俩值以词典的方式给到d
            retries_run = d.get('launch_retries_run')  # 之后通过key把他们统计的值拿出来，这行是运行总数
            status_passed = d.get('launch_status_passed')  # 这行是通过数
            status_failed = d.get('launch_status_failed')  # 这行是失败数
            status_skipped = d.get('launch_status_skipped')  # 这行是跳过数
            status_broken = d.get('launch_status_broken')  # 异常数量
        jenkins_url = "http://250.25.250.250:9000/"
        report_url = r"http://localhost:63342/pytest_auto_uitest_apitest/report/api_report/allure_report/index.html?_ijt=vhdrkjvgm0pd5tspa77fg7a987"  # 拼接allure报告地址

        ding_news.send_markdown(
            title='接口测试报告',
            text="<font color=\'#FFA500\'>[通知] </font>API平台接口自动化...执行完成 \n\n --- \n\n" +
                 "项目名称：api接口数据报告 \n\n " +
                 "报告地址：[点击查看](%s)" % report_url + "\n\n" +
                 "构建地址：[点击查看](%s)" % jenkins_url + "\n\n" +
                 "执行环境：%s" % consts.ENVIRONMENT + "\n\n" +
                 "运行总数：%s" % retries_run + "\n\n" +
                 "通过数量：%s" % status_passed + "\n\n" +
                 "异常数量：%s" % status_broken + "\n\n" +
                 "跳过数量：%s" % status_skipped + "\n\n" +
                 "失败数量：%s" % status_failed + "\n\n" +
                 "执行人员：@%s" % consts.TESTER + "\n\n" +
                 "</font> \n\n --- \n\n  **运行时间：** %s" % tile,
            at_dingtalk_ids=[15382112620]
        )

# if __name__ == "__main__":
#     # 发送钉钉推送消息
#     ding = DingTalk()
#     ding.send_dingding()
