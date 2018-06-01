================================

Author: Bruce.Zhu
Time：2018/04/28

================================

Environment:
	OS: Windows 10
	Appium destop version: 1.7.2
	Python version: 3.4
================================

How to start:
    Run run.py

================================
Tree of whole project:
	
│  Readme.txt
│
├─config
│      logger_main.conf
│      MyObservatoryEle.json
│      testconfig.ini
│
├─log
│      main.log
│
├─report
│      MyObservatoryEle -- Weather forecast_test_report_0428142825.html
│
├─src
│  │  run.py
│  │  __init__.py
│  │
│  ├─common
│  │      adb.py
│  │      app.py
│  │      AppiumScreenshot.py
│  │      cfg.py
│  │      Logger.py
│  │      __init__.py
│  │
│  ├─MyObservatory
│  │      MyObservatory.py
│  │      __init__.py
│  │
│  ├─runner
│  │      HTMLTestRunner.py
│  │      testrunner.py
│  │      __init__.py
│  │
│  └─testsuit
│      │  __init__.py
│      │
│      └─MyObservatory
│              baseCase.py
│              testNineDayWeatherForecast.py
│              __init__.py
│
└─testfile
    └─testcase
            caselist.txt