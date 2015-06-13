# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Bitacora\login.ui'
#
# Created: Fri Apr 24 03:00:38 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_loginDialog(object):
    def setupUi(self, loginDialog):
        loginDialog.setObjectName(_fromUtf8("loginDialog"))
        loginDialog.resize(320, 240)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginDialog.sizePolicy().hasHeightForWidth())
        loginDialog.setSizePolicy(sizePolicy)
        loginDialog.setMaximumSize(QtCore.QSize(320, 240))
        loginDialog.setStyleSheet(_fromUtf8(""))
        self.verticalLayout = QtGui.QVBoxLayout(loginDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.logoLabel = QtGui.QLabel(loginDialog)
        self.logoLabel.setText(_fromUtf8(""))
        self.logoLabel.setObjectName(_fromUtf8("logoLabel"))
        self.horizontalLayout.addWidget(self.logoLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(loginDialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(loginDialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.userName = QtGui.QLineEdit(loginDialog)
        self.userName.setObjectName(_fromUtf8("userName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.userName)
        self.passWord = QtGui.QLineEdit(loginDialog)
        self.passWord.setEchoMode(QtGui.QLineEdit.Password)
        self.passWord.setObjectName(_fromUtf8("passWord"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.passWord)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.exitButton = QtGui.QPushButton(loginDialog)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.horizontalLayout_2.addWidget(self.exitButton)
        self.recoveryButton = QtGui.QPushButton(loginDialog)
        self.recoveryButton.setObjectName(_fromUtf8("recoveryButton"))
        self.horizontalLayout_2.addWidget(self.recoveryButton)
        self.loginButton = QtGui.QPushButton(loginDialog)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.horizontalLayout_2.addWidget(self.loginButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(loginDialog)
        QtCore.QMetaObject.connectSlotsByName(loginDialog)
        loginDialog.setTabOrder(self.userName, self.passWord)
        loginDialog.setTabOrder(self.passWord, self.loginButton)
        loginDialog.setTabOrder(self.loginButton, self.recoveryButton)
        loginDialog.setTabOrder(self.recoveryButton, self.exitButton)

    def retranslateUi(self, loginDialog):
        loginDialog.setWindowTitle(_translate("loginDialog", "Ingreso", None))
        self.label.setText(_translate("loginDialog", "Usuario:", None))
        self.label_2.setText(_translate("loginDialog", "Contraseña:", None))
        self.exitButton.setText(_translate("loginDialog", "Salir", None))
        self.recoveryButton.setText(_translate("loginDialog", "Recuperar Contraseña", None))
        self.loginButton.setText(_translate("loginDialog", "Ingresar", None))

