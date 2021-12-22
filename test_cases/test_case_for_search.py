import time
import unittest
from selenium import webdriver

from page_object.index_page import IndexPage
from page_object.login_page import LoginPage
from ddt import ddt,file_data

@ddt
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Chrome('/Users/huangjiewei/Documents/chromedriver')
        cls.lp=LoginPage(cls.driver)
        cls.ip=IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @file_data('../data/user.yaml')
    def test_1_login(self,username,password):


        #测试流程
        self.lp.login(username, password)
        time.sleep(2)

    def test_2_search(self):
        # 测试数据
        txt = '456'

        # 测试流程
        self.ip.search(txt)
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
