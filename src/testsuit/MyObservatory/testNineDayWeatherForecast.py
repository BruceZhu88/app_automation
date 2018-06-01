
import json
from .baseCase import *
from src.common.Logger import Logger
log = Logger("main").logger()

with open('../config/MyObservatoryEle.json') as json_file:
    ele = json.load(json_file)


class TestNineDayWeatherForecast(BaseCase):

    def testDisplayWeather(self):
        # Agree App protocol
        MyObservatory.my_click('id', 'agree')
        MyObservatory.my_click('id', 'agree')
        MyObservatory.my_click('id', 'whats_new_close')
        # Check if in home page

        # Open Side Menu
        MyObservatory.find_ele('class_', 10, 'android.widget.ImageButton')[0].click()
        # Select item: 9-Day Weather Forecast
        MyObservatory.my_click('ui', '9_day_forecast_btn')
        # Check if in page "9-day Forecast"
        assert MyObservatory.find_text(ele.get("9_day_forecast_title"))
        # Check if default item is "9-day Forecast"
        assert MyObservatory.find_ele('id', 'title_selected').text() == ele.get("9_day_forecast_title")
        # Verify Forecast of the next 9 days are displayed
        dates = MyObservatory.find_ele('id_', 'forecast_dates')
        # Check if it includes 9 days
        assert len(dates) == 9
        # Check every day's content
        for day in dates:
            day.text()

