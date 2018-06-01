
import os
import sys
import datetime
from src.runner.testrunner import TestRunner
from src.common.adb import adb
from src.common.cfg import Config
from src.MyObservatory import MyObservatory
from src.common.Logger import Logger

log = Logger("main").logger()

testconfig = Config('../config/testconfig.ini')
testconfig.cfg_load()
tcfg = testconfig.cfg


def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def connect_phone():
    if not adb.check_device_status():
        log.error('Please check your phone')
        sys.exit()
    log.info('Connecting with your phone ...')
    try:
        MyObservatory.connect(platformName=tcfg.get('App', 'platformName'),
                              deviceName=tcfg.get('App', 'deviceName'),
                              timeout=tcfg.get('App', 'timeout'),
                              appPackage=tcfg.get('MyObservatory', 'appPackage'),
                              appActivity=tcfg.get('MyObservatory', 'appActivity'),
                              remote_server=tcfg.get('Appium', 'remote_server'),
                              )
    except Exception as e:
        log.error('Cannot connect to your phone: {}'.format(e))
        sys.exit()


# Prepare report path and file info
report_path = tcfg.get('Report', 'report_path')
testlist = tcfg.get('TestCase', 'list')
make_dir(report_path)
prj_name = 'MyObservatoryEle -- Weather forecast'
report_name = '{}/{}_test_report_{}.html'.format(
    report_path, prj_name, datetime.datetime.now().strftime('%m%d%H%M%S'))
title = '{} Automation Test Report'.format(prj_name)
description = 'Test Execution Details:'

# Start to connect test phone
connect_phone()

# Run test case
TR = TestRunner(report_name, title, description, testlist)
TR.run()
