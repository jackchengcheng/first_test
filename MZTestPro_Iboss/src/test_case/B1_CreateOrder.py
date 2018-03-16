'''
Created on 2018年2月22日

@author: fanzhaoni
'''
import unittest
from time import sleep
import random
from models import myunit,function
from page_obj.CreateOrder_page import CreateOrder
from DataDriver.ReadEXLEFile import ReadEXLEFile
from _sqlite3 import Row
from page_obj.base import Page

TYPE = 1     #"1,表示调试；2,表示正式"

class CrOrderTest(myunit.MyTest):
    '''法律IBOSS商务新增商机测试'''
    
    def tearDown(self):
        #用例执行完成后暂时不用退出，下一个用例需要云用本次用例的结果
        pass
    
        
    #测试商务进入谈单下单页面
    def Business_CreateOrder(self):
        self.page_CreateOrder = CreateOrder(self.driver)
        self.page_CreateOrder.BusinessCreateOrder("4222787","a123")

    
    
    def test_BusinessCheck(self):
        '''新增订单'''
        '''(1)点击"新增订单"按钮，进入商机验证页面
           (2)填写用户信息，进入正式下单页面
           (3)填写订单信息，确认下单 '''
         
         

        #读取用户及订单信息
        filepath = function.Get_datafilepath("Order.xls")
        TestFile = ReadEXLEFile(filepath)
        tables =TestFile.excel_table_byindex()
        
        #进入谈单下单菜单
        self.Business_CreateOrder()
        Infors = []
        if TYPE != 2:
            Infors.append(tables[1])
        else:
            Infors = tables
            
        
        page_Order = self.page_CreateOrder
        for infor in Infors:
            sleep(3)
            #(1)点击"新增订单"按钮，进入商机验证页面
            page_Order.NewOrder()
            function.insert_img(self.driver, "BusinessCheck.jpg")
            self.assertIn("display: block",page_Order.NewOrder_Windows(), "新增订单弹出框未显示")
        
        
            #(2)填写用户信息，进入正式下单页面
            print('订单信息如下：')
            print(infor)
            
            page_Order.SetCustomerinfo(infor['客户电话'], infor['客户姓名']) 
            function.insert_img(self.driver, "NewOrder.jpg") 

            
            #(3)填写订单信息，确认下单
            page_Order.Interface_NewOrder()
            page_Order.Set_loanamount(infor['预计贷款金额(万)'],infor['期望利率(%)'],infor['贷款期数'])
            page_Order.Set_repayment_method(infor['还款方式'])
            sleep(1)
            page_Order.Set_big_category(infor['业务大类'])
            sleep(1)
            #is否是组合
            if infor['业务大类']!="组合业务":
                page_Order.Set_small_category(infor['业务小类'])
                #添加产品（后期需要补充）
                sleep(2)
                if infor['业务小类']=="一抵":
                    page_Order.Set_advance(infor['是否需要垫资'])
                    if infor['是否需要垫资'] =="是":
                       page_Order.Set_advaceInfor(infor['垫资金额(万)'],infor['垫资利率(%)'],infor['垫资时间(天)'])
                page_Order.Set_contractinfor(infor['合同编号'], infor['合同比例(%)'])
                page_Order.Set_packing_charge(infor['包装费用(元)'])
                #下单时间（后期需要补充）
                page_Order.Set_process_personnel(infor['流程人员'])
                page_Order.Set_assist_personnel(infor['协单人员'])
                page_Order.Set_remarks(infor['备注'])
                
            else:
                for subIndex in [1,2]:
                    sleep(1)
                    page_Order.Set_G_big_category(subIndex-1,infor['业务大类%d' % subIndex])
                    sleep(1)
                    page_Order.Set_G_small_category(subIndex-1,infor['业务小类%d' % subIndex])
                    #添加产品（后期需要补充）
                    sleep(2)
                    if infor['业务小类%d' % subIndex]=="一抵":
                        page_Order.Set_G_advance(subIndex-1,infor['是否需要垫资%d' % subIndex])
                        if infor['是否需要垫资%d' % subIndex] =="是":
                           page_Order.Set_G_advaceInfor(subIndex-1,infor['垫资金额(万)%d' % subIndex],infor['垫资利率(%%)%d' % subIndex],infor['垫资时间(天)%d' % subIndex])
                    page_Order.Set_G_contractinfor(subIndex-1,infor['合同编号%d' % subIndex], infor['合同比例(%%)%d' % subIndex])
                    page_Order.Set_G_packing_charge(subIndex-1,infor['包装费用(元)%d' % subIndex])
                    #下单时间（后期需要补充）
                    page_Order.Set_G_process_personnel(subIndex-1,infor['流程人员%d' % subIndex])
                    page_Order.Set_G_assist_personnel(subIndex-1,infor['协单人员%d' % subIndex])
                    sleep(1)
                    page_Order.Set_G_remarks(subIndex-1,infor['备注%d' % subIndex])

            page_Order.Set_card(infor["身份证号"])
            sleep(5)
            function.insert_img(self.driver, "Order_%s.jpg" % infor['客户姓名']) 
            page_Order.Save_Btn("确认签单")
        
        
        
if __name__ == "__main__":
    unittest.main()