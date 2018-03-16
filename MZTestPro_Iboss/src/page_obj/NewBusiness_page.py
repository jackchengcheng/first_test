'''
Created on 2018年3月2日

@author: fanzhaoni
'''
from selenium.webdriver.common.action_chains import ActionChains     #鼠标事件
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from page_obj.menu_page import menu
from page_com.CommonControl import CommonControl
from time import sleep
from models.driver import browser
from calendar import setfirstweekday

class NewBusiness(menu,CommonControl):
    '''
    新建商机页面
    '''
    
    NewBus_NewBusinessForm_loc = (By.ID,"newBusinessForm")                     #新增商机表单form   
    NewBus_ContactWay_loc = (By.ID,"check_type")                               #联系方式
    NewBus_ContactNum_loc = (By.ID,"checkInfoText")                            #联系号码
    NewBus_Search_loc = (By.ID,"buttonsearch")                                 #搜索按钮
    NewBus_CustomerName_loc = (By.NAME,"customerName")                         #客户姓名
    NewBus_BusinessTypeName_loc = (By.NAME,"businessTypeName")                 #业务类型
    NewBus_AreaName_loc = (By.NAME,"areaName")                                 #区域名
    NewBus_LoanAmount_loc = (By.NAME,"loanAmountText")                         #贷款金额
    NewBus_IdCard_loc = (By.NAME,"idCard")                                     #省份证号码
    NewBus_birthday_loc = (By.NAME,"birthday")                                 #生日
    NewBus_Age_loc = (By.ID,"age")                                             #年龄
    NewBus_Sex_loc = (By.NAME,"sex")                                           #性别
    NewBus_Residence_loc = (By.NAME,"registeredResidence")                     #户口所在地
    NewBus_Address_loc = (By.ID,"address")                                     #客户地址
    NewBus_Email_loc = (By.ID,"email")                                         #邮箱
    NewBus_MaritalStatus_loc = (By.NAME,"maritalStatus")                       #婚姻状态
    NewBus_EduBackground_loc = (By.NAME,"eduBackground")                       #教育背景
    NewBus_LoanTime_loc = (By.NAME,"loanTime")                                 #急需时间
    NewBus_LoanCycle_loc = (By.NAME,"loanCycle")                               #贷款周期
    NewBus_LoanInterrestRate_loc = (By.NAME,"loanInterrestRate")               #利率要求                                                     
    NewBus_LoanRateValue_loc = (By.NAME,"loadInterrestValue")                  #利率值                                                     
    NewBus_RepaymentType_loc = (By.NAME,"repaymentType")                       #还款方式       
    NewBus_Description_loc = (By.ID,"description")                             #客户留言                
    NewBus_SaveBusiness_loc = (By.XPATH,"//button[@onclick='saveBusiness()']") #保存商机
    NewBus_Confirm_loc = (By.LINK_TEXT,"确定")                                  #确定

    
    #下来框的二次封装
    def Set_Selects(self,mainloc,Selecttitle):
        Select_loc = (By.XPATH,"//option[contains(text(),'%s')]" % Selecttitle)
        self.Set_Droplist(mainloc,Select_loc,Selecttitle)
    
    #选择联系方式
    def SelectContactWay(self,ContactWay="QQ"):
        self.Set_Selects(self.NewBus_ContactWay_loc, ContactWay)
    
    #联系号码
    def InputContactNum(self,ContactNum = "14352346"):
        self.Set_input(self.NewBus_ContactNum_loc, ContactNum)

    #点击搜索
    def ButtonSearch(self):
        self.Set_Button(self.NewBus_Search_loc)
        
    #输入客户名字
    def InputcustomerName(self,customerName="fanzhaonitest"):
        self.Set_input(self.NewBus_CustomerName_loc, customerName)
    
    #选择业务类型
    def SelectBusinessType(self,businessType="信用贷款/空放"):
        self.Set_CascadeSelect(self.NewBus_BusinessTypeName_loc, businessType)
    
    #选择地区
    def SelectAreaName(self,areaName="四川省/成都市/天府新区"):
        self.Set_CascadeSelect(self.NewBus_AreaName_loc, areaName)

    #输入贷款金额
    def InputLoanAmount(self,loanAmount="36"):
        self.Set_input(self.NewBus_LoanAmount_loc, loanAmount)

    #输入身份证号码
    def InputIdCard(self,idCard="142724198803121111"):
        self.Set_input(self.NewBus_IdCard_loc, idCard)
    
    #输入生日
    def InputBirthday(self,birthday="1988-03-12"):
        self.Set_input(self.NewBus_birthday_loc, birthday)    
        #时间控件用完后必须要返回到所有操作的form下面
        self.find_element(*self.NewBus_NewBusinessForm_loc).click()
    
    #年龄
    def InputAge(self,age = "30"):
        self.Set_input(self.NewBus_Age_loc, age) 
           
    #性别
    def SelectSex(self,sex="女"):
        self.Set_Selects(self.NewBus_Sex_loc,sex)

    #户口所在地
    def SelectResidence(self,Residence="四川省/成都市/天府新区"):
        self.Set_CascadeSelect(self.NewBus_Residence_loc, Residence)    
    
    #客户地址
    def InputAddress(self,address="客户地址"):
        self.Set_input(self.NewBus_Address_loc, address)

    #邮箱
    def InputEmail(self,email="fanzhaoni@126.com"):
        self.Set_input(self.NewBus_Email_loc, email)
    
    #选择婚姻状态
    def SelectMaritalStatus(self,MaritalStatus="未婚"):        
        self.Set_Selects(self.NewBus_MaritalStatus_loc, MaritalStatus)
        
    #选择学历
    def SelectEduBackground(self,EduBackground="本科"):        
        self.Set_Selects(self.NewBus_EduBackground_loc, EduBackground)
    #选择急需时间
    def SelectLoanTime(self,LoanTime="3个月内"):        
        self.Set_Selects(self.NewBus_LoanTime_loc, LoanTime)
    #选择贷款周期
    def SelectLoanCycle(self,LoanCycle="5年以上"):        
        self.Set_Selects(self.NewBus_LoanCycle_loc, LoanCycle)
    #选择利率要求 
    def SelectLoanInterrestRate(self,LoanInterrestRate="月息"):        
        self.Set_Selects(self.NewBus_LoanInterrestRate_loc, LoanInterrestRate)        
    #选择利率值 
    def SelectLoanRateValue(self,LoanRateValue="无利息要求"):        
        self.Set_Selects(self.NewBus_LoanRateValue_loc, LoanRateValue)
    #选择还款方式 
    def SelectRepaymentType(self,RepaymentType="先息后本"):        
        self.Set_Selects(self.NewBus_RepaymentType_loc, RepaymentType)                                                                                              

    #保存商机
    def ButtonSaveBusiness(self):
        self.Set_Button(self.NewBus_SaveBusiness_loc)
    
    def Submit(self):    
        self.Set_Button(self.NewBus_Confirm_loc)
     
    def Message(self):
        try:
            alert =self.switch_Alert()  #使用driver.switchTo().alert()方法获取到alert对象
            print(alert.getText)
        except:
            print("尝试操作的alert框没有被找到");
        
    def Interface_NewBusiness(self,OrderInfro="/bus/newBusiness/toAdd.shtml"):
        xpath_loc = (By.XPATH,"//iframe[starts-with(@src,'%s')]" % OrderInfro)
        #print(xpath_loc)
        if self.IS_element_present(xpath_loc):
            frameOrder = self.find_element(*xpath_loc)
            self.switch_frame(frameOrder)
            return True
        else:
            print("找不到 %s"%xpath_loc,"停止测试")
            return False
    
    def NewBusiness(self,LoginType=1,username="4222787",password="666666"):   
        self.menu_NewBusiness(LoginType, username, password)
        return self.Interface_NewBusiness(OrderInfro="/bus/newBusiness/toAdd.shtml")
        
        
        
        
        
        