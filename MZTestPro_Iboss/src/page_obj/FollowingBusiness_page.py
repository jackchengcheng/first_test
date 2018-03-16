"""
Created on 2018年3月15日

@author: 王贝贝 89144029
"""

from selenium.webdriver.common.by import By
from page_obj.menu_page import menu
from page_com.ExtendControlTable import ExtendControlTable


class FollowingBusiness(menu, ExtendControlTable):
    """
    跟进中商机页面
    """
    # 商机-跟进中页面的iframe
    f_business_xpath_loc = (By.XPATH, "//iframe[contains(@src,'/bus/list/followingIndex.shtml?')]")

    # 搜索区域
    f_business_search_div_loc = (By.XPATH, '@class="titleSearch"')
    # 过滤条件
    f_business_filter_condition_cus_name_loc = (By.ID, 'customerName')                  # 客户信息
    f_business_filter_condition_cus_attr_select_loc = (By.ID, 'cusAttr')                # 客户属性

    new_order_business_table_flow_user_name_loc = (By.NAME, 'flowUserName')         # 流程人员
    # 客户属性下拉框
    f_business_filter_condition_cus_attr_loc = (By.XPATH, "//input[@class='select2-search__field']")
    # 客户属性过滤结果
    f_business_filter_condition_cus_attr_result_loc = (By.XPATH, "//li[contains(@class,'select2-results__option')]")

    f_business_filter_condition_origin_code_loc = (By.ID, 'originCodeDiv')              # 来源渠道
    f_business_filter_condition_is_vip_loc = (By.ID, 'isVip')                           # 是否VIP
    f_business_filter_condition_start_loan_amount_loc = (By.ID, 'startLoanAmount')      # 贷款金额范围
    f_business_filter_condition_end_loan_amount_loc = (By.ID, 'endLoanAmount')          # 贷款金额范围
    f_business_filter_condition_business_stage_loc = (By.ID, 'businessStage')           # 销售阶段
    f_business_filter_condition_start_time_loc = (By.ID, 'startTime')                   # 新增日期范围
    f_business_filter_condition_end_time_loc = (By.ID, 'endTime')                       # 新增日期范围
    f_business_filter_condition_follow_s_time_loc = (By.ID, 'followSTime')              # 最后跟进时间范围
    f_business_filter_condition_follow_e_time_loc = (By.ID, 'followETime')              # 最后跟进时间范围
    f_business_filter_condition_n_follow_s_time_loc = (By.ID, 'startTime1')             # 下次跟进时间范围
    f_business_filter_condition_n_follow_e_time_loc = (By.ID, 'endTime1')               # 下次跟进时间范围
    f_business_filter_condition_way_code_loc = (By.ID, 'wayCode')                       # 接收方式
    f_business_filter_condition_reception_s_time_loc = (By.ID, 'receptionStartTime')    # 接收时间范围
    f_business_filter_condition_reception_e_time_loc = (By.ID, 'receptionEndTime')      # 接收时间间范围
    # 搜索按钮
    f_business_search_btn_loc = (By.XPATH, "//*[@onclick='reloadTableTrue();' and @text()='搜索']")

    # 操作按钮
    f_business_call_btn_loc = (By.XPATH, "//*[@onclick='openCallPage();' and @text()='打电话']")
    f_business_hide_btn_loc = (By.XPATH, "//*[@onclick='hideByBatch()'' and @text()='隐藏']")
    f_business_delete_btn_loc = (By.XPATH, "//*[@onclick='deleteByBatch()'' and @text()='剔除']")
    f_business_invalid_btn_loc = (By.XPATH, "//*[@onclick='invalidByBatch()'' and @text()='返无效']")
    f_business_change_group_btn_loc = (By.XPATH, "//*[@onclick='changeGroup()' and @text()='移动分组']")

    f_business_edit_group_btn_loc = (By.XPATH, "//*[contains(@onclick,'showEditLayer') and @text()='编辑分组']")
    f_business_new_group_btn_loc = (By.XPATH, "//*[@onclick='newGroup()' and @text()='新建分组']")

    f_business_today_following_link_loc = (By.XPATH, "//*[@onclick='onclickImport('todayFollowing');' and @text()='今日待跟进']")
    f_business_today_appointment_link_loc = (By.XPATH, "//*[@onclick='onclickImport('yysm');' and @text()='今日预约上门']")
    f_business_overdue_link_loc = (By.XPATH, "//*[@onclick='onclickImport('overdue');' and @text()='逾期跟进']")
    f_business_tomorrow_link_loc = (By.XPATH, "//*[@onclick='onclickImport('tomorrow');' and @text()='明天掉库']")
    f_business_two_day_link_loc = (By.XPATH, "//*[@onclick='onclickImport('twoDay');' and @text()='2天后掉库']")
    f_business_all_link_loc = (By.XPATH, "//*[@onclick='onclickImport('all');' and @text()='全部']")

    f_business_business_detail_link_loc = (By.XPATH, "./child::a[contains(@onclick,'openBusinessDetail')]")

    f_business_business_remark_link_loc = (By.XPATH, "./child::a[contains(@onclick,'openBusinessRemark') and "
                                                     "@title='备注']")
    f_business_business_send_msg_link_loc = (By.XPATH, "./child::a[contains(@onclick,'openSendMsgPage') and "
                                                       "@title='发短信']")
    f_business_business_order_link_loc = (By.XPATH, "./child::a[contains(@onclick,'openOrderPage') and @title='下单']")

    # 跟进中商机列表
    f_business_table_loc = (By.ID, 'businessList')
    f_business_right_table_loc = (By.XPATH, "//div[@class='DTFC_RightBodyLiner']/table")
    f_business_left_table_head_loc = (By.XPATH, "//div[@class='DTFC_LeftHeadWrapper']/table")
    f_business_left_table_loc = (By.XPATH, "//div[@class='DTFC_LeftBodyLiner']/table")

    # 下拉框的二次封装
    def Set_Selects(self, main_loc, select_title):
        select_loc = (By.XPATH, "//option[contains(text(),'%s')]" % select_title)
        self.Set_Droplist(main_loc, select_loc, select_title)

    # 设置过滤条件具体项
    # 设置客户信息
    def Set_InputCusName(self, cus_name_value):
        self.Set_input(self.f_business_filter_condition_cus_name_loc, cus_name_value)

    # 设置客户属性
    def Set_InputSelectCusAttr(self, cus_attr_value):
        self.Set_InputSelect(self.f_business_filter_condition_cus_attr_loc,
                             self.f_business_filter_condition_cus_attr_loc,
                             self.f_business_filter_condition_cus_attr_result_loc, cus_attr_value)

    # 设置来源渠道
    def Set_CascadeSelectOriginCode(self, origin_code_value):
        self.Set_CascadeSelect(self.f_business_filter_condition_origin_code_loc, origin_code_value)

    # 设置是否VIP
    def Set_SelectIsVip(self, is_vip_value):
        self.Set_Selects(self.f_business_filter_condition_is_vip_loc, is_vip_value)

    # 设置贷款金额范围
    def Set_InputLoanAmount(self, start_loan_amount_value, end_loan_amount_value):
        self.Set_input(self.f_business_filter_condition_start_loan_amount_loc, start_loan_amount_value)
        self.Set_input(self.f_business_filter_condition_end_loan_amount_loc, end_loan_amount_value)

    # 设置销售阶段
    def Set_SelectBusinessStage(self, business_stage_value):
        self.Set_Selects(self.f_business_filter_condition_business_stage_loc, business_stage_value)

    # 设置新增日期
    def Set_TimeAddTime(self, start_time_value, end_time_value):
        self.Set_input(self.f_business_filter_condition_start_time_loc, start_time_value)
        # 时间控件用完后必须要返回到所有操作的form下面
        self.find_element(*self.f_business_search_div_loc).click()
        self.Set_input(self.f_business_filter_condition_end_time_loc, end_time_value)
        # 时间控件用完后必须要返回到所有操作的form下面
        self.find_element(*self.f_business_search_div_loc).click()

    # 设置最后跟进时间
    def Set_TimeFollowTime(self, s_follow_time_value, e_follow_time_value):
        self.Set_input(self.f_business_filter_condition_follow_s_time_loc, s_follow_time_value)
        # 时间控件用完后必须要返回到所有操作的form下面
        self.find_element(*self.f_business_search_div_loc).click()
        self.Set_input(self.f_business_filter_condition_follow_e_time_loc, e_follow_time_value)
        # 时间控件用完后必须要返回到所有操作的form下面
        self.find_element(*self.f_business_search_div_loc).click()

    # 设置下次跟进时间
    def Set_TimeNextFollowTime(self, n_follow_s_time_value, n_follow_e_time_value):
        self.Set_input(self.f_business_filter_condition_n_follow_s_time_loc, n_follow_s_time_value)
        # 时间控件用完后必须要返回到所有操作的form下面
        self.find_element(*self.f_business_search_div_loc).click()
        self.Set_input(self.f_business_filter_condition_n_follow_e_time_loc, n_follow_e_time_value)
        # 时间控件用完后必须要返回到所有操作的form下面
        self.find_element(*self.f_business_search_div_loc).click()

    # 设置接收方式
    def Set_SelectWayCode(self, way_code_value):
        self.Set_Selects(self.f_business_filter_condition_way_code_loc, way_code_value)

    # 设置接收时间
    def Set_TimeReceptionTime(self, reception_s_time_value, reception_e_time_value):
        self.Set_input(self.f_business_filter_condition_reception_s_time_loc, reception_s_time_value)
        # 时间控件用完后必须要返回到所有操作的form下面
        self.find_element(*self.f_business_search_div_loc).click()
        self.Set_input(self.f_business_filter_condition_reception_e_time_loc, reception_e_time_value)
        # 时间控件用完后必须要返回到所有操作的form下面
        self.find_element(*self.f_business_search_div_loc).click()

    # 设置"搜索"操作按钮
    def Set_ButtonSearch(self):
        self.Set_Button(self.f_business_search_btn_loc)

    # 根据搜索条件搜索
    def Set_Search(self, search_info_list):
        # 设置客户信息
        if search_info_list[0] != '':
            self.Set_InputCusName(search_info_list[0])
        # 设置客户属性
        if search_info_list[1] != '':
            self.Set_InputSelectCusAttr(search_info_list[1])
        # 设置来源渠道
        if search_info_list[2] != '':
            self.Set_CascadeSelectOriginCode(search_info_list[2])
        # 设置是否VIP
        if search_info_list[3] != '':
            self.Set_SelectIsVip(search_info_list[3])
        # 设置贷款金额
        if search_info_list[4] != '':
            self.Set_InputLoanAmount(search_info_list[4])
        # 设置销售阶段
        if search_info_list[5] != '':
            self.Set_SelectBusinessStage(search_info_list[5])
        # 设置新增日期
        if search_info_list[6] != '':
            self.Set_TimeAddTime(search_info_list[6])
        # 设置最后跟进时间
        if search_info_list[7] != '':
            self.Set_TimeFollowTime(search_info_list[7])
        # 设置下次跟进时间
        if search_info_list[8] != '':
            self.Set_TimeNextFollowTime(search_info_list[8])
        # 设置接收方式
        if search_info_list[9] != '':
            self.Set_SelectWayCode(search_info_list[9])
        # 设置接收时间
        if search_info_list[10] != '':
            self.Set_TimeReceptionTime(search_info_list[10])

    # 设置"打电话"操作按钮
    def Set_ButtonCall(self):
        self.Set_Button(self.f_business_call_btn_loc)

    # 设置"隐藏"操作按钮
    def Set_ButtonHide(self):
        self.Set_Button(self.f_business_hide_btn_loc)

    # 设置"剔除"操作按钮
    def Set_ButtonDelete(self):
        self.Set_Button(self.f_business_delete_btn_loc)

    # 设置"返无效"操作按钮
    def Set_ButtonInvalid(self):
        self.Set_Button(self.f_business_invalid_btn_loc)

    # 设置"返无效"操作按钮
    def Set_ButtonChangeGroup(self):
        self.Set_Button(self.f_business_change_group_btn_loc)

    # 设置"编辑分组"操作按钮
    def Set_ButtonEditGroup(self):
        self.Set_Button(self.f_business_edit_group_btn_loc)

    # 设置"新建分组"操作按钮
    def Set_ButtonNewGroup(self):
        self.Set_Button(self.f_business_new_group_btn_loc)

    # 设置"今日待跟进"页签
    def Set_ATodayFollowing(self):
        self.Set_Button(self.f_business_today_following_link_loc)

    # 设置"今日预约上门"页签
    def Set_ATodayAppointment(self):
        self.Set_Button(self.f_business_today_appointment_link_loc)

    # 设置"逾期跟进"页签
    def Set_AOverdue(self):
        self.Set_Button(self.f_business_overdue_link_loc)

    # 设置"明天掉库"页签
    def Set_ATomorrow(self):
        self.Set_Button(self.f_business_tomorrow_link_loc)

    # 设置"2天后掉库"页签
    def Set_ATwoDay(self):
        self.Set_Button(self.f_business_two_day_link_loc)

    # 设置"全部"页签
    def Set_AAll(self):
        self.Set_Button(self.f_business_all_link_loc)

    # 设置"商机详情"超链接(点击指定行商机)
    def Set_ABusinessDetail(self, table_row):
        self.Set_Button(self.f_business_business_detail_link_loc, Celement=table_row)

    # 设置"备注"超链接(点击指定行商机)
    def Set_ARemark(self, table_row):
        self.Set_Button(self.f_business_business_remark_link_loc, Celement=table_row)

    # 设置"发短信"超链接(点击指定行商机)
    def Set_ASendMsg(self, table_row):
        self.Set_Button(self.f_business_business_send_msg_link_loc, Celement=table_row)

    # 设置"下单"超链接(点击指定行商机)
    def Set_AOrder(self, table_row):
        self.Set_Button(self.f_business_business_order_link_loc, Celement=table_row)

    # 根据行索引选中跟进中商机中的行
    def Set_CheckRowsFollowingBusinessTableByIndex(self, row_index_list):
        if row_index_list is not []:
            for row_index in row_index_list:
                table_row_element = self.Select_TableRowByRowNum(self.f_business_left_table_loc, int(row_index))
                if table_row_element is not None:
                    self.Select_CheckboxTableRow(table_row_element)
                else:
                    print('没有找到指定行，无法选中', self.f_business_right_table_loc, row_index)
        else:
            print('请指定行索引，否则无法选中', self.f_business_right_table_loc, row_index_list)

    # 选中跟进中商机中的所有行
    def Set_CheckAllRowsFollowingBusinessTable(self):
        table_row_element = self.Select_TableRowByRowNum(self.f_business_left_table_head_loc, 0)
        if table_row_element is not None:
            self.Select_CheckboxTableRow(table_row_element)
        else:
            print('没有找到指定行，无法选中', self.f_business_left_table_head_loc, 0)

    # 进入跟进中页面时，需要切换iframe
    def Iframe_FollowingBusiness(self):
        if self.IS_element_present(self.f_business_xpath_loc):
            f_business_frame = self.find_element(*self.f_business_xpath_loc)
            self.switch_frame(f_business_frame)
            return True
        else:
            print("找不到 %s" % self.f_business_xpath_loc, "停止测试")
            return False
    
    # 从商机-跟进中菜单进入跟进中商机列表页面，需要切换iframe
    def FollowingBusiness(self, login_type=1, user_name='51376245', password='666666'):
        self.menu_Following(login_type, user_name, password)
        return self.Iframe_FollowingBusiness()