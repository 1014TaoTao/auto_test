# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'api_auto_test_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import logging

from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPlainTextEdit

from common import setting
from common.readConfigYaml import Config
from tools import public_tool_project_check
from tools.api_tool_open_html import OpenHtml
from tools.api_tool_read_pyqt_txt import PyqtTxtPack
from tools.api_tool_run_all import API_Run
from tools.public_tool_log import logger

# 执行全部测试流程
logger = logger(setting.API_LOG_PATH)


# 重定向
class Handler(QtCore.QObject, logging.Handler):
    new_record = QtCore.pyqtSignal(object)

    def emit(self, record):
        self.setFormatter(
            logging.Formatter(u'[时间]:%(asctime)s-[级别]:%(levelname)s-[文件]:%(filename)s-[信息]:%(message)s')
        )
        msg = self.format(record)
        self.new_record.emit(msg)


class UiApiAutoTool(object):
    def __init__(self):
        self.delete_old_report_on_off_list = Config().get_delete_report_on_off()
        self.save_report_on_off_list = Config().get_run_report_on_off()
        self.open_report_on_off_list = Config().get_open_report_on_off()
        self.email_on_off_list = Config().get_send_email_on_off()
        self.dingding_on_off_list = Config().get_send_dingding_news_on_off()
        self.tester_list = Config().get_testers()
        self.test_case_list = setting.TEST_CASE_LIST
        self.emvironment_list = Config().get_environment()

    def setupUi(self, ApiAutoTool):

        ApiAutoTool.setObjectName("ApiAutoTool")
        ApiAutoTool.resize(640, 580)
        ApiAutoTool.setMinimumSize(QtCore.QSize(640, 520))
        ApiAutoTool.setSizeIncrement(QtCore.QSize(640, 520))
        ApiAutoTool.setBaseSize(QtCore.QSize(640, 520))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/ico/win.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ApiAutoTool.setWindowIcon(icon)
        ApiAutoTool.setStyleSheet("font: 12pt \"微软雅黑\";")

        self.centralwidget = QtWidgets.QWidget(ApiAutoTool)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.selectEnvTitle = QtWidgets.QLabel(self.centralwidget)
        self.selectEnvTitle.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.selectEnvTitle.setObjectName("selectEnvTitle")
        self.horizontalLayout_6.addWidget(self.selectEnvTitle, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.testcase_txt = QtWidgets.QLabel(self.centralwidget)
        self.testcase_txt.setObjectName("testcase_txt")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.testcase_txt)
        self.testCasePathBox = QtWidgets.QComboBox(self.centralwidget)
        self.testCasePathBox.setObjectName("testCasePathBox")
        self.testCasePathBox.addItems(self.test_case_list)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.testCasePathBox)
        self.verticalLayout.addLayout(self.formLayout)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.deletereport_txt = QtWidgets.QLabel(self.centralwidget)
        self.deletereport_txt.setObjectName("deletereport_txt")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.deletereport_txt)
        self.deleteReportBox = QtWidgets.QComboBox(self.centralwidget)
        self.deleteReportBox.setObjectName("deleteReportBox")
        self.deleteReportBox.addItems(self.delete_old_report_on_off_list)

        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.deleteReportBox)
        self.gridLayout.addLayout(self.formLayout_5, 0, 0, 1, 1)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.saverepor_txt = QtWidgets.QLabel(self.centralwidget)
        self.saverepor_txt.setObjectName("saverepor_txt")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.saverepor_txt)
        self.reportRunBox = QtWidgets.QComboBox(self.centralwidget)
        self.reportRunBox.setObjectName("reportRunBox")
        self.reportRunBox.addItems(self.save_report_on_off_list)

        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.reportRunBox)
        self.gridLayout.addLayout(self.formLayout_3, 0, 1, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.send_email_txt = QtWidgets.QLabel(self.centralwidget)
        self.send_email_txt.setObjectName("send_email_txt")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.send_email_txt)
        self.sendEmailBox = QtWidgets.QComboBox(self.centralwidget)
        self.sendEmailBox.setObjectName("endEmailBox")
        self.sendEmailBox.addItems(self.email_on_off_list)

        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sendEmailBox)
        self.gridLayout.addLayout(self.formLayout_2, 0, 2, 1, 1)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.opneNewReportBox = QtWidgets.QComboBox(self.centralwidget)
        self.opneNewReportBox.setObjectName("opneNewReportBox")
        self.opneNewReportBox.addItems(self.open_report_on_off_list)

        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.opneNewReportBox)
        self.open_report_txt = QtWidgets.QLabel(self.centralwidget)
        self.open_report_txt.setObjectName("open_report_txt")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.open_report_txt)
        self.gridLayout.addLayout(self.formLayout_6, 1, 0, 1, 1)
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setObjectName("formLayout_7")
        self.tester_txt = QtWidgets.QLabel(self.centralwidget)
        self.tester_txt.setObjectName("tester_txt")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.tester_txt)
        self.testerBox = QtWidgets.QComboBox(self.centralwidget)
        self.testerBox.setObjectName("testerBox")
        self.testerBox.addItems(self.tester_list)

        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.testerBox)
        self.gridLayout.addLayout(self.formLayout_7, 1, 1, 1, 1)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.send_dingding_txt = QtWidgets.QLabel(self.centralwidget)
        self.send_dingding_txt.setObjectName("send_dingding_txt")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.send_dingding_txt)
        self.sendDingDingBox = QtWidgets.QComboBox(self.centralwidget)
        self.sendDingDingBox.setObjectName("sendDingDingBox")
        self.sendDingDingBox.addItems(self.dingding_on_off_list)
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sendDingDingBox)
        self.gridLayout.addLayout(self.formLayout_4, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setObjectName("formLayout_8")
        self.emvironmenttxt = QtWidgets.QLabel(self.centralwidget)
        self.emvironmenttxt.setObjectName("emvironmenttxt")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.emvironmenttxt)
        self.emvironment_listBox = QtWidgets.QComboBox(self.centralwidget)
        self.emvironment_listBox.setObjectName("emvironment_listBox")
        self.emvironment_listBox.addItems(self.emvironment_list)
        self.emvironment_listBox.currentTextChanged.connect(lambda: self.updateLoginTitleBox_info())
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.emvironment_listBox)
        self.horizontalLayout_7.addLayout(self.formLayout_8)

        self.formLayout_9 = QtWidgets.QFormLayout()
        self.formLayout_9.setObjectName("formLayout_9")
        self.loginTitletxt = QtWidgets.QLabel(self.centralwidget)
        self.loginTitletxt.setObjectName("loginTitletxt")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.loginTitletxt)
        self.loginTitleBox = QtWidgets.QComboBox(self.centralwidget)
        self.loginTitleBox.setObjectName("loginTitleBox")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.loginTitleBox)
        self.horizontalLayout_7.addLayout(self.formLayout_9)

        self.formLayout_10 = QtWidgets.QFormLayout()
        self.formLayout_10.setObjectName("formLayout_10")
        self.portTitletxt = QtWidgets.QLabel(self.centralwidget)
        self.portTitletxt.setObjectName("portTitletxt")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.portTitletxt)
        self.portTitleBox = QtWidgets.QComboBox(self.centralwidget)
        self.portTitleBox.setObjectName("portTitleBox")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.portTitleBox)
        self.horizontalLayout_7.addLayout(self.formLayout_10)
        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_5.addWidget(self.line)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # 获取token
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.loginButton.setObjectName("loginButton")
        self.horizontalLayout_2.addWidget(self.loginButton)
        # 调试
        self.testRunButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testRunButton.sizePolicy().hasHeightForWidth())
        self.testRunButton.setSizePolicy(sizePolicy)
        self.testRunButton.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.testRunButton.setObjectName("testRunButton")
        self.horizontalLayout_2.addWidget(self.testRunButton)
        # 运行
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runButton.sizePolicy().hasHeightForWidth())
        self.runButton.setSizePolicy(sizePolicy)
        self.runButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.runButton.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.runButton.setObjectName("runButton")
        self.horizontalLayout_2.addWidget(self.runButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.resultLogEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.resultLogEdit.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 0, 0);")
        self.resultLogEdit.setObjectName("resultLogEdit")
        # 不换行
        self.resultLogEdit.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.resultLogEdit.setReadOnly(True)
        self.horizontalLayout_3.addWidget(self.resultLogEdit)
        # 实时显示输出, 将控制台的输出重定向到界面中
        handler = Handler()
        logging.getLogger().addHandler(handler)
        handler.new_record.connect(self.resultLogEdit.appendPlainText)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_4.addWidget(self.line_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.seeReportButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seeReportButton.sizePolicy().hasHeightForWidth())
        self.seeReportButton.setSizePolicy(sizePolicy)
        self.seeReportButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.seeReportButton.setObjectName("seeReportButton")
        self.horizontalLayout.addWidget(self.seeReportButton)
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
        self.resetButton.setSizePolicy(sizePolicy)
        self.resetButton.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout.addWidget(self.resetButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        ApiAutoTool.setCentralWidget(self.centralwidget)
        self.retranslateUi(ApiAutoTool)
        self.loginButton.clicked.connect(lambda: self.longin_get_token())
        self.testRunButton.clicked.connect(lambda: self.testRunButton_info())
        self.runButton.clicked.connect(lambda: self.runButton_info())
        self.seeReportButton.clicked.connect(lambda: OpenHtml().see_html())
        self.resetButton.clicked.connect(self.resultLogEdit.clear)

        QtCore.QMetaObject.connectSlotsByName(ApiAutoTool)

    def retranslateUi(self, ApiAutoTool):
        _translate = QtCore.QCoreApplication.translate
        ApiAutoTool.setWindowTitle(_translate("ApiAutoTool", "接口自动化测试工具"))
        self.testCasePathBox.setCurrentIndex(0)  # 设定默认值:demo01
        self.testerBox.setCurrentIndex(0)  # 设定默认值:张涛
        self.reportRunBox.setCurrentIndex(1)  # 设定默认值:默认不生成测试报告
        self.deleteReportBox.setCurrentIndex(1)  # 设定默认值:默认不删除旧报告
        self.sendEmailBox.setCurrentIndex(1)  # 设定默认值:默认不发送邮件
        self.opneNewReportBox.setCurrentIndex(1)  # 设定默认值:默认不打开测试报告
        self.sendDingDingBox.setCurrentIndex(1)  # 设定默认值:默认不发送消息
        self.emvironment_listBox.setCurrentIndex(1)  # 默认115环境
        self.portTitleBox.setCurrentIndex(7)  # 默认115环境
        # self.resultLogEdit.setPlainText(str(res)) # 只读日志

        self.selectEnvTitle.setText(_translate("ApiAutoTool", "请先选择执行环境"))
        self.testcase_txt.setText(_translate("ApiAutoTool", "执行的文件:"))
        self.deletereport_txt.setText(_translate("ApiAutoTool", "删除旧报告:"))
        self.saverepor_txt.setText(_translate("ApiAutoTool", "生成报告:"))
        self.send_email_txt.setText(_translate("ApiAutoTool", "发送邮件:"))
        self.open_report_txt.setText(_translate("ApiAutoTool", "打开新报告:"))
        self.tester_txt.setText(_translate("ApiAutoTool", "测试人员:"))
        self.send_dingding_txt.setText(_translate("ApiAutoTool", "发送钉钉:"))
        self.emvironmenttxt.setText(_translate("ApiAutoTool", "测试环境"))
        self.loginTitletxt.setText(_translate("ApiAutoTool", "账号选择"))
        self.portTitletxt.setText(_translate("ApiAutoTool", "环境端口"))
        self.loginButton.setText(_translate("ApiAutoTool", "登录"))
        self.testRunButton.setText(_translate("ApiAutoTool", "调试"))
        self.runButton.setText(_translate("ApiAutoTool", "运行"))
        self.seeReportButton.setText(_translate("ApiAutoTool", "查看报告"))
        self.resetButton.setText(_translate("ApiAutoTool", "清除结果"))

    def get_testCasePathBox_info(self):
        """
        :return:
        """
        return self.testCasePathBox.currentText()

    def get_testerBox_info(self):
        """
        :return:
        """
        return self.testerBox.currentText()

    def get_reportRunBox_info(self):
        """
        :return:
        """
        return self.reportRunBox.currentText()

    def get_deleteReportBox_info(self):
        """
        :return:
        """
        return self.deleteReportBox.currentText()

    def get_sendEmailBox_info(self):
        """
        :return:
        """
        return self.sendEmailBox.currentText()

    def get_opneNewReportBox_info(self):
        """
        :return:
        """
        return self.opneNewReportBox.currentText()

    def get_sendDingDingBox_info(self):
        """
        :return:
        """
        return self.sendDingDingBox.currentText()

    def get_emvironmentBox_info(self):
        """
        :return:
        """
        return self.emvironment_listBox.currentText()

    def get_emvironment_port_Box_info(self):
        """
            :return:
            """
        return self.portTitleBox.currentText()

    def get_loginTitleBox_info(self):
        """
        :return:
        """
        return self.loginTitleBox.currentText()

    def updateLoginTitleBox_info(self):
        """
        :return:
        """
        self.loginTitleBox.clear()
        environment_name = self.emvironment_listBox.currentText()
        environment_port = Config().get_environment_port(environment_name)
        login_title = Config().get_login_user_title(environment_name)
        self.portTitleBox.addItems(environment_port)
        self.loginTitleBox.addItems(login_title)

    def testRunButton_info(self):
        """
        :return:
        """
        # 执行文件
        ENVIRONMENT = self.get_emvironmentBox_info()
        LOGINUSER = self.get_loginTitleBox_info()
        TESTCASEPATH = self.get_testCasePathBox_info()
        ENVIRONMENTPORT = self.get_emvironment_port_Box_info()
        APIHOST = Config().get_apihoet(ENVIRONMENT)
        BASEHOST = Config().get_basehost(ENVIRONMENT)
        LOGINHOST = Config().get_loginHost(ENVIRONMENT)
        LOGINDATA = Config().get_login_data(ENVIRONMENT, LOGINUSER)
        USERNAME = Config().get_login_username(ENVIRONMENT, LOGINUSER)


        from tools.api_tool_excel import ExcelPack
        excel = ExcelPack(file_name=TESTCASEPATH, sheet_id=0)
        # 批量执行
        excel.run_excel_case(APIHOST, ENVIRONMENTPORT, BASEHOST, LOGINHOST, LOGINDATA, USERNAME)

    def longin_get_token(self):
        from tools.api_tool_login import Login
        BASEHOST = Config().get_basehost(self.get_emvironmentBox_info())
        LOGINHOST = Config().get_loginHost(self.get_emvironmentBox_info())
        LOGINDATA = Config().get_login_data(self.get_emvironmentBox_info(),
                                            self.get_loginTitleBox_info())
        USERNAME = Config().get_login_username(self.get_emvironmentBox_info(),
                                               self.get_loginTitleBox_info())
        Login(BASEHOST, LOGINHOST, LOGINDATA, USERNAME).api_login()

    def all_info(self):
        """
        :return:
        """
        PyqtTxtPack().clear_pyqt5_txt()
        info_dict = {'testcase_path': self.get_testCasePathBox_info(), 'emvironment': self.get_emvironmentBox_info(),
                     'emvironment_port': self.get_emvironment_port_Box_info(),
                     'login_user': self.get_loginTitleBox_info(),
                     'api_host': Config().get_apihoet(self.get_emvironmentBox_info()),
                     'base_host': Config().get_basehost(self.get_emvironmentBox_info()),
                     'login_host': Config().get_loginHost(self.get_emvironmentBox_info()),
                     'login_usernaem': Config().get_login_username(self.get_emvironmentBox_info(),
                                                                   self.get_loginTitleBox_info()),
                     'login_data': Config().get_login_data(self.get_emvironmentBox_info(),
                                                           self.get_loginTitleBox_info()),
                     'tester': self.get_testerBox_info(), 'delete_report_on_off': self.get_deleteReportBox_info(),
                     'save_report_on_off': self.get_reportRunBox_info(), 'email_on_off': self.get_sendEmailBox_info(),
                     'open_report_on_off': self.get_opneNewReportBox_info(),
                     'send_dingding_on_off': self.get_opneNewReportBox_info()}

        PyqtTxtPack().write_pyqt5_txt(info_dict)

    def runAll_info(self, ENVIRONMENT, TESTER, DELETE_ON_OFF, SAVE_ON_OFF, EMAIL_ON_OFF, OPEN_REPORY_ON_OFF,
                    DINGDING_NEWS_ON_OFF):
        """
            执行前确认pytest.ini文件中testpath的路径
        """
        # =================API测试====================#

        A = API_Run()

        logger.info("""
                              _         _        _           _
              __ _ _ __ (_)  / \\  _   _| |_ __ _| |_ __  ___| |_
             / _` | '_ \\| | / _ \\| | | | |_/ _ \\| |/ _ \\/ __| __|
            | (_| | |_) | |/ ___ \\ |_| | || (_) | |  __/\\__ \\ |_
             \\__,_| .__/|_/_/   \\_\\___/ \\__\\___/ \\_\\___||___/\\__|
                  |_|
                  Starting      ...     ...     ...
                """
                    )

        logger.info('==========< 开始 API自动化项目 测试 >===========')
        # 打印系统和python的版本信息
        public_tool_project_check.api_sys_project(log_path=setting.API_LOG_PATH)
        logger.info(f"【本次执行环境为:{ENVIRONMENT},执行人员：{TESTER}】")

        self.all_info()
        try:
            if DELETE_ON_OFF == 'on':
                # 删除旧的测试结果数据
                A.delete_old_file()
            else:
                logger.info("【DELETE_ON_OFF == off】，不开启删除旧的测试结果数据")
        except Exception as e:
            logger.error(f"判断是否开启删除测试结果数据功能异常：{e}")
        # 执行测试
        A.run_test()
        try:
            if SAVE_ON_OFF == 'on':
                # 生成测试报告
                A.run_allure_report()
            else:
                logger.info("【SAVE_ON_OFF == off】，不开启生成报告功能")
        except Exception as e:
            logger.error(f"判断是否开启生成报告功能异常：{e}")

        # 发送邮件
        try:
            if EMAIL_ON_OFF == 'on':
                # 发送邮件
                A.run_email()
            else:
                logger.info("【EMAIL_ON_OFF == off】，不开启发送邮件功能")
        except Exception as e:
            logger.error(f"判断是否开启发送邮件功能异常：{e}")

        # 打开报告
        try:
            if OPEN_REPORY_ON_OFF == 'on':
                # 打开allure报告
                A.open_report()
            else:
                logger.info("【OPEN_REPORY_ON_OFF == off】，不开启自动打开报告功能")
        except Exception as e:
            logger.error(f"判断是否开启自动打开报告功能异常：{e}")

        # 发送钉钉执行消息
        try:
            if DINGDING_NEWS_ON_OFF == 'on':
                # 发送钉钉消息
                A.send_dingding(ENVIRONMENT, TESTER)
            else:
                logger.info("【DINGDING_NEWS_ON_OFF == off】，不开启发送钉钉消息功能")
        except Exception as e:
            logger.error(f"判断是否开启发送钉钉消息功能异常：{e}")

        logger.info('==========< 结束 API自动化项目 测试 >===========')

    def runButton_info(self):
        """
        :return:
        """
        # 环境信息
        ENVIRONMENT = self.get_emvironmentBox_info()
        # 本次执行人员
        TESTER = self.get_testerBox_info()
        # 是否开启删除历史报告功能,字符串列表转换eval
        DELETE_ON_OFF = self.get_deleteReportBox_info()
        # 是否开启生成报告功能
        SAVE_ON_OFF = self.get_reportRunBox_info()
        # 是否开启发送邮件功能
        EMAIL_ON_OFF = self.get_sendEmailBox_info()
        # 运行结束是否直接打开报告
        OPEN_REPORY_ON_OFF = self.get_opneNewReportBox_info()
        # 发送钉钉
        DINGDING_NEWS_ON_OFF = self.get_sendDingDingBox_info()
        self.runAll_info(ENVIRONMENT, TESTER, DELETE_ON_OFF, SAVE_ON_OFF, EMAIL_ON_OFF, OPEN_REPORY_ON_OFF,
                         DINGDING_NEWS_ON_OFF)
