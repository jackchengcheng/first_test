'''
Created on 2017年2月16日

@author: fanzhaoni
'''
from selenium.webdriver.common.action_chains import ActionChains     #鼠标事件
from selenium.webdriver.common.by import By
from page_com.CommonControl import CommonControl
from time import sleep
from models.driver import browser

class login(CommonControl):
    '''
    用户登录页面
    '''
    #url = '/login.nk'
    url = '/platform/login.shtml'
   # base_url = 'http://172.16.0.25:8011'
    #Action
#     login_username_loc = (By.XPATH,"//input[@id='id_name']")  
#     login_password_loc = (By.XPATH,"//input[@id='id_password']")  
#     login_button_loc = (By.XPATH,"//button[@type='submit']")
    
    login_username_loc = (By.XPATH,"//input[@id='userName']")  
    login_password_loc = (By.XPATH,"//input[@id='password']")  
    login_button_loc = (By.XPATH,"//button[@type='button']")
    #登录用户名
    def login_username(self,username):
        self.Set_input(self.login_username_loc, username)
    
    #登录密码
    def login_password(self,password):
        self.Set_input(self.login_password_loc, password)
        
    #登录按钮
    def login_button(self):
        self.Set_Button(self.login_button_loc)
        
    #定义统一登录入口
    def user_login(self,username="4222787",password="123456"):
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(5)
    
    login_error_hint_loc = (By.XPATH,"//*[@id='spanMsg']")
    login_sucess_loc = (By.LINK_TEXT,"工作台")
    
    #用户名或者密码错误
    def login_error_hint(self):
        return self.find_element(*self.login_error_hint_loc).text
    
    #登录成功
    def login_sucess(self):
        return self.find_element(*self.login_sucess_loc)
    
    
    
    
        