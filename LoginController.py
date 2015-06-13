#!/usr/bin/env/python
# -*- coding: utf-8 -*-

from LoginView import Ui_loginDialog
from ParseHandler import ParseHandler

import sys

from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QPixmap
from PyQt4.QtGui import QInputDialog
from PyQt4.QtCore import SIGNAL

class LoginController(QDialog):

    #Define images inside img folder
    LOGO = "logo.png"
    BACKGROUND = "login_back.png"

    """
    Assign labels according to language, by the default
    the View was setup in Spanish
    """
    
    #Labels
    USER = "Username"
    PWD = "Password"

    #Buttons
    EXIT = "Exit"
    RECOVER = "Recover Password"
    LOGIN = "Login"

    #Error Message
    ERROR_MSG = u'Incorrect username & password'

    #Recover Password
    RECOVER_TITLE = "Password Recovery"
    RECOVER_MSG = "Please type your username"
    CONFIRM_TITLE = "Please check your Email"
    CONFIRM_MSG = "An email has been sent to: "
    

    def __init__(self):
        super(LoginController, self).__init__()
        self.loginUI = Ui_loginDialog()
        self.loginUI.setupUi(self)        
        self.setupLanguage()
        self.setupDialogUi()


    def setupLanguage(self):
        self.loginUI.label.setText(self.USER)
        self.loginUI.label_2.setText(self.PWD)
        self.loginUI.exitButton.setText(self.EXIT)
        self.loginUI.recoveryButton.setText(self.RECOVER)
        self.loginUI.loginButton.setText(self.LOGIN)
        
        
    def setupDialogUi(self):
        pixmap = QPixmap("img/" + self.LOGO)
        self.loginUI.logoLabel.setPixmap(pixmap)
        self.setStyleSheet("background-image: url(img/"+ self.BACKGROUND +"); background-repeat:no-repeat;background-position:center;")
        self.connect(self.loginUI.loginButton, SIGNAL('clicked()'), self.loginHandler)
        self.connect(self.loginUI.exitButton, SIGNAL('clicked()'), self.rejected)
        self.connect(self.loginUI.recoveryButton, SIGNAL('clicked()'), self.recoverPwd)        
      

    def loginHandler(self):
        self.currentHandler = ParseHandler(self.loginUI.userName.text(), self.loginUI.passWord.text())
        self.usr = self.currentHandler.usr
        if self.currentHandler.checkLogin():
            self.accept()

        else:
            QMessageBox.critical(self, "Error", self.ERROR_MSG)


    def rejected(self):
       self.close()

    def recoverPwd(self):
        text, ok = QInputDialog.getText(self,
                                      self.RECOVER_TITLE,
                                      self.RECOVER_MSG)
        if ok:
             self.currentHandler = ParseHandler(text)
             self.currentHandler.passwordReset()             
             QMessageBox.information(self, self.CONFIRM_TITLE,
                                     self.CONFIRM_MSG + text)
            


def main():
    app = QApplication(sys.argv)
    new_dialog = LoginController()
    new_dialog.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

