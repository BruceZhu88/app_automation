
import json
import sys
from src.common.Logger import Logger
from src.common.app import App
from src.common.AppiumScreenshot import ScreenShot
log = Logger("main").logger()

with open('../config/MyObservatoryEle.json') as json_file:
    ele = json.load(json_file)


class MyObservatory(App):

    @classmethod
    def my_click(cls, type_name, name, timeout=15):
        value = ele.get(name)
        if value is None:
            value = name
        if not cls.click(type_name, value, name, timeout=timeout):
            name = 'cannot_find_' + name
            log.info(name)
            cls.shot(name)
            return False
        return True

    @classmethod
    def shot(cls, path, name):
        ScreenShot(cls.driver).get_screenshot(path, name)
