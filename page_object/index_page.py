import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from selenium import webdriver


class IndexPage(BasePage):
     #核心元素
    url="https://lanhuapp.com/web/#/item"

    #首页搜索按钮，关键字输入框
    search_button=(By.CLASS_NAME,'serch_icon')
    input_button=(By.XPATH,"//div[@class='search on']//input[@type='text']")
    makesure_search=(By.XPATH,"//div[@class='search_btn']")

    def search(self,txt):
         self.visit()
         self.click(self.search_button)
         time.sleep(2)
         self.input_(self.input_button,txt)





