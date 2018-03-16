'''
Created on 2018年2月22日

@author: fanzhaoni
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
import unittest, time, re

class BusinessTestCase(unittest.TestCase):
    def setUp(self):
 
         # 加启动配置 （用于去掉启动浏览器出现‘Chrome正在受到自动软件的控制’）
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
    
        # 打开chrome浏览器
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.base_url = "https://192.168.254.80:8037"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_Business(self):
        driver = self.driver
        url = self.base_url +"/platform/index.shtml"
        driver.get(url)
        time.sleep(3)
        driver.find_element_by_id("userName").click()
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("4222787")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("666666")
        driver.find_element_by_xpath("//button[@type='button']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//span[starts-with(text(),'商机')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//span[starts-with(text(),'跟进中')]").click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[starts-with(@src,'/bus/list/followingIndex.shtml')]"))
        time.sleep(10)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()