"""
loginpage类
"""
import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage
from selenium import webdriver


class LoginPage(BasePage):
     #核心元素
    url="https://lanhuapp.com/web/#/user/login"

    user=(By.XPATH,"//input[@placeholder='手机号码或邮箱']")
    password=(By.XPATH,"//input[@placeholder='密码']")
    login_button=(By.XPATH,"//div[text()=' 登录 ']")

    def login(self,username,pwd):
         self.visit()
         self.input_(self.user,username)
         self.input_(self.password,pwd)
         self.click(self.login_button)





