import time

from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('/Users/huangjiewei/Documents/chromedriver')
cookies01={
    # "SERVERID":"a86bc0b1a9d00a213d948f33f18a2db0|1639730093|1639729696",
    # "JSESSIONID":"048C448C74956564A75AF30579C0C790",
    "name":"api_account_token",
    "value":"api_account_token_B5A1C9AEF3B65977ACD45109C5FFE503521050D0E39AA0541C3F2DB0FA70DDB3"
}
cookies02={
    # "SERVERID":"a86bc0b1a9d00a213d948f33f18a2db0|1639730093|1639729696",
    # "JSESSIONID":"048C448C74956564A75AF30579C0C790",
    "name":"JSESSIONID",
    "value":"048C448C74956564A75AF30579C0C790"
}
cookies03={
    "name":"SERVERID",
    "value":"a86bc0b1a9d00a213d948f33f18a2db0|1639730737|1639729696"
}
cookies04={
    "name":"acgt_ae",
    "value":"B5A1C9AEF3B65977ACD45109C5FFE503521050D0E39AA0541C3F2DB0FA70DDB3"
}
cookies05={
    "name":"acgt_an",
    "value":"B5A1C9AEF3B65977ACD45109C5FFE503521050D0E39AA0541C3F2DB0FA70DDB3B5A1C9AEF3B65977ACD45109C5FFE503521050D0E39AA0541C3F2DB0FA70DDB3"
}
cookies06={
    "name":"acgtgt_c",
    "value":"BD2D8FC6BC0F3307BEC6FA14307FE97A69CE90B5AC48E255EC4F82EA"
}

browser.maximize_window()
browser.get('https://www.douban.com')
#browser.delete_all_cookies()
#browser.find_element(By.XPATH,"//span[text()='数读十九届六中全会精神']").click()
#browser.find_element(By.XPATH,"//input[@placeholder='请输入用户名']").send_keys("123")
#browser.find_element(By.XPATH,"//input[@placeholder='请输入密码']").send_keys("456")
# browser.add_cookie(cookies01)
# browser.add_cookie(cookies02)
# browser.add_cookie(cookies03)
# browser.add_cookie(cookies04)
#
# browser.add_cookie(cookies05)
# browser.add_cookie(cookies06)
# time.sleep(3)
# browser.get('https://www.douban.com')
time.sleep(3)
browser.find_element(By.XPATH,"//div[@class='account-body-tabs']/ul/li[text()='密码登录']").click()

# TODO 记录要做的事情



