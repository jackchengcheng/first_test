'''
Created on 2017年2月16日

@author: fanzhaoni
'''
import unittest
from selenium import webdriver
from models.driver import browser
import os

'''
因为所有的测试类中的setUp()与tearDowm()方法所做的事情相同,
所以将他们抽象为MyTest()类,好处就是在编写测试用例时不再考虑这两个方法的实现
'''
class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = browser()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        print("MyTest")

#     def setUp(self):
#         self.driver = browser()
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(3)
# 
#         print("hahaha")
        
    @classmethod   
    def tearDownClass(self):
        self.driver.quit() 
           
#     def tearDown(self):
#         self.driver.quit()
    
    '''
    def test_print(self):
        print("自动化测试进行中");
    '''

if __name__ == '__main__':
    unittest.main()