from time import sleep

from selenium import webdriver
import selenium

class BasePage:


    def __init__(self,driver):
        self.driver=driver

    def visit(self):
        self.driver.get(self.url)

    def locator(self,loc):
        #*loc为一个元组
        return self.driver.find_element(*loc)

    def input_(self,loc,txt):
        self.locator(loc).send_keys(txt)

    def click(self,loc):
        self.locator(loc).click()

    def wait(self,time_):
        sleep(time_)
