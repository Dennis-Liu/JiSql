# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewConnDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(520, 284)
        self.pushButton_test = QtWidgets.QPushButton(Dialog)
        self.pushButton_test.setGeometry(QtCore.QRect(238, 220, 80, 27))
        self.pushButton_test.setObjectName("pushButton_test")
        self.pushButton_save = QtWidgets.QPushButton(Dialog)
        self.pushButton_save.setGeometry(QtCore.QRect(324, 220, 80, 27))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_cancle = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancle.setGeometry(QtCore.QRect(410, 220, 80, 27))
        self.pushButton_cancle.setObjectName("pushButton_cancle")
        self.pushButton_open = QtWidgets.QPushButton(Dialog)
        self.pushButton_open.setGeometry(QtCore.QRect(117, 219, 80, 27))
        self.pushButton_open.setObjectName("pushButton_open")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 451, 194))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_conname = QtWidgets.QLabel(self.layoutWidget)
        self.label_conname.setObjectName("label_conname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_conname)
        self.lineEdit_conname = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_conname.setObjectName("lineEdit_conname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_conname)
        self.label_hostname = QtWidgets.QLabel(self.layoutWidget)
        self.label_hostname.setObjectName("label_hostname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_hostname)
        self.lineEdit_hostname = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_hostname.setObjectName("lineEdit_hostname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_hostname)
        self.label_port = QtWidgets.QLabel(self.layoutWidget)
        self.label_port.setObjectName("label_port")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_port)
        self.lineEdit_port = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_port)
        self.label_username = QtWidgets.QLabel(self.layoutWidget)
        self.label_username.setObjectName("label_username")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_username)
        self.lineEdit_user = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_user)
        self.label_password = QtWidgets.QLabel(self.layoutWidget)
        self.label_password.setObjectName("label_password")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_password)
        self.lineEdit_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_password)
        self.gridLayout.addLayout(self.formLayout, 0, 2, 1, 1)
        self.listWidget_conn = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget_conn.setStyleSheet("")
        self.listWidget_conn.setObjectName("listWidget_conn")
        self.gridLayout.addWidget(self.listWidget_conn, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.pushButton_cancle.clicked.connect(Dialog.reject)
        self.pushButton_save.clicked.connect(Dialog.accept)
        self.listWidget_conn.clicked['QModelIndex'].connect(Dialog.editConn)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "打开链接"))
        self.pushButton_test.setText(_translate("Dialog", "连接测试"))
        self.pushButton_save.setText(_translate("Dialog", "保存"))
        self.pushButton_cancle.setText(_translate("Dialog", "取消"))
        self.pushButton_open.setText(_translate("Dialog", "打开"))
        self.label_conname.setText(_translate("Dialog", "链接名:"))
        self.lineEdit_conname.setPlaceholderText(_translate("Dialog", "本地链接"))
        self.label_hostname.setText(_translate("Dialog", "主机名或者IP:"))
        self.lineEdit_hostname.setPlaceholderText(_translate("Dialog", "127.0.0.1"))
        self.label_port.setText(_translate("Dialog", "端口:"))
        self.lineEdit_port.setPlaceholderText(_translate("Dialog", "3306"))
        self.label_username.setText(_translate("Dialog", "用户名:"))
        self.lineEdit_user.setPlaceholderText(_translate("Dialog", "root"))
        self.label_password.setText(_translate("Dialog", "密码:"))
        self.lineEdit_password.setPlaceholderText(_translate("Dialog", "root"))
