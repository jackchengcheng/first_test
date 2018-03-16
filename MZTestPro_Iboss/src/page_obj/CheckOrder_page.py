'''
Created on 2017年3月14日

@author: 20170207
'''
from selenium.webdriver.common.action_chains import ActionChains     #鼠标事件
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from page_obj.menu_page import menu
from page_com.CommonControl import CommonControl
from time import sleep
from models.driver import browser

class CheckOrder(menu,CommonControl):
    '''
    下单审核前端页面
    '''


    def Interface_BusinessCheck(self):
        self.SwitchTomainwindows()
        #切换到当前表单下面
        self.switch_frame("noka_menu_cent_body_body_iframe_163")
        
    
    #列表检查
    
    
    #列表操作
        
        
    
        