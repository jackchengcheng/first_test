"""
Created on 2018年3月9日

@author: 王贝贝 89144029
"""

import unittest
from time import sleep
from models import myunit, function
from page_obj.FollowingBusiness_page import FollowingBusiness
from DataDriver.ReadEXLEFile import ReadEXLEFile

TYPE = 1     # 1,表示调试；2,表示正式


class FollowingBusinessTest(myunit.MyTest, FollowingBusiness):
    """
    IBOSS商务跟进中页面测试
    """
    
    def setUp(self):
        # 初始化浏览器
        myunit.MyTest.setUp(self)

        # 新建一个正确的商机
        pass

    def tearDown(self):
        # 用例执行完成后暂时不用退出，下一个用例需要云用本次用例的结果
        pass

    # 测试商务进入跟进中商机页面
    def Business_FollowingBusiness(self):
        self.page_FollowingBusiness = FollowingBusiness(self.driver, base_url='https://192.168.254.80:8037')
        return self.page_FollowingBusiness.FollowingBusiness(1, '51376245', '666666')

    # 读取跟进中商机测试数据
    def Get_FollowingBusinessTestCaseData(self, test_case_file_name):
        test_case_file_path = function.Get_datafilepath(test_case_file_name)
        test_file = ReadEXLEFile(test_case_file_path)
        tables = test_file.excel_table_byindex()
        infors = []

        if TYPE != 2:
            infors.append(tables[0])
        else:
            infors = tables
        return infors

    def test_FollowingBusinessSearch(self):

        """
        跟进中商机搜索功能测试:
        (1)"商机-跟进中"菜单，进入跟进中商机页面
        (2)填写商机过滤信息，确认搜索结果正确
        """
        # 读取跟进中商机测试数据
        f_business_infos = self.Get_FollowingBusinessTestCaseData("FollowingBusiness.xls")

        page_FollowingBusiness = self.Business_FollowingBusiness()

        page_order = self.Order_CreateOrder()
        for order_info in order_infos:
            sleep(2)

            if page_order:

        for infor in self.Infors:
            print("进入text",infor['用例标题'])
            function.insert_img(self.driver, "BusinessCheck.jpg")
            #self.assertIn("display: block",page_NewBusiness, "haha")
            # 进入新增商机菜单
            if page_NewBusiness:
                sleep(3)
                self.SelectContactWay(infor['联系方式'])                           # 联系方式
                self.InputContactNum(infor['联系号码'])                            # 联系号码
                self.ButtonSearch()                                               # 搜索
                sleep(3)
                self.InputcustomerName(infor['客户姓名'])                       # 客户姓名
                self.SelectBusinessType(infor['业态'])                          # 业态
                self.SelectAreaName(infor['区域'])                              # 区域
                self.InputLoanAmount(infor['贷款金额'])                         # 贷款金额
                self.InputIdCard(infor['身份证号码'])                           # 身份证号码
                self.InputBirthday(infor['生日'])                               # 生日
                self.InputAge(infor['年龄'])                                    # 年龄
                self.SelectSex(infor['性别'])                                   # 性别
                self.SelectResidence(infor['户口所在地'])                       # 户口所在地
                self.SelectMaritalStatus(infor['婚姻状态'])                     # 婚姻状态
                self.SelectEduBackground(infor['学历'])                         # 学历
                self.SelectLoanTime(infor['急需时间'])                          # 急需时间
                self.SelectLoanCycle(infor['贷款周期'])                         # 贷款周期
                self.SelectLoanInterrestRate(infor['利率要求'])                 # 利率要求
                self.SelectLoanRateValue(infor['利率值'])                       # 利率值
                self.SelectRepaymentType(infor['还款方式'])                     # 还款方式

            function.insert_img(self.driver, "Order_fanzhaonitest2.jpg")
            self.page_NewBusiness.ButtonSaveBusiness()
            self.page_NewBusiness.Message()
            function.insert_img(self.driver, "success.jpg" )
            sleep(2)
#
#         
#             #(2)填写用户信息，进入正式下单页面
#             print('订单信息如下：')
#             print(infor)
#             
#             page_Order.SetCustomerinfo(infor['客户电话'], infor['客户姓名']) 
#             function.insert_img(self.driver, "NewOrder.jpg") 
# 
#             
#             #(3)填写订单信息，确认下单
#             page_Order.Interface_NewOrder()
#             page_Order.Set_loanamount(infor['预计贷款金额(万)'],infor['期望利率(%)'],infor['贷款期数'])
#             page_Order.Set_repayment_method(infor['还款方式'])
#             sleep(1)
#             page_Order.Set_big_category(infor['业务大类'])
#             sleep(1)
#             #is否是组合
#             if infor['业务大类']!="组合业务":
#                 page_Order.Set_small_category(infor['业务小类'])
#                 #添加产品（后期需要补充）
#                 sleep(2)
#                 if infor['业务小类']=="一抵":
#                     page_Order.Set_advance(infor['是否需要垫资'])
#                     if infor['是否需要垫资'] =="是":
#                        page_Order.Set_advaceInfor(infor['垫资金额(万)'],infor['垫资利率(%)'],infor['垫资时间(天)'])
#                 page_Order.Set_contractinfor(infor['合同编号'], infor['合同比例(%)'])
#                 page_Order.Set_packing_charge(infor['包装费用(元)'])
#                 #下单时间（后期需要补充）
#                 page_Order.Set_process_personnel(infor['流程人员'])
#                 page_Order.Set_assist_personnel(infor['协单人员'])
#                 page_Order.Set_remarks(infor['备注'])
#                 
#             else:
#                 for subIndex in [1,2]:
#                     sleep(1)
#                     page_Order.Set_G_big_category(subIndex-1,infor['业务大类%d' % subIndex])
#                     sleep(1)
#                     page_Order.Set_G_small_category(subIndex-1,infor['业务小类%d' % subIndex])
#                     #添加产品（后期需要补充）
#                     sleep(2)
#                     if infor['业务小类%d' % subIndex]=="一抵":
#                         page_Order.Set_G_advance(subIndex-1,infor['是否需要垫资%d' % subIndex])
#                         if infor['是否需要垫资%d' % subIndex] =="是":
#                            page_Order.Set_G_advaceInfor(subIndex-1,infor['垫资金额(万)%d' % subIndex],infor['垫资利率(%%)%d' % subIndex],infor['垫资时间(天)%d' % subIndex])
#                     page_Order.Set_G_contractinfor(subIndex-1,infor['合同编号%d' % subIndex], infor['合同比例(%%)%d' % subIndex])
#                     page_Order.Set_G_packing_charge(subIndex-1,infor['包装费用(元)%d' % subIndex])
#                     #下单时间（后期需要补充）
#                     page_Order.Set_G_process_personnel(subIndex-1,infor['流程人员%d' % subIndex])
#                     page_Order.Set_G_assist_personnel(subIndex-1,infor['协单人员%d' % subIndex])
#                     sleep(1)
#                     page_Order.Set_G_remarks(subIndex-1,infor['备注%d' % subIndex])
# 
#             page_Order.Set_card(infor["身份证号"])
#             sleep(5)
#             function.insert_img(self.driver, "Order_%s.jpg" % infor['客户姓名']) 
#             page_Order.Save_Btn("确认签单")
#         
        
        
if __name__ == "__main__":
    unittest.main()