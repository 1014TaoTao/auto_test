# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'api_auto_test_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ApiAutoTool(object):
    def setupUi(self, ApiAutoTool):
        ApiAutoTool.setObjectName("ApiAutoTool")
        ApiAutoTool.resize(1080, 842)
        ApiAutoTool.setMinimumSize(QtCore.QSize(640, 520))
        ApiAutoTool.setSizeIncrement(QtCore.QSize(640, 520))
        ApiAutoTool.setBaseSize(QtCore.QSize(640, 520))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ico/win.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.testCasePathBox.addItem("")
        self.testCasePathBox.addItem("")
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
        self.deleteReportBox.addItem("")
        self.deleteReportBox.addItem("")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.deleteReportBox)
        self.gridLayout.addLayout(self.formLayout_5, 0, 0, 1, 1)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.saverepor_txt = QtWidgets.QLabel(self.centralwidget)
        self.saverepor_txt.setObjectName("saverepor_txt")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.saverepor_txt)
        self.reportRunBox = QtWidgets.QComboBox(self.centralwidget)
        self.reportRunBox.setObjectName("reportRunBox")
        self.reportRunBox.addItem("")
        self.reportRunBox.addItem("")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.reportRunBox)
        self.gridLayout.addLayout(self.formLayout_3, 0, 1, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.send_email_txt = QtWidgets.QLabel(self.centralwidget)
        self.send_email_txt.setObjectName("send_email_txt")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.send_email_txt)
        self.sendEmailBox = QtWidgets.QComboBox(self.centralwidget)
        self.sendEmailBox.setObjectName("sendEmailBox")
        self.sendEmailBox.addItem("")
        self.sendEmailBox.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sendEmailBox)
        self.gridLayout.addLayout(self.formLayout_2, 0, 2, 1, 1)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.opneNewReportBox = QtWidgets.QComboBox(self.centralwidget)
        self.opneNewReportBox.setStyleSheet("")
        self.opneNewReportBox.setObjectName("opneNewReportBox")
        self.opneNewReportBox.addItem("")
        self.opneNewReportBox.addItem("")
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
        self.testerBox.addItem("")
        self.testerBox.addItem("")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.testerBox)
        self.gridLayout.addLayout(self.formLayout_7, 1, 1, 1, 1)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.send_dingding_txt = QtWidgets.QLabel(self.centralwidget)
        self.send_dingding_txt.setObjectName("send_dingding_txt")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.send_dingding_txt)
        self.sendDingDingBox = QtWidgets.QComboBox(self.centralwidget)
        self.sendDingDingBox.setObjectName("sendDingDingBox")
        self.sendDingDingBox.addItem("")
        self.sendDingDingBox.addItem("")
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
        self.emvironment_lisBox = QtWidgets.QComboBox(self.centralwidget)
        self.emvironment_lisBox.setObjectName("emvironment_lisBox")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.emvironment_lisBox)
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
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.loginButton.setObjectName("loginButton")
        self.horizontalLayout_2.addWidget(self.loginButton)
        self.testRunButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testRunButton.sizePolicy().hasHeightForWidth())
        self.testRunButton.setSizePolicy(sizePolicy)
        self.testRunButton.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.testRunButton.setObjectName("testRunButton")
        self.horizontalLayout_2.addWidget(self.testRunButton)
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
        self.resultLogEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.resultLogEdit.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 0, 0);")
        self.resultLogEdit.setObjectName("resultLogEdit")
        self.horizontalLayout_3.addWidget(self.resultLogEdit)
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
        self.resetButton.clicked.connect(self.testCasePathBox.clear)
        self.resetButton.clicked.connect(self.deleteReportBox.clear)
        self.resetButton.clicked.connect(self.reportRunBox.clear)
        self.resetButton.clicked.connect(self.sendEmailBox.clear)
        self.resetButton.clicked.connect(self.resultLogEdit.clear)
        self.resetButton.clicked.connect(self.opneNewReportBox.clear)
        self.resetButton.clicked.connect(self.testerBox.clear)
        self.resetButton.clicked.connect(self.sendDingDingBox.clear)
        self.seeReportButton.clicked.connect(ApiAutoTool.close)
        self.runButton.clicked.connect(ApiAutoTool.close)
        QtCore.QMetaObject.connectSlotsByName(ApiAutoTool)

    def retranslateUi(self, ApiAutoTool):
        _translate = QtCore.QCoreApplication.translate
        ApiAutoTool.setWindowTitle(_translate("ApiAutoTool", "接口自动化测试工具"))
        self.selectEnvTitle.setText(_translate("ApiAutoTool", "请先选择执行环境"))
        self.testcase_txt.setText(_translate("ApiAutoTool", "执行的文件:"))
        self.testCasePathBox.setItemText(0, _translate("ApiAutoTool", "1"))
        self.testCasePathBox.setItemText(1, _translate("ApiAutoTool", "2"))
        self.deletereport_txt.setText(_translate("ApiAutoTool", "删除旧报告:"))
        self.deleteReportBox.setItemText(0, _translate("ApiAutoTool", "1"))
        self.deleteReportBox.setItemText(1, _translate("ApiAutoTool", "2"))
        self.saverepor_txt.setText(_translate("ApiAutoTool", "生成报告:"))
        self.reportRunBox.setItemText(0, _translate("ApiAutoTool", "2"))
        self.reportRunBox.setItemText(1, _translate("ApiAutoTool", "1"))
        self.send_email_txt.setText(_translate("ApiAutoTool", "发送邮件:"))
        self.sendEmailBox.setItemText(0, _translate("ApiAutoTool", "1"))
        self.sendEmailBox.setItemText(1, _translate("ApiAutoTool", "2"))
        self.opneNewReportBox.setItemText(0, _translate("ApiAutoTool", "1"))
        self.opneNewReportBox.setItemText(1, _translate("ApiAutoTool", "2"))
        self.open_report_txt.setText(_translate("ApiAutoTool", "打开新报告:"))
        self.tester_txt.setText(_translate("ApiAutoTool", "测试人员:"))
        self.testerBox.setItemText(0, _translate("ApiAutoTool", "1"))
        self.testerBox.setItemText(1, _translate("ApiAutoTool", "2"))
        self.send_dingding_txt.setText(_translate("ApiAutoTool", "发送钉钉:"))
        self.sendDingDingBox.setItemText(0, _translate("ApiAutoTool", "1"))
        self.sendDingDingBox.setItemText(1, _translate("ApiAutoTool", "2"))
        self.emvironmenttxt.setText(_translate("ApiAutoTool", "测试环境"))
        self.loginTitletxt.setText(_translate("ApiAutoTool", "账号选择"))
        self.loginButton.setText(_translate("ApiAutoTool", "登录"))
        self.testRunButton.setText(_translate("ApiAutoTool", "调试"))
        self.runButton.setText(_translate("ApiAutoTool", "运行"))
        self.seeReportButton.setText(_translate("ApiAutoTool", "查看报告"))
        self.resetButton.setText(_translate("ApiAutoTool", "重置执行"))
