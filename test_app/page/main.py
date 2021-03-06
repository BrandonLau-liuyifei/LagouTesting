import logging
import os

from appium import webdriver
from selenium.webdriver.common import utils
from selenium.webdriver.common.by import By

from test_app.page.base_page import BasePage
from test_app.page.search import SearchPage
from test_app.page.stock_select import StockSelect
from test_app.page.trade import TradePage


class MainPage(BasePage):

    def __init__(self):
        caps = {
            "platformName": "android",
            "deviceName": "hogwarts",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "autoGrantPermissions": "true",
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            "chromedriverExecutableDir": "/Users/seveniruby/projects/chromedriver/chromedrivers",
            "chromedriverChromeMappingFile": "/Users/seveniruby/PycharmProjects/LagouTesting/test_app/chromedriver.json",
            #并行运行
            "udid": os.getenv("udid", None),
            'systemPort': utils.free_port(),
            'chromedriverPort': utils.free_port(),

        }

        logging.info(caps)
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.implicitly_wait()
        self.wait(["同意", "image_cancel", "home_search"], timeout=60)

        # self.find_element(By.ID, "image_cancel").click()
        # self.find_element(By.ID, "tv_agree").click()

    def search(self):
        self.find_element(By.ID, "tv_search").click()
        return SearchPage(self.driver)

    def stock_select(self):
        self.find_element(
            By.XPATH,
            "//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='行情']"
        ).click()
        return StockSelect(self.driver)

    def trade(self):
        self.click(By.XPATH, "//*[contains(@resource-id, 'tab') and @text='交易']")
        return TradePage(self.driver)
