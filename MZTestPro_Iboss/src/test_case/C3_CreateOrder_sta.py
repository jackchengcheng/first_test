"""
Created on 2018年3月9日

@author: 王贝贝 89144029
"""

import unittest
from time import sleep
from models import myunit, function
from page_obj.CreateOrder_page import CreateOrder
from page_obj.CusInfo_page import EditCusInfo
from DataDriver.ReadEXLEFile import ReadEXLEFile

TYPE = 1     # 1,表示调试；2,表示正式


class CreateOrderTest(myunit.MyTest, CreateOrder, EditCusInfo):
    """
    IBOSS商务下单页面测试
    """

    def setUp(self):
        # 初始化浏览器
        myunit.MyTest.setUp(self)

        # 新建一个正确的商机
        pass

    def tearDown(self):
        # 用例执行完成后暂时不用退出，下一个用例需要云用本次用例的结果
        pass

    # 测试商务进入谈单下单页面
    def Order_CreateOrder(self):
        self.page_CreateOrder = CreateOrder(self.driver, base_url='https://192.168.254.80:8037')
        return self.page_CreateOrder.CreateOrderByOrderMenu(1, '51376245', '666666')

    # 读取下单测试数据
    def Get_OrderTestCaseData(self, test_case_file_name):
        test_case_file_path = function.Get_datafilepath(test_case_file_name)
        test_file = ReadEXLEFile(test_case_file_path)
        tables = test_file.excel_table_byindex()
        infors = []

        if TYPE != 2:
            infors.append(tables[0])
        else:
            infors = tables
        return infors

    # 读取下单_各个数据模块测试数据
    def Get_OrderDataModuleTestCaseData(self, test_case_file_name):
        test_case_file_path = function.Get_datafilepath(test_case_file_name)
        test_file = ReadEXLEFile(test_case_file_path)
        tables = test_file.excel_table_byindex()
        return tables

    # 设置借贷人数据
    def Set_Lender(self, lender_info_dict):
        if lender_info_dict['借贷人个数'] == '1':
            lender_info_list = [lender_info_dict['身份'], lender_info_dict['姓名'], lender_info_dict['身份证号码'],
                                lender_info_dict['联系电话'], lender_info_dict['婚姻状况'], lender_info_dict['子女情况'],
                                lender_info_dict['家属是否知晓'], lender_info_dict['与主借贷人关系'],
                                lender_info_dict['是否是客户本人']]
            self.Set_TableLender(lender_num=1, lender_info_list=lender_info_list)
        else:
            lender_status_list = lender_info_dict['身份'].split('|')
            lender_name_list = lender_info_dict['姓名'].split('|')
            lender_id_card_list = lender_info_dict['身份证号码'].split('|')
            lender_no_list = lender_info_dict['联系电话'].split('|')
            lender_marital_status_list = lender_info_dict['婚姻状况'].split('|')
            lender_children_num_list = lender_info_dict['子女情况'].split('|')
            lender_no_know_list = lender_info_dict['家属是否知晓'].split('|')
            lender_relationship_of_cus_list = lender_info_dict['与主借贷人关系'].split('|')
            lender_is_self_list = lender_info_dict['是否是客户本人'].split('|')
            lender_num = int(lender_info_dict['借贷人个数'])
            for lender_index in range(lender_num):
                lender_info_list = [lender_status_list[lender_index], lender_name_list[lender_index],
                                    lender_id_card_list[lender_index], lender_no_list[lender_index],
                                    lender_marital_status_list[lender_index], lender_children_num_list[lender_index],
                                    lender_no_know_list[lender_index], lender_relationship_of_cus_list[lender_index],
                                    lender_is_self_list[lender_index]]
                self.Set_TableLender(lender_num=lender_index + 1, lender_info_list=lender_info_list)

    # 设置合同约定数据
    def Set_Loan(self, loan_info_dict):
        self.Set_InputLoansAmount(loan_info_dict['贷款金额'])
        self.Set_InputLoansNum(loan_info_dict['贷款年限'])
        self.Set_InputLoansInterest(loan_info_dict['贷款利息'])
        self.Set_SelectLoansRateType(loan_info_dict['贷款利息方式'])
        self.Set_InputEarnestMoney(loan_info_dict['定金'])

    # 设置办理业务数据
    def Set_Business(self, business_info_dict):
        if business_info_dict['办理业务个数'] == '1':
            business_info_list = [business_info_dict['业务'], business_info_dict['产品'], business_info_dict['手续费'],
                                  business_info_dict['利率方式'], business_info_dict['贷款额度(万)'],
                                  business_info_dict['合同编号'], business_info_dict['建议渠道'],
                                  business_info_dict['流程人员']]
            self.Set_TableBusiness(business_num=1, business_info_list=business_info_list)
        else:
            business_bt_name_list = business_info_dict['业务'].split('|')
            business_product_list = business_info_dict['产品'].split('|')
            business_service_charge_list = business_info_dict['手续费'].split('|')
            business_rate_type_list = business_info_dict['利率方式'].split('|')
            business_loans_amount_list = business_info_dict['贷款额度(万)'].split('|')
            business_contract_no_list = business_info_dict['合同编号'].split('|')
            business_chanel_list = business_info_dict['建议渠道'].split('|')
            business_flow_user_name_list = business_info_dict['流程人员'].split('|')
            business_num = int(business_info_dict['办理业务个数'])
            for business_index in range(business_num):
                business_info_list = [business_bt_name_list[business_index], business_product_list[business_index],
                                      business_service_charge_list[business_index],
                                      business_rate_type_list[business_index],
                                      business_loans_amount_list[business_index],
                                      business_contract_no_list[business_index], business_chanel_list[business_index],
                                      business_flow_user_name_list[business_index]]
                self.Set_TableBusiness(business_num=business_index + 1, business_info_list=business_info_list)
        # 设置抵押物地址
        self.Set_InputMortgageAddress(business_info_dict['抵押物地址'])

    # 设置包装费数据
    def Set_Subject(self, subject_info_dict):
        if subject_info_dict['包装科目个数'] == '1':
            subject_info_list = [subject_info_dict['科目'], subject_info_dict['数量'], subject_info_dict['价格'],
                                 subject_info_dict['合同']]
            self.Set_TableSubject(subject_num=1, subject_info_list=subject_info_list)
        else:
            subject_name_list = subject_info_dict['科目'].split('|')
            subject_num_list = subject_info_dict['数量'].split('|')
            subject_price_list = subject_info_dict['价格'].split('|')
            subject_contract_no_list = subject_info_dict['合同'].split('|')
            subject_num = int(subject_info_dict['包装科目个数'])
            for subject_index in range(subject_num):
                subject_info_list = [subject_name_list[subject_index], subject_num_list[subject_index],
                                     subject_price_list[subject_index], subject_contract_no_list[subject_index]]
                self.Set_TableSubject(subject_num=subject_index + 1, subject_info_list=subject_info_list)

    # 设置客户属性数据
    def Set_CusAttr(self, cus_attr_info_dict):
        # 点击编辑操作按钮
        self.Set_ButtonCusAttrEdit()
        sleep(8)
        if cus_attr_info_dict['是否存在客户属性'] == '是':
            # 设置房产信息
            if cus_attr_info_dict['房产数'] == '0':
                print('该客户无房产信息')
            else:
                house_info_lists = cus_attr_info_dict['房产信息'].split('|')
                for house_index in range(len(house_info_lists)):
                    house_info_list = house_info_lists[house_index].split(',')
                    self.Set_House(house_index, house_info_list)
                    sleep(2)
            # 设置车辆信息
            if cus_attr_info_dict['车辆数'] == '0':
                print('该客户车辆信息')
            else:
                car_info_lists = cus_attr_info_dict['车辆信息'].split('|')
                for car_index in range(len(car_info_lists)):
                    car_info_list = car_info_lists[car_index].split(',')
                    self.Set_Car(car_index, car_info_list)
            # 设置保单信息
            if cus_attr_info_dict['保单信息'] == 'null':
                print('不设置保单信息')
            else:
                insurance_info_list = cus_attr_info_dict['保单信息'].split(',')
                self.Set_Insurance(insurance_info_list)
            # 设置工作信息
            if cus_attr_info_dict['工作信息'] == 'null':
                print('不设置工作信息')
            else:
                job_info_list = cus_attr_info_dict['工作信息'].split(',')
                self.Set_Job(job_info_list)
            # 设置社保信息
            if cus_attr_info_dict['社保信息'] == 'null':
                print('不设置社保信息')
            else:
                social_security_info_list = cus_attr_info_dict['社保信息'].split(',')
                self.Set_SocialSecurity(social_security_info_list)
            # 设置公积金信息
            if cus_attr_info_dict['公积金信息'] == 'null':
                print('不设置公积金信息')
            else:
                acc_fund_info_list = cus_attr_info_dict['公积金信息'].split(',')
                self.Set_AccFund(acc_fund_info_list)
            # 设置负债信息
            if cus_attr_info_dict['负债信息'] == 'null':
                print('不设置负债信息')
            else:
                liability_info_list = cus_attr_info_dict['负债信息'].split(',')
                self.Set_Liability(liability_info_list)
            # 设置信用卡信息
            if cus_attr_info_dict['信用卡信息'] == 'null':
                print('不设置信用卡信息')
            else:
                credit_card_info_list = cus_attr_info_dict['信用卡信息'].split(',')
                self.Set_CreditCard(credit_card_info_list)
            # 点击保存操作按钮
            self.Set_ButtonCusAttrSave()
            sleep(2)
        else:
            # 点击取消操作按钮
            self.Set_ButtonCusAttrCancel()
            sleep(2)

    # 设置客户资料数据
    def Set_CusData(self, cus_num, cus_data_info_dict):
        # 点击选择资料操作按钮
        self.Set_ButtonCusDataEdit()
        sleep(2)
        if cus_data_info_dict['是否存在客户资料'] == '是':
            cus_data_info_list = [cus_data_info_dict['工作证明'], cus_data_info_dict['房产证明'],
                                  cus_data_info_dict['婚姻证明'], cus_data_info_dict['身份证明'],
                                  cus_data_info_dict['其它资料']]
            cus_data_type_value_all_list = self.Set_CusDataClass(cus_data_info_list)
            # 点击保存操作按钮
            self.Set_ButtonCusDataSave()
            sleep(2)
            # 点击客户资料原件复印件
            self.Set_CusDataDatil(cus_num, cus_data_type_value_all_list)
            sleep(2)
        else:
            # 点击取消操作按钮
            self.Set_ButtonCusDataCancel()
            sleep(2)

    def test_BusinessCheck(self):
        """
        下单各输入项数据测试:
        (1)"订单-下单"菜单，进入下单页面
        (2)选择商机，进入正式下单页面
        (3)填写订单信息，确认下单
        """
        # 读取下单_借贷人测试数据
        lender_infos = self.Get_OrderDataModuleTestCaseData("OrderLender.xls")
        # 读取下单_合同约定测试数据
        loan_infos = self.Get_OrderDataModuleTestCaseData("OrderLoan.xls")
        # 读取下单_办理业务测试数据
        business_infos = self.Get_OrderDataModuleTestCaseData("OrderBusiness.xls")
        # 读取下单_包装费测试数据
        subject_infos = self.Get_OrderDataModuleTestCaseData("OrderSubject.xls")
        # 读取下单_客户属性测试数据
        cus_attr_infos = self.Get_OrderDataModuleTestCaseData("CusAttr.xls")
        # 读取下单_客户资料测试数据
        cus_data_infos = self.Get_OrderDataModuleTestCaseData("OrderCusData.xls")
        # 读取下单测试数据
        order_infos = self.Get_OrderTestCaseData("Order.xls")

        page_order = self.Order_CreateOrder()
        for order_info in order_infos:
            sleep(2)

            if page_order:
                # 选择商机
                self.Set_ChooseBusiness('')
                self.Set_ButtonBusinessSave()
                sleep(2)

                # 设置订单相关信息
                if order_info['借贷人'] != 'null':
                    lender_info_index = int(order_info['借贷人'])
                    self.Set_Lender(lender_infos[lender_info_index - 2])
                if order_info['合同约定'] != 'null':
                    loan_info_index = int(order_info['合同约定'])
                    self.Set_Loan(loan_infos[loan_info_index - 2])
                if order_info['办理业务'] != 'null':
                    business_info_index = int(order_info['办理业务'])
                    self.Set_Business(business_infos[business_info_index - 2])
                if order_info['包装费'] != 'null':
                    subject_info_index = int(order_info['包装费'])
                    self.Set_Subject(subject_infos[subject_info_index - 2])
                if order_info['客户属性'] != 'null':
                    cus_attr_info_index = int(order_info['客户属性'])
                    self.Set_CusAttr(cus_attr_infos[cus_attr_info_index - 2])
                if order_info['客户资料'] != 'null':
                    cus_data_info_index = int(order_info['客户资料'])
                    self.Set_CusData(int(lender_infos[int(order_info['借贷人']) - 2]['借贷人个数']),
                                     cus_data_infos[cus_data_info_index - 2])

                # 提交
                self.Set_ButtonOrderSubmitAudit()
        
if __name__ == "__main__":
    unittest.main()