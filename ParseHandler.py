#!/usr/bin/env/python
# -*- coding: utf-8 -*-

from parse_rest.datatypes import Object
from parse_rest.connection import register
from parse_rest.user import User

class ParseHandler():
    APP_ID = "YOUR APP ID"
    REST_API_KEY = "YOUR REST API KEY"

    def getString(self, strInput):
        outStr = unicode(strInput.toUtf8(),"utf-8")
        return outStr.strip()

    def __init__(self, usr, pwd = None):       
       self.parseRegister = register(self.APP_ID, self.REST_API_KEY)
       self.usr = self.getString(usr)
       if pwd:
           self.pwd = self.getString(pwd)

    def passwordReset(self):
        User.request_password_reset(email=self.usr)
        

    def checkLogin(self):
      try:
         u = User.login(self.usr, self.pwd)
         return True
      except:
         return False  
