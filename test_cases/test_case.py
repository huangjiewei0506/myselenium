import time
import unittest
from selenium import webdriver

from page_object.index_page import IndexPage
from page_object.login_page import LoginPage


class TestCase(unittest.TestCase):
    def test_1_login(self):
        #此处Chrome为大写，并且后面指定driver的存放路径
        driver=webdriver.Chrome('/Users/huangjiewei/Documents/chromedriver')
        username = '756898445@qq.com'
        password = 'LTXWJwyyjk123'
        txt='123'
        lp = LoginPage(driver)
        lp.login(username, password)
        #将driver传递给这个页面对象，等于使用了同个浏览器
        ip=IndexPage(driver)
        time.sleep(3)
        ip.search(txt)
        time.sleep(3)
        #driver.quit()


if __name__ == '__main__':
    unittest.main()
