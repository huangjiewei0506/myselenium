import time
import unittest
from selenium import webdriver

from page_object.index_page import IndexPage
from page_object.login_page import LoginPage


class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Chrome('/Users/huangjiewei/Documents/chromedriver')
        cls.lp=LoginPage(cls.driver)
        cls.ip=IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_1_login(self):
        #测试数据
        username = '756898445@qq.com'
        password = 'LTXWJwyyjk123'
        txt='123'

        #测试流程
        self.lp.login(username, password)
        time.sleep(2)
        self.ip.search(txt)
        time.sleep(2)
        #driver.quit()



if __name__ == '__main__':
    unittest.main()
