import time
import unittest
from selenium import webdriver

from page_object.index_page import IndexPage
from page_object.login_page import LoginPage
from ddt import ddt,file_data,data

@ddt
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
       # '/Users/huangjiewei/Documents/chromedriver'
        cls.driver=webdriver.Chrome()
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


    @data('123')
    def test_2_search(self,txt):
        # 测试数据

        # 测试流程
        self.ip.search(txt)
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
