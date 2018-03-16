"""
Created on 2018年3月7日

@author: 王贝贝 89144029
"""


from selenium.webdriver.common.by import By
from page_obj.menu_page import menu
# from page_com.CommonControl import CommonControl
from page_com.ExtendControlTable import ExtendControlTable
from time import sleep


class CreateOrder(menu, ExtendControlTable):

    """
    商务下单页面
    """
    # 下单页面的iframe
    new_order_xpath_loc = (By.XPATH, "//iframe[contains(@src,'/orf/order/businessOrder.shtml?')]")

    # ‘选择商机’、‘新建商机’操作按钮
    new_order_choose_business_btn_loc = (By.XPATH, "//a[@onclick='chooseBusiness()']")
    new_order_new_business_btn_loc = (By.XPATH, "//a[@href='/bus/newBusiness/toAdd.shtml?pageFrom=order']")

    # 选择商机相关参数
    new_order_choose_business_table_loc = (By.ID, 'myTable')                                # 商机表
    new_order_choose_business_filter_condition_loc = (By.ID, 'keyword')                    # 商机过滤条件

    new_order_choose_business_search_btn_loc = (By.XPATH, "//button[@onclick='submitBusParam()']")
    new_order_choose_business_save_btn_loc = (By.LINK_TEXT, "保存")
    new_order_choose_business_cancel_btn_loc = (By.LINK_TEXT, "取消")

    # 借贷人相关参数
    new_order_loans_table_loc = (By.ID, "loansTable")                               # 借贷人信息表

    new_order_loans_table_lender_status_loc = (By.NAME, "lenderStatus")             # 借贷人身份
    new_order_loans_table_name_loc = (By.NAME, "name")                              # 借贷人姓名
    new_order_loans_table_id_card_loc = (By.NAME, "idCard")                         # 借贷人身份证号码
    new_order_loans_table_no_loc = (By.NAME, "no")                                  # 借贷人联系电话
    new_order_loans_table_marital_status_loc = (By.NAME, "maritalStatus")           # 借贷人婚姻状况
    new_order_loans_table_children_num_loc = (By.NAME, "childrenNum")               # 借贷人子女情况
    new_order_loans_table_no_know_loc = (By.NAME, "noKnow")                         # 借贷人家属是否知晓
    new_order_loans_table_relationship_of_cus_loc = (By.NAME, "relationshipOfCus")  # 借贷人与主借贷人关系
    new_order_loans_table_is_self_loc = (By.NAME, "isSelf")                         # 借贷人是否是客户本人

    new_order_loans_table_add_loc = (By.LINK_TEXT, "新增一行")                       # 新增一个借贷人
    new_order_loans_table_delete_loc = (By.LINK_TEXT, "删除")                       # 删除一行

    # 合同约定相关参数
    new_order_loans_amount_loc = (By.ID, "loansAmountId")                           # 贷款金额
    new_order_loans_num_loc = (By.ID, "loansNumId")                                 # 贷款年限
    new_order_loans_interest_loc = (By.ID, "loansInterestId")                       # 贷款利息
    new_order_loans_rate_type_loc = (By.ID, "loansRateTypeId")                      # 贷款利息类型
    new_order_earnest_money_loc = (By.ID, "earnestMoneyId")                         # 定金

    # 办理业务相关参数
    new_order_business_table_loc = (By.ID, "orderBusinesId")                        # 业务信息表

    new_order_business_table_bt_name_loc = (By.NAME, "btName")                      # 业态名称
    new_order_business_table_product_loc = (By.NAME, "productName")                 # 产品
    new_order_business_table_service_charge_loc = (By.NAME, "serviceCharge")        # 手续费
    new_order_business_table_rate_type_loc = (By.NAME, "rateType")                  # 利率方式
    new_order_business_table_loans_amount_loc = (By.NAME, "loansAmount")            # 贷款额度(万)
    new_order_business_table_contract_no_loc = (By.NAME, "contractNo")              # 合同编号
    new_order_business_table_chanel_loc = (By.NAME, "channel")                      # 建议渠道

    new_order_business_table_flow_user_name_loc = (By.NAME, 'flowUserName')         # 流程人员
    # 流程人员下拉框
    new_order_flow_user_name_loc = (By.XPATH, "./descendant::span[contains(@id,'flowUserName')]")
    # 流程人员过滤输入框
    new_order_flow_user_name_filter_loc = (By.XPATH, "./following::input[@class='select2-search__field']")
    # 流程人员过滤结果
    new_order_flow_user_name_result_loc = (By.XPATH, "./following::li[contains(@class,'select2-results__option')]")

    new_order_business_table_add_loc = (By.LINK_TEXT, "新增一行")                    # 新增一个业务
    new_order_business_table_delete_loc = (By.LINK_TEXT, "删除")                    # 删除一行

    # 产品相关参数
    new_order_product_table_loc = (By.ID, 'productTable')                           # 产品表

    new_order_product_bt_name_loc = (By.ID, 'btId')                                 # 过滤条件业务名称
    new_order_product_name_loc = (By.ID, 'productId')                               # 过滤条件产品名称
    new_order_product_channel_loc = (By.ID, 'channelList')                          # 过滤条件渠道

    new_order_product_search_btn_loc = (By.XPATH, "//button[@onclick='submitBusParam()']")
    new_order_product_save_btn_loc = (By.LINK_TEXT, "保存")
    new_order_product_cancel_btn_loc = (By.LINK_TEXT, "取消")

    # 抵押物地址参数
    new_order_mortgage_address_loc = (By.ID, "mortgageAddress")                     # 抵押物地址

    # 包装费相关参数
    new_order_subject_table_loc = (By.ID, "subjectId")                              # 包装费用信息表

    new_order_subject_table_name_loc = (By.NAME, "subjectName")                       # 包装费用科目
    new_order_subject_table_num_loc = (By.NAME, "subjectNum")                         # 包装费用数量
    new_order_subject_table_price_loc = (By.NAME, "subjectPrice")                     # 包装费用价格
    new_order_subject_table_contract_no_loc = (By.NAME, "subjectContractNo")          # 包装费用合同

    new_order_subject_table_add_loc = (By.LINK_TEXT, "新增一行")                     # 新增一个业务
    new_order_subject_table_delete_loc = (By.LINK_TEXT, "删除")                     # 删除一行

    # 客户属性相关参数
    new_order_attr_editor_btn_loc = (By.LINK_TEXT, "编辑")                          # 编辑客户属性按钮
    new_order_attr_save_btn_loc = (By.LINK_TEXT, "保存")                            # 保存客户属性按钮
    new_order_attr_cancel_btn_loc = (By.LINK_TEXT, "取消")                          # 取消客户属性按钮

    # 客户资料相关参数
    new_order_cus_data_chooser_btn_loc = (By.LINK_TEXT, "选择资料")                  # 选择客户资料按钮
    new_order_cus_data_save_btn_loc = (By.LINK_TEXT, "保存")                        # 保存客户资料按钮
    new_order_cus_data_cancel_btn_loc = (By.LINK_TEXT, "取消")                      # 取消客户资料按钮

    # ‘提交审核’按钮
    new_order_submit_audit_btn_loc = (By.XPATH, "//button[@onclick='this.disabled=true;saveOrder(this);']")

    # ‘暂存’按钮
    new_order_save_temp_btn_loc = (By.XPATH, "//button[@onclick='this.disabled=true;saveOrderTemp(this);']")

    # ‘取消’按钮history.go(-1)
    new_order_cancel_btn_loc = (By.XPATH, "//button[@onclick='history.go(-1)']")

    # 下拉框的二次封装
    def Set_Selects(self, main_loc, select_title, Celement=None):
        select_loc = (By.XPATH, "//option[contains(text(),'%s')]" % select_title)
        self.Set_Droplist(main_loc, select_loc, select_title, Celement=Celement)

    # 具体字段的封装
    # 借贷人具体字段的封装
    # 设置借贷人身份
    def Set_SelectLenderStatus(self, lender_element, lender_status_value):
        self.Set_Selects(self.new_order_loans_table_lender_status_loc, lender_status_value, Celement=lender_element)

    # 设置借贷人姓名
    def Set_InputLenderName(self, lender_element, lender_name_value):
        self.Set_input(self.new_order_loans_table_name_loc, inputtext=lender_name_value,
                       Celement=lender_element)

    # 设置借贷人身份证号码
    def Set_InputLenderIdCard(self, lender_element, lender_id_card_value):
        self.Set_input(self.new_order_loans_table_id_card_loc, inputtext=lender_id_card_value,
                       Celement=lender_element)

    # 设置借贷人联系电话
    def Set_InputLenderNo(self, lender_element, lender_no_value):
        self.Set_input(self.new_order_loans_table_no_loc, inputtext=lender_no_value,
                       Celement=lender_element)

    # 设置借贷人婚姻状况
    def Set_SelectLenderMaritalStatus(self, lender_element, lender_marital_status_value):
        self.Set_Selects(self.new_order_loans_table_marital_status_loc, lender_marital_status_value,
                         Celement=lender_element)

    # 设置借贷人子女情况
    def Set_InputLenderChildrenNum(self, lender_element, lender_children_num_value):
        self.Set_input(self.new_order_loans_table_children_num_loc, inputtext=lender_children_num_value,
                       Celement=lender_element)

    # 设置借贷人家属是否知晓
    def Set_SelectLenderNoKnow(self, lender_element, lender_no_know_value):
        self.Set_Selects(self.new_order_loans_table_no_know_loc, lender_no_know_value, Celement=lender_element)

    # 设置借贷人与主借贷人关系
    def Set_SelectLenderRelationshipOfCus(self, lender_element, lender_relationship_of_cus_value):
        self.Set_Selects(self.new_order_loans_table_relationship_of_cus_loc, lender_relationship_of_cus_value,
                         Celement=lender_element)

    # 设置借贷人是否是客户本人
    def Set_SelectLenderIsSelf(self, lender_element, lender_is_self_value):
        self.Set_Selects(self.new_order_loans_table_is_self_loc, lender_is_self_value, Celement=lender_element)

    # 设置第N个借贷人信息
    def Set_TableLender(self, lender_num, lender_info_list=['主借贷人', '第一个借贷人', '429001198702060001',
                                                            '13708010001', '已婚', '1', '知晓', '本人', '是']):
        # 如果当前设置的不是第一个借贷人，则需要先点击新增一行按钮
        if lender_num > 1:
            lender_add_row = self.Select_TableRowByRowNum(table_loc=self.new_order_loans_table_loc,
                                                          table_row_num=-1)
            lender_add = self.Select_TableControlByControlLoc(table_element=lender_add_row,
                                                              control_loc=self.new_order_loans_table_add_loc)
            lender_add.click()
        # 获取当前列表行
        lender_info_row = self.Select_TableRowByRowNum(table_loc=self.new_order_loans_table_loc,
                                                       table_row_num=lender_num + 1)
        # 设置借贷人身份
        if lender_info_list[0] != '' or lender_info_list[0] != '主借贷人':
            self.Set_SelectLenderStatus(lender_info_row, lender_info_list[0])
        # 设置借贷人姓名
        if lender_info_list[1] != '':
            self.Set_InputLenderName(lender_info_row, lender_info_list[1])
        # 设置借贷人身份证号码
        if lender_info_list[2] != '':
            self.Set_InputLenderIdCard(lender_info_row, lender_info_list[2])
        # 设置借贷人联系电话
        if lender_info_list[3] != '':
            self.Set_InputLenderNo(lender_info_row, lender_info_list[3])
        # 设置借贷人婚姻状况
        if lender_info_list[4] != '' or lender_info_list[4] != '未婚':
            self.Set_SelectLenderMaritalStatus(lender_info_row, lender_info_list[4])
        # 设置借贷人子女情况
        if lender_info_list[5] != '':
            self.Set_InputLenderChildrenNum(lender_info_row, lender_info_list[5])
        # 设置借贷人家属是否知晓
        if lender_info_list[6] != '':
            self.Set_SelectLenderNoKnow(lender_info_row, lender_info_list[6])
        # 设置借贷人与主借贷人关系
        if lender_info_list[7] != '':
            self.Set_SelectLenderRelationshipOfCus(lender_info_row, lender_info_list[7])
        # 设置借贷人是否是客户本人
        if lender_info_list[8] != '':
            self.Set_SelectLenderIsSelf(lender_info_row, lender_info_list[8])

    # 删除第N个借贷人
    def Delete_TableLender(self, lender_num):
        # 第1个借贷人不能删除
        if lender_num > 1:
            lender_delete_row = self.Select_TableRowByRowNum(table_loc=self.new_order_loans_table_lender_status_loc,
                                                             table_row_num=lender_num + 1)
            lender_delete_col = self.Select_TableColByColNum(lender_delete_row, -1)
            lender_delete = self.Select_TableControlByControlLoc(lender_delete_col,
                                                                 self.new_order_loans_table_delete_loc)
            lender_delete.click()
        else:
            print('第1个借贷人不能删除')

    # 设置合同约定相关参数
    # 设置贷款金额
    def Set_InputLoansAmount(self, loans_amount_value='36'):
        self.Set_input(self.new_order_loans_amount_loc, loans_amount_value)

    # 设置贷款年限
    def Set_InputLoansNum(self, loans_num_value='10'):
        self.Set_input(self.new_order_loans_num_loc, loans_num_value)

    # 设置贷款利息
    def Set_InputLoansInterest(self, loans_interest_value='1'):
        self.Set_input(self.new_order_loans_interest_loc, loans_interest_value)

    # 设置贷款利息类型
    def Set_SelectLoansRateType(self, loans_rate_type="日息"):
        self.Set_Selects(self.new_order_loans_rate_type_loc, loans_rate_type)

    # 设置定金
    def Set_InputEarnestMoney(self, earnest_money='3600'):
        self.Set_input(self.new_order_earnest_money_loc, earnest_money)

    # 选择产品信息具体字段的封装
    # 设置搜索条件业务名称
    def Set_SelectFilterConditionBtName(self, bt_name_value):
        self.Set_Selects(self.new_order_product_bt_name_loc, bt_name_value)

    # 设置搜索条件产品名称
    def Set_SelectFilterConditionProductName(self, product_name_value):
        self.Set_Selects(self.new_order_product_name_loc, product_name_value)

    # 设置搜索条件渠道
    def Set_SelectFilterConditionChannel(self, product_channel_value):
        self.Set_Selects(self.new_order_product_channel_loc, product_channel_value)

    # 设置‘搜索’操作按钮
    def Set_ButtonProductSearch(self):
        self.Set_Button(self.new_order_product_search_btn_loc)

    # 设置‘保存’操作按钮
    def Set_ButtonProductSave(self):
        self.Set_Button(self.new_order_product_save_btn_loc)

    # 设置‘取消’操作按钮
    def Set_ButtonProductCancel(self):
        self.Set_Button(self.new_order_product_cancel_btn_loc)

    # 选择产品
    def Set_ProductName(self, product_index=2, product_filter_condition_list=['', '', '']):
        # 按过滤条件查找
        if product_filter_condition_list[0] != '':
            # 设置过滤条件
            self.Set_SelectFilterConditionBtName(product_filter_condition_list[0])
            if product_filter_condition_list[1] != '':
                self.Set_SelectFilterConditionProductName(product_filter_condition_list[1])
                if product_filter_condition_list[2] != '':
                    self.Set_SelectFilterConditionChannel(product_filter_condition_list[2])
            # 点击‘搜索’操作按钮
            self.Set_ButtonProductSearch()
            sleep(5)
        # 选择第N条产品
        product_row = self.Select_TableRowByRowNum(table_loc=self.new_order_product_table_loc,
                                                   table_row_num=product_index)
        self.Select_CheckboxTableRow(product_row)

    # 业务信息具体字段的封装
    # 设置业态名称
    def Set_SelectBusinessBtName(self, business_element, business_bt_name_value):
        self.Set_Selects(self.new_order_business_table_bt_name_loc, business_bt_name_value,
                         Celement=business_element)

    # 设置产品
    def Set_InputBusinessProduct(self, business_element, business_index, business_bt_name_value='',
                                 business_product_name_value='', business_channel_value=''):
        self.Set_Button(self.new_order_business_table_product_loc, Celement=business_element)
        sleep(8)
        self.Set_ProductName(product_index=business_index, product_filter_condition_list=[business_bt_name_value,
                                                                                          business_product_name_value,
                                                                                          business_channel_value])
        sleep(1)

    # 设置手续费
    def Set_InputBusinessServiceCharge(self, business_element, business_service_charge_value):
        self.Set_input(self.new_order_business_table_service_charge_loc, inputtext=business_service_charge_value,
                       Celement=business_element)

    # 设置利率方式
    def Set_SelectBusinessRateType(self, business_element, business_rate_type_value):
        self.Set_Selects(self.new_order_business_table_rate_type_loc, business_rate_type_value,
                         Celement=business_element)

    # 设置贷款额度(万)
    def Set_InputBusinessLoansAmount(self, business_element, business_loans_amount_value):
        self.Set_input(self.new_order_business_table_loans_amount_loc, inputtext=business_loans_amount_value,
                       Celement=business_element)

    # 设置合同编号
    def Set_InputBusinessContractNo(self, business_element, business_contract_no_value):
        self.Set_input(self.new_order_business_table_contract_no_loc, inputtext=business_contract_no_value,
                       Celement=business_element)

    # 设置建议渠道
    def Set_SelectBusinessChanel(self, business_element, business_chanel_index):
        self.Set_SelectByIndex(self.new_order_business_table_chanel_loc, select_list_index=business_chanel_index,
                               Celement=business_element)

    # 设置流程人员
    def Set_SelectLenderFlowUserName(self, business_element, business_flow_user_name_value='',
                                     business_flow_user_index=1):
        if business_flow_user_name_value != '':
            self.Set_InputSelect(self.new_order_flow_user_name_loc, self.new_order_flow_user_name_filter_loc,
                                 self.new_order_flow_user_name_result_loc, SelectText=business_flow_user_name_value,
                                 Celement=business_element)
        else:
            self.Set_SelectByIndex(self.new_order_business_table_flow_user_name_loc, business_flow_user_index)

    # 设置第N个业务信息
    def Set_TableBusiness(self, business_num, business_info_list=[]):
        # 如果当前设置的不是第一个业务，则需要先点击新增一行按钮
        if business_num > 1:
            business_add_row = self.Select_TableRowByRowNum(table_loc=self.new_order_business_table_loc,
                                                            table_row_num=-1)
            business_add = self.Select_TableControlByControlLoc(table_element=business_add_row,
                                                                control_loc=self.new_order_business_table_add_loc)
            business_add.click()
        # 获取当前列表行
        business_info_row = self.Select_TableRowByRowNum(table_loc=self.new_order_business_table_loc,
                                                         table_row_num=business_num + 1)
        # 设置业态名称
        if business_info_list[0] != '':
            self.Set_SelectBusinessBtName(business_info_row, business_info_list[0])
        # 设置产品
        if business_info_list[1] != '':
            business_product_index = int(business_info_list[1])
            self.Set_InputBusinessProduct(business_info_row, business_product_index,
                                          business_bt_name_value=business_info_list[0])
            self.Set_ButtonProductSave()
            sleep(2)
        # 设置手续费
        if business_info_list[2] != '':
            self.Set_InputBusinessServiceCharge(business_info_row, business_info_list[2])
        # 设置利率方式
        if business_info_list[3] != '':
            self.Set_SelectBusinessRateType(business_info_row, business_info_list[3])
        # 设置贷款额度(万)
        if business_info_list[4] != '':
            self.Set_InputBusinessLoansAmount(business_info_row, business_info_list[4])
        # 设置合同编号
        if business_info_list[5] != '':
            self.Set_InputBusinessContractNo(business_info_row, business_info_list[5])
        # 设置建议渠道
        if business_info_list[6] != '':
            business_channel_index = int(business_info_list[6])
            self.Set_SelectBusinessChanel(business_info_row, business_channel_index)
        # 设置流程人员
        if business_info_list[7] != '':
            if len(business_info_list[7]) < 3:
                business_flow_user_index = int(business_info_list[7])
                self.Set_SelectLenderFlowUserName(business_info_row, business_flow_user_index=business_flow_user_index)
            else:
                self.Set_SelectLenderFlowUserName(business_info_row,
                                                  business_flow_user_name_value=business_info_list[7])

    # 删除第N个业务信息
    def Delete_TableBusiness(self, business_num):
        # 第1个业务信息不能删除
        if business_num > 1:
            business_delete_row = self.Select_TableRowByRowNum(table_loc=self.new_order_loans_table_lender_status_loc,
                                                               table_row_num=business_num + 1)
            business_delete_col = self.Select_TableColByColNum(business_delete_row, -1)
            business_delete = self.Select_TableControlByControlLoc(business_delete_col,
                                                                   self.new_order_business_table_delete_loc)
            business_delete.click()
        else:
            print('第1个业务信息不能删除')

    # 设置抵押物地址
    def Set_InputMortgageAddress(self, mortgage_address_value='抵押物地址'):
        self.Set_input(self.new_order_mortgage_address_loc, mortgage_address_value)

    # 科目包装费用信息具体字段的封装
    # 设置包装费用科目
    def Set_SelectSubjectName(self, subject_element, subject_name_value):
        self.Set_Selects(self.new_order_subject_table_name_loc, subject_name_value,
                         Celement=subject_element)

    # 设置包装费用数量
    def Set_InputSubjectNum(self, subject_element, subject_num_value):
        self.Set_input(self.new_order_subject_table_num_loc, inputtext=subject_num_value,
                       Celement=subject_element)

    # 设置包装费用价格
    def Set_InputSubjectPrice(self, subject_element, subject_price_value):
        self.Set_input(self.new_order_subject_table_price_loc, inputtext=subject_price_value,
                       Celement=subject_element)

    # 设置包装费用合同
    def Set_InputSubjectContractNo(self, subject_element, subject_contract_no_value):
        self.Set_input(self.new_order_subject_table_contract_no_loc, inputtext=subject_contract_no_value,
                       Celement=subject_element)

    # 设置第N个科目包装费用
    def Set_TableSubject(self, subject_num, subject_info_list=[]):
        # 如果当前设置的不是第一个科目包装费用，则需要先点击新增一行按钮
        if subject_num > 1:
            subject_add_row = self.Select_TableRowByRowNum(table_loc=self.new_order_subject_table_loc, table_row_num=-1)
            subject_add = self.Select_TableControlByControlLoc(table_element=subject_add_row,
                                                               control_loc=self.new_order_subject_table_add_loc)
            subject_add.click()
        # 获取当前列表行
        subject_info_row = self.Select_TableRowByRowNum(table_loc=self.new_order_subject_table_loc,
                                                        table_row_num=subject_num + 1)
        # 设置包装费用科目
        if subject_info_list[0] != '':
            self.Set_SelectSubjectName(subject_info_row, subject_info_list[0])
        # 设置包装费用数量
        if subject_info_list[1] != '':
            self.Set_InputSubjectNum(subject_info_row, subject_info_list[1])
        # 设置包装费用价格
        if subject_info_list[2] != '':
            self.Set_InputSubjectPrice(subject_info_row, subject_info_list[2])
        # 设置包装费用合同
        if subject_info_list[3] != '':
            self.Set_InputSubjectContractNo(subject_info_row, subject_info_list[3])

    # 删除第N个科目包装费用
    def Delete_TableSubject(self, subject_num):
        # 第1个科目包装费用信息不能删除
        if subject_num > 1:
            subject_delete_row = self.Select_TableRowByRowNum(table_loc=self.new_order_subject_table_loc,
                                                              table_row_num=subject_num + 1)
            subject_delete_col = self.Select_TableColByColNum(subject_delete_row, -1)
            subject_delete = self.Select_TableControlByControlLoc(subject_delete_col,
                                                                  self.new_order_subject_table_delete_loc)
            subject_delete.click()
        else:
            print('第1个科目包装费用信息不能删除')

    # 设置客户属性
    # 设置‘编辑’操作按钮
    def Set_ButtonCusAttrEdit(self):
        self.Set_Button(self.new_order_attr_editor_btn_loc)

    # 设置‘保存’操作按钮
    def Set_ButtonCusAttrSave(self):
        self.Set_Button(self.new_order_attr_save_btn_loc)

    # 设置‘取消’操作按钮
    def Set_ButtonCusAttrCancel(self):
        self.Set_Button(self.new_order_attr_cancel_btn_loc)

    # 设置客户资料
    # 设置‘选择资料’操作按钮
    def Set_ButtonCusDataEdit(self):
        self.Set_Button(self.new_order_cus_data_chooser_btn_loc)

    # 设置‘保存’操作按钮
    def Set_ButtonCusDataSave(self):
        self.Set_Button(self.new_order_cus_data_save_btn_loc)

    # 设置‘取消’操作按钮
    def Set_ButtonCusDataCancel(self):
        self.Set_Button(self.new_order_cus_data_cancel_btn_loc)

    # 设置'提交审核'操作按钮
    def Set_ButtonOrderSubmitAudit(self):
        self.Set_Button(self.new_order_submit_audit_btn_loc)

    # 设置'暂存'操作按钮
    def Set_ButtonOrderSaveTemp(self):
        self.Set_Button(self.new_order_save_temp_btn_loc)

    # 设置'取消'操作按钮
    def Set_ButtonOrderCancel(self):
        self.Set_Button(self.new_order_cancel_btn_loc)

    # 商机点击下单进入下单页面，需要切换windows句柄
    def WindowsHandle_CreateOrder(self):
        # 获取当前主窗口，并切换至新打开页签
        current_main_windows = self.Getmainwindows()
        self.switch_windows(current_main_windows)

    # 设置'选择商机'操作按钮
    def Set_ButtonOrderChooseBusiness(self):
        self.Set_Button(self.new_order_choose_business_btn_loc)

    # 选择商机信息具体字段的封装
    # 设置商机搜索条件
    def Set_InputFilterCondition(self, filter_condition_value):
        self.Set_input(self.new_order_choose_business_filter_condition_loc, inputtext=filter_condition_value)

    # 设置‘搜索’操作按钮
    def Set_ButtonBusinessSearch(self):
        self.Set_Button(self.new_order_choose_business_search_btn_loc)

    # 设置‘保存’操作按钮
    def Set_ButtonBusinessSave(self):
        self.Set_Button(self.new_order_choose_business_save_btn_loc)

    # 设置‘取消’操作按钮
    def Set_ButtonBusinessCancel(self):
        self.Set_Button(self.new_order_choose_business_cancel_btn_loc)

    # 从订单-下单菜单进入下单页面，需要选择商机
    def Set_ChooseBusiness(self, business_filter_condition=''):
        # 点击选择商机
        self.Set_ButtonOrderChooseBusiness()
        sleep(5)

        # 按过滤条件查找
        if business_filter_condition != '':
            # 设置过滤条件
            self.Set_InputFilterCondition(business_filter_condition)
            # 点击‘搜索’操作按钮
            self.Set_ButtonBusinessSearch()
            sleep(2)
        # 选择第1条产品
        business_row = self.Select_TableRowByRowNum(table_loc=self.new_order_choose_business_table_loc, table_row_num=2)
        self.Select_CheckboxTableRow(business_row)

    # 进入下单页面，iframe有变动
    def Iframe_CreateOrder(self):
        if self.IS_element_present(self.new_order_xpath_loc):
            new_order_frame = self.find_element(*self.new_order_xpath_loc)
            self.switch_frame(new_order_frame)
            return True
        else:
            print("找不到 %s" % self.new_order_xpath_loc, "停止测试")
            return False

    # 从订单-下单菜单进入下单页面，需要切换iframe
    def CreateOrderByOrderMenu(self, login_type=1, user_name='51376245', password='666666'):
        self.menu_PreOrder(login_type, user_name, password)
        return self.Iframe_CreateOrder()

    # 从商机-跟进中菜单选择商机，点击下单，进入下单页面，需要切换iframe
    def CreateOrderByBusiness(self):
        self.WindowsHandle_CreateOrder()
        return self.Iframe_CreateOrder()