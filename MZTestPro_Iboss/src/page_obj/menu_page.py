'''
Created on 2017年3月3日

@author: 20170207

'''

from selenium.webdriver.common.by import By
from page_obj.login_page import login
from time import sleep

class menu(login):
    '''
    菜单元素
    '''
        
    #商机菜单
    menu_Business_loc = (By.XPATH,"//span[starts-with(text(),'商机')]") #商机-----主菜单
    menu_NewBusiness_loc = (By.XPATH,"//span[starts-with(text(),'新增商机')]")#新增商机
    menu_Allocated_loc = (By.XPATH,"//span[starts-with(text(),'已分配')]")#已分配
    menu_ToFollowUp_loc = (By.XPATH,"//span[starts-with(text(),'待跟进')]")#待跟进
    menu_Following_loc = (By.XPATH,"//span[starts-with(text(),'跟进中')]")#跟进中
    menu_SignedBill_loc = (By.XPATH,"//span[starts-with(text(),'已签单')]")#已签单
    menu_InAndOut_loc = (By.XPATH,"//span[starts-with(text(),'出入库记录')]")#出入库记录
    menu_KeyBusiness_loc = (By.XPATH,"//span[starts-with(text(),'重点商机')]")#重点商机
    menu_Pending_loc = (By.XPATH,"//span[starts-with(text(),'待处理')]")#待处理
    
    
    #订单菜单
    menu_Order_loc = (By.XPATH,"//span[starts-with(text(),'订单')]")#订单-----订单
    menu_AllOrder_loc = (By.XPATH,"//span[starts-with(text(),'全部订单')]")#全部订单
    menu_MyPendingOrder_loc = (By.XPATH,"//span[starts-with(text(),'我的待审核')]")#我的待审核
    menu_PreOrder_loc = (By.XPATH,"//span[starts-with(text(),'下单')]")#下单
    menu_AuditedOrder_loc = (By.XPATH,"//span[starts-with(text(),'已审核订单')]")#已审核订单
    menu_DraftBox_loc = (By.XPATH,"//span[starts-with(text(),'草稿箱')]")#草稿箱
    menu_PendingOrder_loc = (By.XPATH,"//span[starts-with(text(),'待审核订单')]")#待审核订单
    menu_RejectedOrder_loc = (By.XPATH,"//span[starts-with(text(),'订单被驳回')]")#订单被驳回
    
    
    '''点击菜单，确保菜单可见'''
    def menu_Click(self,Mainmenu,Submenu):
        if self.IS_element_present(Submenu) is None:
            self.find_element(*Mainmenu).click()
            sleep(2)
        self.find_element(*Submenu).click()
    '''商机菜单'''
    def menu_SubBusiness(self,Submenu,LoginType=1,username="4222787",password="0359422400"):
        if LoginType==1:
            self.user_login(username,password)
            self.SwitchTomainwindows()
        self.menu_Click(self.menu_Business_loc,Submenu)     
    #新增商机菜单
    def menu_NewBusiness(self,LoginType=1,username="4222787",password="0359422400"):
        self.menu_SubBusiness(self.menu_NewBusiness_loc,LoginType,username,password)
    #已分配菜单
    def menu_Allocated(self,LoginType=1,username="4222787",password="0359422400"):
        self.menu_SubBusiness(self.menu_Allocated_loc,LoginType,username,password)
    #待跟进
    def menu_ToFollowUp(self,LoginType=1,username="4222787",password="0359422400"):
        self.menu_SubBusiness(self.menu_ToFollowUp_loc,LoginType,username,password)
    #跟进中
    def menu_Following(self,LoginType=1,username="4222787",password="0359422400"):
        self.menu_SubBusiness(self.menu_Following_loc,LoginType,username,password)
    #已签单
    def menu_SignedBill(self,LoginType=1,username="4222787",password="0359422400"):
        self.menu_SubBusiness(self.menu_SignedBill_loc,LoginType,username,password)
    #出入库记录
    def menu_InAndOut(self,LoginType=1,username="4222787",password="0359422400"):
        self.menu_SubBusiness(self.menu_InAndOut_loc,LoginType,username,password) 
    #重点商机
    def menu_KeyBusiness(self,LoginType=1,username="4222787",password="0359422400"):
        self.menu_SubBusiness(self.menu_KeyBusiness_loc,LoginType,username,password)      
    #待处理
    def menu_Pending(self,LoginType=1,username="4222787",password="0359422400"):
        self.menu_SubBusiness(self.menu_Pending_loc,LoginType,username,password)   
    
    '''订单菜单'''
    def menu_SubOrder(self,Submenu,LoginType=1,username="4222787",password="0359422400"):
        if LoginType==1:
            self.user_login(username,password)
            self.SwitchTomainwindows()
        self.menu_Click(self.menu_Order_loc,Submenu)    
        
        
    #全部订单菜单
    def menu_AllOrder(self,LoginType=1,username="4222787",password="0359422400"):
        self.menu_SubOrder(self.menu_AllOrder_loc,LoginType,username,password)   
    #我的待审核菜单
    def menu_MyPendingOrder(self,LoginType=1,username="4222787",password="0359422400"):
        self.menu_SubOrder(self.menu_MyPendingOrder_loc,LoginType,username,password)
    #下单菜单
    def menu_PreOrder(self,LoginType=1,username="4222787",password="0359422400"):
        self.menu_SubOrder(self.menu_PreOrder_loc,LoginType,username,password)
    #已审核订单
    def menu_AuditedOrder(self,LoginType=1,username="4222787",password="0359422400"):
        self.menu_SubOrder(self.menu_AuditedOrder_loc,LoginType,username,password)
    #草稿箱菜单
    def menu_DraftBox(self,LoginType=1,username="4222787",password="0359422400"):
        self.menu_SubOrder(self.menu_DraftBox_loc,LoginType,username,password)
    #待审核订单菜单
    def menu_PendingOrder(self,LoginType=1,username="4222787",password="0359422400"):
        self.menu_SubOrder(self.menu_PendingOrder_loc,LoginType,username,password)
    #订单被驳回菜单
    def menu_RejectedOrder(self,LoginType=1,username="4222787",password="0359422400"):
        self.menu_SubOrder(self.menu_RejectedOrder_loc,LoginType,username,password)

    #切换到主窗口
    def SwitchTomainwindows(self):
        self.mainwindows = self.Getmainwindows()
        self.switch_windows(self.mainwindows)
    
