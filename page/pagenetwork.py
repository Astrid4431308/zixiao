import os,sys
sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from base.baseaction import BaseAction

more_button = By.XPATH,"//*[contains(@text,'更多')]"
movable_button = By.XPATH,"//*[contains(@text,'移动网络')]"
first_choice_button = By.XPATH,"//*[contains(@text,'首选网络类型')]"
type_2g = By.XPATH,"//*[contains(@text,'2G')]"
type_3g = By.XPATH,"//*[contains(@text,'3G')]"


class PageNetWork(BaseAction):
    def __init__(self,driver):
        self.driver = driver
        self.clicks(more_button)
        self.clicks(movable_button)
        self.clicks(first_choice_button)

    def type_2G(self):
        self.clicks(type_2g)

    def type_3G(self):
        self.clicks(type_3g)