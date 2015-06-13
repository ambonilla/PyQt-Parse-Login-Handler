# PyQt-Parse-Login-Handler
A login handler for Parse made on Python 2.7 and PyQt 4

##Dependencies:
- [PyQt 4]
- [Python 2.7]
- [ParsePy]

##Usage:

On ParseHandler.py modify lines 9 and 10 with your APP ID and REST API KEY

```
    APP_ID = "YOUR APP ID"
    REST_API_KEY = "YOUR REST API KEY"
```

You can also customize the messages, background, and login icon inside LoginController.py

In case you want to include this inside another project you can use this example before calling your Main Window or Widget:

```
   app = QApplication(sys.argv)   
   newLogin = Login()
   if newLogin.exec_() == QDialog.Accepted:
      newLogin.destroy()
      #Call your Window or Widget here
   else:
      exit()
   
   sys.exit(app.exec_())
```


[PyQt 4]:http://www.riverbankcomputing.com/software/pyqt/download
[Python 2.7]:https://www.python.org/downloads/
[ParsePy]:https://github.com/dgrtwo/ParsePy
