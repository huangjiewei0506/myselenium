
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from selenium import webdriver


class IndexPage(BasePage):
     #核心元素
    url="https://lanhuapp.com/web/#/item"

    search_button=(By.CLASS_NAME,'serch_icon')


    def search(self,txt):
         self.visit()
         self.click(self.search_button)




