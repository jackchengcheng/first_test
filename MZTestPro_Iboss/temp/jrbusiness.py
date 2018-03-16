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
from page_com.CommonControl import CommonControl
import unittest, time, re

class BusinessTestCase(unittest.TestCase,CommonControl):
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
        
        driver.find_element_by_xpath("//span[starts-with(text(),'新增商机')]").click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[starts-with(@src,'/bus/newBusiness/toAdd.shtml')]"))
        driver.find_element_by_id("check_type").click()
        Select(driver.find_element_by_id("check_type")).select_by_visible_text("QQ")
        driver.find_element_by_xpath("//option[@value='QQ']").click()
        driver.find_element_by_id("checkInfoText").click()
        driver.find_element_by_id("checkInfoText").clear()
        driver.find_element_by_id("checkInfoText").send_keys("56546567")
        driver.find_element_by_id("buttonsearch").click()
        time.sleep(3)
        driver.find_element_by_name("customerName").click()
        driver.find_element_by_name("customerName").clear()
        driver.find_element_by_name("customerName").send_keys("test_fzn_A")
        driver.find_element_by_name("businessTypeName").click()
        driver.find_element_by_link_text("信用贷款").click()
        driver.find_element_by_link_text("空放").click()
        driver.find_element_by_name("areaName").click()
        driver.find_element_by_link_text(u"四川省").click()
        driver.find_element_by_link_text(u"成都市").click()
        driver.find_element_by_link_text(u"天府新区").click()
        driver.find_element_by_name("loanAmountText").click()
        driver.find_element_by_name("loanAmountText").clear()
        driver.find_element_by_name("loanAmountText").send_keys("36")
        driver.find_element_by_name("idCard").click()
        driver.find_element_by_name("idCard").clear()
        driver.find_element_by_name("idCard").send_keys("142724198707112222")
        driver.find_element_by_name("birthday").click()
        driver.find_element_by_name("birthday").clear()
        driver.find_element_by_name("birthday").send_keys("1987-07-11")
        #时间控件用完后必须要返回到所有操作的form下面
        driver.find_element_by_id("newBusinessForm").click()
        driver.find_element_by_id("age").click()
        driver.find_element_by_id("age").clear()
        driver.find_element_by_id("age").send_keys("31")
        driver.find_element_by_name("sex").click()
        Select(driver.find_element_by_name("sex")).select_by_visible_text(u"女")
        driver.find_element_by_name("registeredResidence").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'四川省')])[3]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'成都市')])[3]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'天府新区')])[3]").click()
        driver.find_element_by_id("address").click()
        driver.find_element_by_id("address").clear()
        driver.find_element_by_id("address").send_keys(u"客户地址")
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("fanzhaoni@126.com")
        driver.find_element_by_name("maritalStatus").click()
        driver.find_element_by_xpath("//option[@value='HYZK_WH']").click()
        driver.find_element_by_name("eduBackground").click()
        Select(driver.find_element_by_name("eduBackground")).select_by_visible_text(u"本科")
        driver.find_element_by_xpath("//option[@value='KHXL_BK']").click()
        driver.find_element_by_name("loanTime").click()
        Select(driver.find_element_by_name("loanTime")).select_by_visible_text(u"3个月内")
        driver.find_element_by_xpath("//option[@value='CUS_JXSJ_3M']").click()
        driver.find_element_by_name("loanCycle").click()
        Select(driver.find_element_by_name("loanCycle")).select_by_visible_text(u"5年以上")
        driver.find_element_by_xpath("//option[@value='CUS_DKZQ_5YYS']").click()
        driver.find_element_by_name("loanInterrestRate").click()
        Select(driver.find_element_by_name("loanInterrestRate")).select_by_visible_text(u"月息")
        driver.find_element_by_xpath("//option[@value='CUS_LLZQ_M']").click()
        driver.find_element_by_name("loadInterrestValue").click()
        Select(driver.find_element_by_name("loadInterrestValue")).select_by_visible_text("0.7%~1%")
        driver.find_element_by_xpath("//option[@value='CUS_LLFS_0.7-1']").click()
        driver.find_element_by_name("repaymentType").click()
        Select(driver.find_element_by_name("repaymentType")).select_by_visible_text(u"先息后本")
        driver.find_element_by_xpath("//option[@value='CUS_HKFS_XXHB']").click()
#         driver.find_element_by_link_text(u"编辑").click()
#         time.sleep(5)
#         driver.find_element_by_xpath("(//input[@name='attrBuildings[0].payType'])[3]").click()
#         driver.find_element_by_xpath("(//input[@name='attrVehicles[0].payType'])[3]").click()
#         driver.find_element_by_xpath("(//input[@name='warranty'])[2]").click()
#         driver.find_element_by_xpath("(//input[@name='attrJob.jobNature'])[5]").click()
#         driver.find_element_by_xpath("(//input[@name='social'])[2]").click()
#         driver.find_element_by_xpath("(//input[@name='money'])[2]").click()
#         driver.find_element_by_xpath("(//input[@name='attrLiability.liabilityType'])[6]").click()
#         driver.find_element_by_xpath("(//input[@name='liabilities'])[2]").click()
#         driver.find_element_by_xpath("(//input[@name='ids'])[5]").click()
#         driver.find_element_by_link_text(u"保存").click()
#         driver.find_element_by_xpath("//form[@id='newBusinessForm']/table/tbody/tr[20]/th/span").click()
        driver.find_element_by_id("description").click()
        driver.find_element_by_id("description").clear()
        driver.find_element_by_id("description").send_keys(u"客户留言")
        driver.find_element_by_xpath("//button[@onclick='saveBusiness()']").click()
        print(self.GetBubbleText())
        if self.GetBubbleText()==False:
            driver.find_element_by_link_text(u"确定").click()

    
        time.sleep(20)
    
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