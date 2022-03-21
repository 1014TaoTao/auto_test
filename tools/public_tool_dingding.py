# -*- coding: utf-8 -*-#

# 钉钉发送消息模块
import time
from typing import Any

from dingtalkchatbot.chatbot import DingtalkChatbot, FeedLink

from common import setting, readConfigYaml
from tools.public_tool_allurereport import CaseCount
from tools.public_tool_log import logger

# from common import consts

logger = logger(log_path=setting.API_LOG_PATH)


class DingTalk:

    def __init__(self):

        self.secret = readConfigYaml.Config().get_dingding_secret()
        self.webhook = readConfigYaml.Config().get_dingding_webhook()
        self.ding_news = DingtalkChatbot(webhook=self.webhook, secret=self.secret, pc_slide=False, fail_notice=False)

        self.allureData = CaseCount()
        self.PASS = self.allureData.passCount()
        self.FAILED = self.allureData.failedCount()
        self.BROKEN = self.allureData.brokenCount()
        self.SKIP = self.allureData.skippedCount()
        self.TOTAL = self.allureData.totalCount()
        self.RATE = self.allureData.passRate()

    def send_text(self, msg: str, mobiles=None) -> None:
        """
        发送文本信息
        :param msg: 文本内容
        :param mobiles: 艾特用户电话
        :return:
        """
        if not mobiles:
            self.ding_news.send_text(msg=msg, is_at_all=True)
        else:
            if isinstance(mobiles, list):
                self.ding_news.send_text(msg=msg, at_mobiles=mobiles)
            else:
                raise TypeError("mobiles类型错误 不是list类型.")

    def send_link(self, title: str, text: str, message_url: str, pic_url: str) -> None:
        """
        发送link通知
        :return:
        """
        try:
            self.ding_news.send_link(title=title, text=text, message_url=message_url, pic_url=pic_url)
        except Exception:
            raise

    def send_markdown(self, title: str, msg: str, mobiles=None) -> None:
        """
        :param mobiles:
        :param title:
        :param msg:
        markdown 格式
        """

        if mobiles is None:
            self.ding_news.send_markdown(title=title, text=msg, is_at_all=True)
        else:
            if isinstance(mobiles, list):
                self.ding_news.send_markdown(title=title, text=msg, at_mobiles=mobiles)
            else:
                raise TypeError("mobiles类型错误 不是list类型.")

    @staticmethod
    def feed_link(title: str, message_url: str, pic_url: str) -> Any:

        return FeedLink(title=title, message_url=message_url, pic_url=pic_url)

    def send_feed_link(self, *arg) -> None:
        try:
            self.ding_news.send_feed_card(list(arg))
        except Exception:
            raise

    # 发送钉钉消息
    def send_dingding(self, ENVIRONMENT, TESTER):
        """
        发送钉钉通知
        :return:
        """

        jenkins_url = "http://250.25.250.250:9000/"
        reprot_url = r"http://localhost:63342/pytest_auto_uitest_apitest/report/api_report/allure_report/index.html"

        self.ding_news.send_markdown(
            title='**【接口测试报告】**',
            text="<font color=\'#FFA500\'>[通知] </font>API平台接口自动化...执行完成 \n\n --- \n\n" +
                 "项目名称：**api接口数据报告** \n\n " +
                 "执行环境：<font color=\"#1d953f\">%s</font>" % ENVIRONMENT + "\n\n" +
                 "运行总数：<font color=\"#d71345\">%s 个</font>" % self.TOTAL + "\n\n" +
                 "通过数量：<font color=\"#1d953f\">%s 个</font>" % self.PASS + "\n\n" +
                 "异常数量：<font color=\"#fdb933\">%s 个</font>" % self.BROKEN + "\n\n" +
                 "跳过数量：<font color=\"#2585a6\">%s 个</font>" % self.SKIP + "\n\n" +
                 "失败数量：<font color=\"#c63c26\">%s 个</font>" % self.FAILED + "\n\n" +
                 "成功率为：<font color=\"#1d953f\">%s </font>" % self.RATE + "\n\n" +
                 "执行人员：<font color=\"#130c0e\">@%s</font>" % TESTER + "\n\n --- \n\n" +
                 "报告详情：[点击查看](%s)" % reprot_url + "\n\n" +
                 "构建地址：[点击查看，暂未开通](%s)" % jenkins_url + "\n\n" +
                 "</font> \n\n --- \n\n  **运行时间：** <font color=\"#464547\">%s</font>" % time.strftime("%Y-%m-%d %H:%M:%S"),
            at_dingtalk_ids=[15382112620]
        )


# if __name__ == "__main__":
#     # 发送钉钉推送消息
#     ding = DingTalk()
#     ding.send_dingding()
