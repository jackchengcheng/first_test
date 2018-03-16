'''
Created on 2018年2月22日

@author: fanzhaoni
'''
import unittest
from time import sleep
import random
from models import myunit,function
from page_obj.login_page import login


class loginTest(myunit.MyTest):
    '''法律IBOSS登录测试'''
    #测试用户登录
    def user_login_verify(self,username="",password=""):
        login(self.driver).user_login(username, password)
    
    def test_login1(self):
        '''账号不存在'''
        character = random.choice('abcdefghigklmn')
        username = "zhangshan" +character
        self.user_login_verify( username=username, password="123456")
        po = login(self.driver)
        function.insert_img(self.driver, "login_error1.jpg")
        asserttest = "帐号["+ username +"]不存在,请重新输入！"
        self.assertEqual(po.login_error_hint(), asserttest)
        
    def test_login2(self):
        '''密码错误'''
        self.user_login_verify( username="4222787", password="456789")
        po = login(self.driver)
        function.insert_img(self.driver, "login_error2.jpg")
        self.assertEqual(po.login_error_hint(), "密码错误,请重新输入！")   
        
    def test_login3(self):
        ''' 用户名密码正确'''
        self.user_login_verify(username="4222787", password="666666")  
        sleep(2)
        po = login(self.driver)
        self.assertTrue(po.login_sucess())
        function.insert_img(self.driver, "login_sucess.jpg")
 
 
 
if __name__ == '__main__':
    unittest.main()
