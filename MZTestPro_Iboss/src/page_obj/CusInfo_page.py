"""
Created on 2018年3月13日

@author: 王贝贝 89144029
"""


from selenium.webdriver.common.by import By
# from page_com.CommonControl import CommonControl
from page_com.ExtendControlTable import ExtendControlTable
from time import sleep


class EditCusInfo(ExtendControlTable):

    """
    客户属性与客户资料
    """
    # 客户属性form
    cus_attr_form_loc = (By.ID, 'cus_attr_form')

    # 客户属性之房产
    # 房产付款方式
    cus_attr_house_pay_type_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'payType') and "
                                             "contains(@name,'attrBuildings')]")
    cus_attr_house_pay_type_dict = {'全款房': 0, '按揭房': 1, '无': 2}
    # 房屋类型
    cus_attr_house_type_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'buildingType') and "
                                         "contains(@name,'attrBuildings')]")
    cus_attr_house_type_dict = {'住宅': 0, '商铺': 1, '别墅': 2, '厂房': 3, '写字楼': 4, '安置房': 5, '经济适用房': 6,
                                '政策性住房': 7}
    # 建立时间
    cus_attr_house_built_time_loc = (By.XPATH, "//*[@type='text' and contains(@name,'builtUpTime') and "
                                               "contains(@name,'attrBuildings')]")
    # 房屋位置
    cus_attr_house_position_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'buildingPosition') and "
                                             "contains(@name,'attrBuildings')]")
    cus_attr_house_position_dict = {'主城区': 0, '郊区': 1, '外地': 2}
    # 房屋面积
    cus_attr_house_area_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'buildingArea') and "
                                         "contains(@name,'attrBuildings')]")
    cus_attr_house_area_dict = {'60㎡以下': 0, '60㎡~80㎡': 1, '80㎡~140㎡': 2, '140㎡~180㎡': 3, '180㎡以上': 4}
    # 市场价格
    cus_attr_house_market_price_loc = (By.XPATH, "//*[@type='text' and contains(@name,'marketPrice') and "
                                                 "contains(@name,'attrBuildings')]")
    # 房产证
    cus_attr_house_certificate_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'certificate') and "
                                                "contains(@name,'attrBuildings')]")
    cus_attr_house_certificate_dict = {'与他人共有': 0, '夫妻共有': 1, '单独所有': 2, '无': 3}
    # 按揭银行
    cus_attr_house_mortgage_bank_loc = (By.XPATH, "//select[contains(@name,'mortgageBank') and "
                                                  "contains(@name,'attrBuildings')]")
    cus_attr_house_mortgage_bank_dict = {'请选择': 0, '中国银行': 1, '建设银行': 2, '农业银行': 3, '工商银行': 4, '交通银行': 5,
                                         '兴业银行': 6}
    # 按揭金额
    cus_attr_house_mortgage_amount_loc = (By.XPATH, "//*[@type='text' and contains(@name,'mortgageAmount') and "
                                                    "contains(@name,'attrBuildings')]")
    # 按揭开始时间
    cus_attr_house_mortgage_time_loc = (By.XPATH, "//*[@type='text' and contains(@name,'mortgageTime') and "
                                                  "contains(@name,'attrBuildings')]")
    # 月供
    cus_attr_house_month_pay_loc = (By.XPATH, "//*[@type='text' and contains(@name,'monthPay') and "
                                              "contains(@name,'attrBuildings')]")
    # 按揭年限
    cus_attr_house_mortgage_years_loc = (By.XPATH, "//*[@type='text' and contains(@name,'mortgageYears') and "
                                                   "contains(@name,'attrBuildings')]")
    # 按揭方式
    cus_attr_house_mortgage_way_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'mortgageWay') and "
                                                 "contains(@name,'attrBuildings')]")
    cus_attr_house_mortgage_way_dict = {'商贷': 0, '公积金': 1, '公积金+商贷': 2}
    # 还款方式
    cus_attr_house_repayment_way_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'repaymentWay') and "
                                                  "contains(@name,'attrBuildings')]")
    cus_attr_house_repayment_way_dict = {'等额本息': 0, '等额本金': 1, '先息后本': 2, '组合还款': 3, '其它方式': 4}
    # 增加房产按钮
    cus_attr_house_add_btn_loc = {By.XPATH, "//a[@onclick='addHouse(this)']"}

    # 客户属性之车辆信息
    # 车辆付款方式
    cus_attr_car_pay_type_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'payType') and "
                                           "contains(@name,'attrVehicles')]")
    cus_attr_car_pay_type_dict = {'全款车': 0, '按揭车': 1, '无': 2}
    # 车辆品牌
    cus_attr_car_vehicle_brand_loc = (By.XPATH, "//select[contains(@name,'vehicleBrand') and "
                                                "contains(@name,'attrVehicles')]")
    cus_attr_car_vehicle_brand_dict = {'请选择': 0, 'A_ABT': 1}
    # 购车时间
    cus_attr_car_buying_time_loc = (By.XPATH, "//*[@type='text' and contains(@name,'buyingTime') and "
                                              "contains(@name,'attrVehicles')]")
    # 裸车价
    cus_attr_car_bare_car_price_loc = (By.XPATH, "//*[@type='text' and contains(@name,'bareCarPrice') and "
                                                 "contains(@name,'attrVehicles')]")
    # 车辆所属类型
    cus_attr_car_vehicle_type_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'vehicleType') and "
                                               "contains(@name,'attrVehicles')]")
    cus_attr_car_vehicle_type_dict = {'个人名下': 0, '公司名下': 1}
    # 车辆是否被抵押
    cus_attr_car_is_mortgage_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'isMortgage') and "
                                              "contains(@name,'attrVehicles')]")
    cus_attr_car_is_mortgage_dict = {'是': 0, '否': 1}
    # 车辆地域
    cus_attr_car_vehicle_area_loc = (By.XPATH, "//*[@type='text' and contains(@name,'vehicleArea') and "
                                               "contains(@name,'attrVehicles')]")
    # 按揭方式
    cus_attr_car_mortgage_way_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'mortgageWay') and "
                                               "contains(@name,'attrVehicles')]")
    cus_attr_car_mortgage_way_dict = {'金融公司': 0, '银行': 1, '信用卡': 2}
    # 按揭开始时间
    cus_attr_car_mortgage_time_loc = (By.XPATH, "//*[@type='text' and contains(@name,'mortgageTime') and "
                                                "contains(@name,'attrVehicles')]")
    # 按揭金额
    cus_attr_car_mortgage_amount_loc = (By.XPATH, "//*[@type='text' and contains(@name,'mortgageAmount') and "
                                                  "contains(@name,'attrVehicles')]")
    # 月供
    cus_attr_car_month_pay_loc = (By.XPATH, "//*[@type='text' and contains(@name,'monthPay') and "
                                            "contains(@name,'attrVehicles')]")
    # 按揭年限
    cus_attr_car_mortgage_years_loc = (By.XPATH, "//*[@type='text' and contains(@name,'mortgageYears') and "
                                                 "contains(@name,'attrVehicles')]")
    # 车辆保险
    cus_attr_car_vehicle_insurance_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'vehicleInsurance') and "
                                                    "contains(@name,'attrVehicles')]")
    cus_attr_car_vehicle_insurance_dict = {'无': 0, '其它商业险': 1, '双险': 2, '交强险': 3}
    # 车辆保险公司
    cus_attr_car_insurance_company_loc = (By.XPATH, "//select[contains(@name,'insuranceCompany') and "
                                                    "contains(@name,'attrVehicles')]")
    cus_attr_car_insurance_company_dict = {'平安': 1, '中国人保': 2, '太平洋': 3, '中华联合': 4}
    # 车辆保险金额
    cus_attr_car_insurance_amount_loc = (By.XPATH, "//*[@type='text' and contains(@name,'insuranceAmount') and "
                                                   "contains(@name,'attrVehicles')]")
    # 增加车辆按钮
    cus_attr_car_add_btn_loc = {By.XPATH, "//a[@onclick='addCar(this)']"}

    # 客户属性之保单信息
    # 保单有无
    cus_attr_insurance_policy_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'warranty')]")
    cus_attr_insurance_policy_dict = {'有保单': 0, '无': 1}
    # 保险公司
    cus_attr_insurance_company_loc = (By.XPATH, "//select[contains(@name,'attrPolicy.insuranceCompany')]")
    cus_attr_insurance_company_dict = {'中国人寿': 1, '中国人保': 2, '中国平安': 3, '太平洋': 4}
    # 缴费方式
    cus_attr_insurance_payment_way_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'attrPolicy.paymentWay')]")
    cus_attr_insurance_payment_way_dict = {'趸缴': 0, '月缴': 1, '季缴': 2, '年缴': 3}
    # 缴费金额
    cus_attr_insurance_payment_amount_loc = (By.XPATH, "//*[@type='text' and "
                                                       "contains(@name,'attrPolicy.paymentAmount')]")
    # 缴费开始时间
    cus_attr_insurance_payment_time_loc = (By.XPATH, "//*[@type='text' and contains(@name,'attrPolicy.paymentTime')]")
    # 已缴费年限
    cus_attr_insurance_payment_years_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'attrPolicy.paymentYears')]")
    cus_attr_insurance_payment_years_dict = {'1年': 0, '2年': 1, '3年': 1, '5年': 2, '5年以上': 3}
    # 投保人
    cus_attr_insurance_policy_holder_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'attrPolicy.policyHolder')]")
    cus_attr_insurance_policy_holder_dict = {'本人': 0, '他人': 1}
    # 是否变更投保人
    cus_attr_insurance_is_change_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'attrPolicy.isChange')]")
    cus_attr_insurance_is_change_dict = {'是': 0, '否': 1}
    # 变更时间
    cus_attr_insurance_change_time_loc = (By.XPATH, "//*[@type='text' and contains(@name,'attrPolicy.changeTime')]")

    # 客户属性之工作信息
    # 工作性质
    cus_attr_job_nature_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'jobNature')]")
    cus_attr_job_nature_dict = {'工薪': 0, '个体户': 1, '企业主': 2, '军人': 3, '无': 4}
    # 企业性质
    cus_attr_job_enterprise_nature_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'attrJob.enterpriseNature')]")
    cus_attr_job_enterprise_nature_dict = {'国企': 0, '事业编制': 1, '公务员': 2, '民营': 3, '无': 4}
    # 是否优质企业
    cus_attr_job_is_quality_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'attrJob.isQuality')]")
    cus_attr_job_is_quality_dict = {'是': 0, '否': 1}
    # 工资发放形式
    cus_attr_job_wages_pay_form_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'attrJob.wagesPayForm')]")
    cus_attr_job_wages_pay_form_dict = {'打卡': 0, '现金': 1, '转账': 1, '其它': 2}
    # 工资
    cus_attr_job_wages_loc = (By.XPATH, "//*[@type='text' and contains(@name,'attrJob.wages')]")
    # 开始经营时间
    cus_attr_job_start_operate_time_loc = (By.XPATH, "//*[@type='text' and contains(@name,'attrJob.startOperateTime')]")
    # 经营流水
    cus_attr_job_operating_stream_loc = (By.XPATH, "//*[@type='text' and contains(@name,'attrJob.operatingStream')]")
    # 营业执照
    cus_attr_job_business_license_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'attrJob.businessLicense')]")
    cus_attr_job_business_license_dict = {'有': 0, '无': 1}
    # 经营行业
    cus_attr_job_management_industry_loc = (By.XPATH, "//select[contains(@name,'attrJob.managementIndustry')]")
    cus_attr_job_management_industry_dict = {'食品': 1, '商贸': 2, '服饰': 3, '建材': 4}
    # 占股
    cus_attr_job_total_shares_loc = (By.XPATH, "//*[@type='text' and contains(@name,'attrJob.totalShares')]")
    # 是否文职军人
    cus_attr_job_civilian_soldier_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'attrJob.civilianSoldier')]")
    cus_attr_job_civilian_soldier_dict = {'是': 0, '否': 1}
    # 是否有身份证
    cus_attr_job_own_id_card_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'attrJob.ownIdCard')]")
    cus_attr_job_own_id_card_dict = {'有': 0, '无': 1}

    # 客户属性之社保信息
    # 社保有无
    cus_attr_social_security_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'social')]")
    cus_attr_social_security_dict = {'有社保': 0, '无': 1}
    # 购买人
    cus_attr_social_security_purchaser_loc = (By.XPATH, "//*[@type='radio' and "
                                                        "contains(@name,'attrSocialSecurity.purchaser')]")
    cus_attr_social_security_purchaser_dict = {'本单位': 0, '本人': 1, '第三方': 2}
    # 社保基数
    cus_attr_social_security_base_loc = (By.XPATH, "//*[@type='text' and "
                                                   "contains(@name,'attrSocialSecurity.socialSecurityBase')]")
    # 已缴费年限
    cus_attr_social_security_years_loc = (By.XPATH, "//*[@type='text' and "
                                                    "contains(@name,'attrSocialSecurity.socialSecurityYears')]")
    # 客户属性之公积金信息
    # 公积金有无
    cus_attr_acc_fund_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'money')]")
    cus_attr_acc_fund_dict = {'有公积金': 0, '无': 1}
    # 公积金基数
    cus_attr_acc_fund_base_loc = (By.XPATH, "//*[@type='text' and contains(@name,'attrAccFund.accFundBase')]")
    # 缴纳年限
    cus_attr_acc_fund_payment_years_loc = (By.XPATH, "//*[@type='text' and contains(@name,'attrAccFund.paymentYears')]")
    # 购买单位
    cus_attr_acc_fund_purchaser_unit_loc = (By.XPATH, "//*[@type='radio' and "
                                                      "contains(@name,'attrAccFund.purchaseUnit')]")
    cus_attr_acc_fund_purchaser_unit_dict = {'本单位': 0, '第三方': 1}

    # 客户属性之负债信息
    # 负债有无
    cus_attr_liability_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'attrLiability.liabilityType')]")
    cus_attr_liability_dict = {'抵押贷款': 0, '银行信贷': 1, '车贷': 2, '小贷': 3, '房屋抵押': 4, '无': 5}
    # 是否逾期
    cus_attr_liability_is_overdue_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'attrLiability.isOverdue')]")
    cus_attr_liability_is_overdue_dict = {'无': 0, '1年内有逾期': 1, '2年内有逾期': 2, '2-5年内有逾期': 3,
                                          '呆账/坏账/冻结': 4, '法院执行': 5}
    # 逾期金额
    cus_attr_liability_overdue_amount_loc = (By.XPATH, "//*[@type='text' and "
                                                       "contains(@name,'attrLiability.overdueAmount')]")
    # 逾期次数
    cus_attr_liability_overdue_times_loc = (By.XPATH, "//*[@type='text' and "
                                                      "contains(@name,'attrLiability.overdueTimes')]")

    # 客户属性之信用卡信息
    # 信用卡有无
    cus_attr_credit_card_liabilities_loc = (By.XPATH, "//*[@type='radio' and contains(@name,'liabilities')]")
    cus_attr_credit_card_liabilities_dict = {'有信用卡': 0, '无': 1}
    # 逾期金额
    cus_attr_credit_card_quota_loc = (By.XPATH, "//*[@type='text' and contains(@name,'attrCreditCard.quota')]")
    # 逾期次数
    cus_attr_credit_card_usage_quota_loc = (By.XPATH, "//*[@type='text' and "
                                                      "contains(@name,'attrCreditCard.usageQuota')]")
    # 是否透支
    cus_attr_credit_card_is_overdraft_loc = (By.XPATH, "//*[@type='radio' and "
                                                       "contains(@name,'attrCreditCard.isOverdraft')]")
    cus_attr_credit_card_is_overdraft_dict = {'是': 0, '否': 1}

    # 客户资料
    # 客户资料大类
    cus_data_class_dict = {0: '工作证明', 1: '房产证明', 2: '婚姻证明', 3: '身份证明', 4: '其它资料'}
    # 客户资料复印件或原件复选框
    cus_data_detail_checkbox_loc = (By.XPATH, "//input[@type = 'checkbox' and contains(@name,'IdCardName')]")

    # 设置客户属性之房产
    # 设置房产付款方式
    def Set_RadioHousePayType(self, house_pay_type_value):
        self.Set_RadioByIndex(self.cus_attr_house_pay_type_loc, self.cus_attr_house_pay_type_dict[house_pay_type_value])

    # 设置房屋类型
    def Set_RadioHouseType(self, house_type_value):
        self.Set_RadioByIndex(self.cus_attr_house_type_loc, self.cus_attr_house_type_dict[house_type_value])

    # 设置建立时间
    def Set_TimeHouseBuiltTime(self, house_built_time_value):
        self.Set_input(self.cus_attr_house_built_time_loc, house_built_time_value)
        # 时间控件用完后必须要返回到所操作的form下面
        self.find_element(*self.cus_attr_form_loc).click()

    # 设置房屋位置
    def Set_RadioHousePosition(self, house_position_value):
        self.Set_RadioByIndex(self.cus_attr_house_position_loc, self.cus_attr_house_position_dict[house_position_value])

    # 设置房屋面积
    def Set_RadioHouseArea(self, house_area_value):
        self.Set_RadioByIndex(self.cus_attr_house_area_loc, self.cus_attr_house_area_dict[house_area_value])

    # 设置市场价格
    def Set_InputHouseMarketPrice(self, house_market_price_value):
        self.Set_input(self.cus_attr_house_market_price_loc, inputtext=house_market_price_value)

    # 设置房产证
    def Set_RadioHouseCertificate(self, house_certificate_value):
        self.Set_RadioByIndex(self.cus_attr_house_certificate_loc,
                              self.cus_attr_house_certificate_dict[house_certificate_value])

    # 设置按揭银行
    def Set_SelectHouseMortgageBank(self, house_mortgage_bank_value):
        self.Set_SelectByIndex(self.cus_attr_house_mortgage_bank_loc,
                               self.cus_attr_house_mortgage_bank_dict[house_mortgage_bank_value])

    # 设置按揭金额
    def Set_InputHouseMortgageAmount(self, house_mortgage_amount_value):
        self.Set_input(self.cus_attr_house_mortgage_amount_loc, inputtext=house_mortgage_amount_value)

    # 设置按揭开始时间
    def Set_TimeHouseMortgageTime(self, house_mortgage_time_value):
        self.Set_input(self.cus_attr_house_mortgage_time_loc, house_mortgage_time_value)
        # 时间控件用完后必须要返回到所操作的form下面
        self.find_element(*self.cus_attr_form_loc).click()

    # 设置月供
    def Set_InputHouseMonthPay(self, house_month_pay_value):
        self.Set_input(self.cus_attr_house_month_pay_loc, inputtext=house_month_pay_value)

    # 设置按揭年限
    def Set_InputHouseMortgageYears(self, house_mortgage_years_value):
        self.Set_input(self.cus_attr_house_mortgage_years_loc, inputtext=house_mortgage_years_value)

    # 设置按揭方式
    def Set_RadioHouseMortgageWay(self, house_mortgage_way_value):
        self.Set_RadioByIndex(self.cus_attr_house_mortgage_way_loc,
                              self.cus_attr_house_mortgage_way_dict[house_mortgage_way_value])

    # 设置还款方式
    def Set_RadioHouseRepaymentWay(self, house_repayment_way_value):
        self.Set_RadioByIndex(self.cus_attr_house_repayment_way_loc,
                              self.cus_attr_house_repayment_way_dict[house_repayment_way_value])

    # 设置增加房产
    def Set_ButtonHouseAdd(self):
        self.Set_Button(self.cus_attr_house_add_btn_loc)

    # 设置第N套房产信息
    def Set_House(self, house_index, house_info_list):
        # 如果当前设置的不是第一套房产，则需要先点击增加房产
        if house_index > 0:
            self.Set_ButtonHouseAdd()
        # 设置房屋付款类型的信息
        if house_info_list[0] != '':
            self.Set_RadioHousePayType(house_info_list[0])
            sleep(1)
            # 设置全款房或按揭房的公共信息
            if house_info_list[0] == '全款房' or house_info_list[0] == '按揭房':
                # 设置房屋类型
                if house_info_list[1] != '':
                    self.Set_RadioHouseType(house_info_list[1])
                # 设置建立时间
                if house_info_list[2] != '':
                    self.Set_TimeHouseBuiltTime(house_info_list[2])
                # 设置房屋位置
                if house_info_list[3] != '':
                    self.Set_RadioHousePosition(house_info_list[3])
                # 设置房屋面积
                if house_info_list[4] != '':
                    self.Set_RadioHouseArea(house_info_list[4])
                # 设置市场价格
                if house_info_list[5] != '':
                    self.Set_InputHouseMarketPrice(house_info_list[5])
                # 设置房产证
                if house_info_list[6] != '':
                    self.Set_RadioHouseCertificate(house_info_list[6])
            # 设置按揭房的额外信息
            if house_info_list[0] == '按揭房':
                # 设置按揭银行
                if house_info_list[7] != '':
                    self.Set_SelectHouseMortgageBank(house_info_list[7])
                # 设置按揭金额
                if house_info_list[8] != '':
                    self.Set_InputHouseMortgageAmount(house_info_list[8])
                # 设置按揭开始时间
                if house_info_list[9] != '':
                    self.Set_TimeHouseMortgageTime(house_info_list[9])
                # 设置月供
                if house_info_list[10] != '':
                    self.Set_InputHouseMonthPay(house_info_list[10])
                # 设置按揭年限
                if house_info_list[11] != '':
                    self.Set_InputHouseMortgageYears(house_info_list[11])
                # 设置按揭方式
                if house_info_list[12] != '':
                    self.Set_RadioHouseMortgageWay(house_info_list[12])
                # 设置还款方式
                if house_info_list[13] != '':
                    self.Set_RadioHouseRepaymentWay(house_info_list[13])

    # 设置客户属性之车辆信息
    # 设置车辆付款方式
    def Set_RadioCarPayType(self, car_pay_type_value):
        self.Set_RadioByIndex(self.cus_attr_car_pay_type_loc, self.cus_attr_car_pay_type_dict[car_pay_type_value])

    # 设置车辆品牌
    def Set_SelectCarVehicleBrand(self, car_vehicle_brand_value):
        self.Set_SelectByIndex(self.cus_attr_car_vehicle_brand_loc,
                               self.cus_attr_car_vehicle_brand_dict[car_vehicle_brand_value])

    # 设置购车时间
    def Set_TimeCarBuyingTime(self, car_buying_time_value):
        self.Set_input(self.cus_attr_car_buying_time_loc, car_buying_time_value)
        # 时间控件用完后必须要返回到所操作的form下面
        self.find_element(*self.cus_attr_form_loc).click()

    # 设置裸车价
    def Set_InputCarBareCarPrice(self, car_bare_car_price_value):
        self.Set_input(self.cus_attr_car_bare_car_price_loc, inputtext=car_bare_car_price_value)

    # 设置车辆所属类型
    def Set_RadioCarVehicleType(self, car_vehicle_type_value):
        self.Set_RadioByIndex(self.cus_attr_car_vehicle_type_loc,
                              self.cus_attr_car_vehicle_type_dict[car_vehicle_type_value])

    # 设置车辆是否被抵押
    def Set_RadioCarIsMortgage(self, car_is_mortgage_value):
        self.Set_RadioByIndex(self.cus_attr_car_is_mortgage_loc,
                              self.cus_attr_car_is_mortgage_dict[car_is_mortgage_value])

    # 设置车辆地域
    def Set_InputCarVehicleArea(self, car_vehicle_area_value):
        self.Set_input(self.cus_attr_car_vehicle_area_loc, inputtext=car_vehicle_area_value)

    # 设置按揭方式
    def Set_RadioCarMortgageWay(self, car_mortgage_way_value):
        self.Set_RadioByIndex(self.cus_attr_car_mortgage_way_loc,
                              self.cus_attr_car_mortgage_way_dict[car_mortgage_way_value])

    # 设置按揭开始时间
    def Set_TimeCarMortgageTime(self, car_mortgage_time_value):
        self.Set_input(self.cus_attr_car_mortgage_time_loc, car_mortgage_time_value)
        # 时间控件用完后必须要返回到所操作的form下面
        self.find_element(*self.cus_attr_form_loc).click()
        sleep(1)

    # 设置按揭金额
    def Set_InputCarMortgageAmount(self, car_mortgage_amount_value):
        self.Set_input(self.cus_attr_car_mortgage_amount_loc, inputtext=car_mortgage_amount_value)

    # 设置月供
    def Set_InputCarMonthPay(self, car_month_pay_value):
        self.Set_input(self.cus_attr_car_month_pay_loc, inputtext=car_month_pay_value)

    # 设置按揭年限
    def Set_InputCarMortgageYears(self, car_mortgage_years_value):
        self.Set_input(self.cus_attr_car_mortgage_years_loc, inputtext=car_mortgage_years_value)

    # 设置车辆保险
    def Set_RadioCarVehicleInsurance(self, car_vehicle_insurance_value):
        self.Set_RadioByIndex(self.cus_attr_car_vehicle_insurance_loc,
                              self.cus_attr_car_vehicle_insurance_dict[car_vehicle_insurance_value])

    # 设置车辆保险公司
    def Set_SelectCarInsuranceCompany(self, car_insurance_company_value):
        self.Set_SelectByIndex(self.cus_attr_car_insurance_company_loc,
                               self.cus_attr_car_insurance_company_dict[car_insurance_company_value])

    # 设置车辆保险金额
    def Set_InputCarInsuranceAmount(self, car_insurance_amount_value):
        self.Set_input(self.cus_attr_car_insurance_amount_loc, inputtext=car_insurance_amount_value)

    # 增加车辆按钮
    def Set_ButtonCarAdd(self):
        self.Set_Button(self.cus_attr_car_add_btn_loc)

    # 设置第N套车辆信息
    def Set_Car(self, car_index, car_info_list):
        # 如果当前设置的不是第一辆车辆，则需要先点击增加车辆
        if car_index > 0:
            self.Set_ButtonCarAdd()
        # 设置车辆付款类型的信息
        if car_info_list[0] != '':
            self.Set_RadioCarPayType(car_info_list[0])
            # 设置全款车或按揭车的公共信息
            if car_info_list[0] == '全款车' or car_info_list[0] == '按揭车':
                # 设置车辆品牌
                if car_info_list[1] != '':
                    self.Set_SelectCarVehicleBrand(car_info_list[1])
                # 设置购车时间
                if car_info_list[2] != '':
                    self.Set_TimeCarBuyingTime(car_info_list[2])
                # 设置裸车价
                if car_info_list[3] != '':
                    self.Set_InputCarBareCarPrice(car_info_list[3])
                # 设置车辆所属类型
                if car_info_list[4] != '':
                    self.Set_RadioCarVehicleType(car_info_list[4])
                # 设置车辆是否被抵押
                if car_info_list[5] != '':
                    self.Set_RadioCarIsMortgage(car_info_list[5])
                # 设置车辆地域
                if car_info_list[6] != '':
                    self.Set_InputCarVehicleArea(car_info_list[6])
            # 设置按揭车的额外信息
            if car_info_list[0] == '按揭车':
                # 设置按揭方式
                if car_info_list[7] != '':
                    self.Set_RadioCarMortgageWay(car_info_list[7])
                # 设置按揭开始时间
                if car_info_list[8] != '':
                    self.Set_TimeCarMortgageTime(car_info_list[8])
                # 设置按揭金额
                if car_info_list[9] != '':
                    self.Set_InputCarMortgageAmount(car_info_list[9])
                # 设置月供
                if car_info_list[10] != '':
                    self.Set_InputCarMonthPay(car_info_list[10])
                # 设置按揭年限
                if car_info_list[11] != '':
                    self.Set_InputCarMortgageYears(car_info_list[11])
                # 设置车辆保险
                if car_info_list[12] != '':
                    self.Set_RadioCarVehicleInsurance(car_info_list[12])
                    if car_info_list[12] != '无':
                        # 设置车辆保险公司
                        if car_info_list[13] != '':
                            self.Set_SelectCarInsuranceCompany(car_info_list[13])
                        if car_info_list[14] != '':
                            # 设置车辆保险金额
                            self.Set_InputCarInsuranceAmount(car_info_list[14])

    # 设置客户属性之保单信息
    # 设置保单有无
    def Set_RadioInsurancePolicy(self, insurance_policy_value):
        self.Set_RadioByIndex(self.cus_attr_insurance_policy_loc,
                              self.cus_attr_insurance_policy_dict[insurance_policy_value])

    # 设置保险公司
    def Set_SelectInsuranceCompany(self, insurance_company_value):
        self.Set_SelectByIndex(self.cus_attr_insurance_company_loc,
                               self.cus_attr_insurance_company_dict[insurance_company_value])

    # 设置缴费方式
    def Set_RadioInsurancePaymentWay(self, insurance_payment_way_value):
        self.Set_RadioByIndex(self.cus_attr_insurance_payment_way_loc,
                              self.cus_attr_insurance_payment_way_dict[insurance_payment_way_value])

    # 设置缴费金额
    def Set_InputInsurancePaymentAmount(self, insurance_payment_amount_value):
        self.Set_input(self.cus_attr_insurance_payment_amount_loc, inputtext=insurance_payment_amount_value)

    # 设置缴费开始时间
    def Set_TimeInsurancePaymentTime(self, insurance_payment_time_value):
        self.Set_input(self.cus_attr_insurance_payment_time_loc, inputtext=insurance_payment_time_value)
        # 时间控件用完后必须要返回到所操作的form下面
        self.find_element(*self.cus_attr_form_loc).click()

    # 设置已缴费年限
    def Set_RadioInsurancePaymentYears(self, insurance_payment_years_value):
        self.Set_RadioByIndex(self.cus_attr_insurance_payment_years_loc,
                              self.cus_attr_insurance_payment_years_dict[insurance_payment_years_value])

    # 设置投保人
    def Set_RadioInsurancePolicyHolder(self, insurance_policy_holder_value):
        self.Set_RadioByIndex(self.cus_attr_insurance_policy_holder_loc,
                              self.cus_attr_insurance_policy_holder_dict[insurance_policy_holder_value])

    # 设置是否变更投保人
    def Set_RadioInsuranceIsChange(self, insurance_is_change_value):
        self.Set_RadioByIndex(self.cus_attr_insurance_is_change_loc,
                              self.cus_attr_insurance_is_change_dict[insurance_is_change_value])

    # 设置变更时间
    def Set_TimeInsuranceChangeTime(self, insurance_change_time_value):
        self.Set_input(self.cus_attr_insurance_change_time_loc, inputtext=insurance_change_time_value)
        # 时间控件用完后必须要返回到所操作的form下面
        self.find_element(*self.cus_attr_form_loc).click()

    # 设置保单信息
    def Set_Insurance(self, insurance_info_list):
        # 设置保单有无
        if insurance_info_list[0] != '':
            self.Set_RadioInsurancePolicy(insurance_info_list[0])
        # 设置保单信息
        if insurance_info_list[0] == '有保单':
            # 设置保险公司
            if insurance_info_list[1] != '':
                self.Set_SelectInsuranceCompany(insurance_info_list[1])
            # 设置缴费方式
            if insurance_info_list[2] != '':
                self.Set_RadioInsurancePaymentWay(insurance_info_list[2])
            # 设置缴费金额
            if insurance_info_list[3] != '':
                self.Set_InputInsurancePaymentAmount(insurance_info_list[3])
            # 设置缴费开始时间
            if insurance_info_list[4] != '':
                self.Set_TimeInsurancePaymentTime(insurance_info_list[4])
            # 设置已缴费年限
            if insurance_info_list[5] != '':
                self.Set_RadioInsurancePaymentYears(insurance_info_list[5])
            # 设置投保人
            if insurance_info_list[6] != '':
                self.Set_RadioInsurancePolicyHolder(insurance_info_list[6])
            # 设置是否变更投保人
            if insurance_info_list[7] != '':
                self.Set_RadioInsuranceIsChange(insurance_info_list[7])
                # 如果变更投保人，设置变更时间
                if insurance_info_list[7] == '是':
                    if insurance_info_list[8] != '':
                        self.Set_TimeInsuranceChangeTime(insurance_info_list[8])

    # 设置客户属性之工作信息
    # 设置工作性质
    def Set_RadioJobNature(self, job_nature_value):
        self.Set_RadioByIndex(self.cus_attr_job_nature_loc, self.cus_attr_job_nature_dict[job_nature_value])

    # 设置企业性质
    def Set_RadioJobEnterpriseNature(self, job_enterprise_nature_value):
        self.Set_RadioByIndex(self.cus_attr_job_enterprise_nature_loc,
                              self.cus_attr_job_enterprise_nature_dict[job_enterprise_nature_value])

    # 设置是否优质企业
    def Set_RadioJobIsQuality(self, job_is_quality_value):
        self.Set_RadioByIndex(self.cus_attr_job_is_quality_loc,
                              self.cus_attr_job_is_quality_dict[job_is_quality_value])

    # 设置工资发放形式
    def Set_RadioJobWagesPayForm(self, job_wages_pay_form_value):
        self.Set_RadioByIndex(self.cus_attr_job_wages_pay_form_loc,
                              self.cus_attr_job_wages_pay_form_dict[job_wages_pay_form_value])

    # 设置工资
    def Set_InputJobWages(self, job_wages_value):
        self.Set_input(self.cus_attr_job_wages_loc, inputtext=job_wages_value)

    # 设置开始经营时间
    def Set_TimeJobStartOperateTime(self, job_start_operate_time_value):
        self.Set_input(self.cus_attr_job_start_operate_time_loc, inputtext=job_start_operate_time_value)
        # 时间控件用完后必须要返回到所操作的form下面
        self.find_element(*self.cus_attr_form_loc).click()

    # 设置经营流水
    def Set_InputJobOperatingStream(self, job_operating_stream_value):
        self.Set_input(self.cus_attr_job_operating_stream_loc, inputtext=job_operating_stream_value)

    # 设置营业执照
    def Set_RadioJobBusinessLicense(self, job_business_license_value):
        self.Set_RadioByIndex(self.cus_attr_job_business_license_loc,
                              self.cus_attr_job_business_license_dict[job_business_license_value])

    # 设置经营行业
    def Set_SelectJobManagementIndustry(self, job_management_industry_value):
        self.Set_SelectByIndex(self.cus_attr_job_management_industry_loc,
                               self.cus_attr_job_management_industry_dict[job_management_industry_value])

    # 设置占股
    def Set_InputJobTotalShares(self, job_total_shares_value):
        self.Set_input(self.cus_attr_job_total_shares_loc, inputtext=job_total_shares_value)

    # 设置是否文职军人
    def Set_RadioJobCivilianSoldier(self, job_civilian_soldier_value):
        self.Set_RadioByIndex(self.cus_attr_job_civilian_soldier_loc,
                              self.cus_attr_job_civilian_soldier_dict[job_civilian_soldier_value])

    # 设置是否有身份证
    def Set_RadioJobOwnidCard(self, job_own_id_card_value):
        self.Set_RadioByIndex(self.cus_attr_job_own_id_card_loc,
                              self.cus_attr_job_own_id_card_dict[job_own_id_card_value])

    # 设置工作信息
    def Set_Job(self, job_info_list):
        # 设置工作类型
        if job_info_list[0] != '':
            self.Set_RadioJobNature(job_info_list[0])
        # 设置工薪信息
        if job_info_list[0] == '工薪':
            # 设置企业性质
            if job_info_list[1] != '':
                self.Set_RadioJobEnterpriseNature(job_info_list[1])
            # 设置是否优质企业
            if job_info_list[2] != '':
                self.Set_RadioJobIsQuality(job_info_list[2])
            # 设置工资发放形式
            if job_info_list[3] != '':
                self.Set_RadioJobWagesPayForm(job_info_list[3])
            # 设置工资
            if job_info_list[4] != '':
                self.Set_InputJobWages(job_info_list[4])
        # 设置个体户或企业主的公共信息
        if job_info_list[0] == '个体户' or job_info_list[0] == '企业主':
            # 设置开始经营时间
            if job_info_list[1] != '':
                self.Set_TimeJobStartOperateTime(job_info_list[1])
            # 设置经营流水
            if job_info_list[2] != '':
                self.Set_InputJobOperatingStream(job_info_list[2])
            # 设置营业执照
            if job_info_list[3] != '':
                self.Set_RadioJobBusinessLicense(job_info_list[3])
        # 设置个体户的额外信息
        if job_info_list[0] == '个体户':
            # 设置经营行业
            if job_info_list[4] != '':
                self.Set_SelectJobManagementIndustry(job_info_list[4])
        # 设置企业主的额外信息
        if job_info_list[0] == '企业主':
            # 设置经营行业
            if job_info_list[4] != '':
                self.Set_InputJobTotalShares(job_info_list[4])
            # 设置经营行业
            if job_info_list[5] != '':
                self.Set_SelectJobManagementIndustry(job_info_list[5])
        # 设置军人信息
        if job_info_list[0] == '军人':
            # 设置是否文职军人
            if job_info_list[1] != '':
                self.Set_RadioJobCivilianSoldier(job_info_list[1])
            # 设置是否有身份证
            if job_info_list[2] != '':
                self.Set_RadioJobOwnidCard(job_info_list[2])

    # 设置客户属性之社保信息
    # 设置社保有无
    def Set_RadioSocialSecurity(self, social_security_value):
        self.Set_RadioByIndex(self.cus_attr_social_security_loc,
                              self.cus_attr_social_security_dict[social_security_value])

    # 设置购买人
    def Set_RadioSocialSecurityPurchaser(self, social_security_purchaser_value):
        self.Set_RadioByIndex(self.cus_attr_social_security_purchaser_loc,
                              self.cus_attr_social_security_purchaser_dict[social_security_purchaser_value])

    # 设置社保基数
    def Set_InputSocialSecurityBase(self, social_security_base_value):
        self.Set_input(self.cus_attr_social_security_base_loc, inputtext=social_security_base_value)

    # 设置已缴费年限
    def Set_InputSocialSecurityYears(self, social_security_years_value):
        self.Set_input(self.cus_attr_social_security_years_loc, inputtext=social_security_years_value)

    # 设置社保信息
    def Set_SocialSecurity(self, social_security_info_list):
        # 设置社保有无
        if social_security_info_list[0] != '':
            self.Set_RadioSocialSecurity(social_security_info_list[0])
        # 设置社保信息
        if social_security_info_list[0] == '有社保':
            # 设置购买人
            if social_security_info_list[1] != '':
                self.Set_RadioSocialSecurityPurchaser(social_security_info_list[1])
            # 设置社保基数
            if social_security_info_list[2] != '':
                self.Set_InputSocialSecurityBase(social_security_info_list[2])
            # 设置已缴费年限
            if social_security_info_list[3] != '':
                self.Set_InputSocialSecurityYears(social_security_info_list[3])

    # 设置客户属性之公积金信息
    # 设置公积金有无
    def Set_RadioAccFund(self, acc_fund_value):
        self.Set_RadioByIndex(self.cus_attr_acc_fund_loc, self.cus_attr_acc_fund_dict[acc_fund_value])

    # 设置公积金基数
    def Set_InputAccFundBase(self, acc_fund_base_value):
        self.Set_input(self.cus_attr_acc_fund_base_loc, inputtext=acc_fund_base_value)

    # 设置缴纳年限
    def Set_InputAccFundPaymentYears(self, acc_fund_payment_years_value):
        self.Set_input(self.cus_attr_acc_fund_payment_years_loc, inputtext=acc_fund_payment_years_value)

    # 设置购买单位
    def Set_RadioAccFundPurchaserUnit(self, acc_fund_purchaser_unit_value):
        self.Set_RadioByIndex(self.cus_attr_acc_fund_purchaser_unit_loc,
                              self.cus_attr_acc_fund_purchaser_unit_dict[acc_fund_purchaser_unit_value])

    # 设置公积金信息
    def Set_AccFund(self, acc_fund_info_list):
        # 设置公积金有无
        if acc_fund_info_list[0] != '':
            self.Set_RadioAccFund(acc_fund_info_list[0])
        # 设置公积金信息
        if acc_fund_info_list[0] == '有公积金':
            # 设置公积金基数
            if acc_fund_info_list[1] != '':
                self.Set_InputAccFundBase(acc_fund_info_list[1])
            # 设置缴纳年限
            if acc_fund_info_list[2] != '':
                self.Set_InputAccFundPaymentYears(acc_fund_info_list[2])
            # 设置购买单位
            if acc_fund_info_list[3] != '':
                self.Set_RadioAccFundPurchaserUnit(acc_fund_info_list[3])

    # 设置客户属性之负债信息
    # 设置负债有无
    def Set_RadioLiability(self, liability_value):
        self.Set_RadioByIndex(self.cus_attr_liability_loc, self.cus_attr_liability_dict[liability_value])

    # 设置是否逾期
    def Set_RadioLiabilityIsOverdue(self, liability_is_overdue_value):
        self.Set_RadioByIndex(self.cus_attr_liability_is_overdue_loc,
                              self.cus_attr_liability_is_overdue_dict[liability_is_overdue_value])

    # 设置逾期金额
    def Set_InputLiabilityOverdueAmount(self, liability_overdue_amount_value):
        self.Set_input(self.cus_attr_liability_overdue_amount_loc, inputtext=liability_overdue_amount_value)

    # 设置逾期次数
    def Set_InputLiabilityOverdueTimes(self, liability_overdue_times_value):
        self.Set_input(self.cus_attr_liability_overdue_times_loc, inputtext=liability_overdue_times_value)

    # 设置负债信息
    def Set_Liability(self, liability_info_list):
        # 设置负债有无
        if liability_info_list[0] != '':
            self.Set_RadioLiability(liability_info_list[0])
            # 设置抵押贷款或银行信贷或车贷或房屋抵押的公共信息
            if liability_info_list[0] != '无':
                # 设置是否逾期
                if liability_info_list[1] != '':
                    self.Set_RadioLiabilityIsOverdue(liability_info_list[1])
                # 设置逾期金额
                if liability_info_list[2] != '':
                    self.Set_InputLiabilityOverdueAmount(liability_info_list[2])
                # 设置逾期次数
                if liability_info_list[3] != '':
                    self.Set_InputLiabilityOverdueTimes(liability_info_list[3])

    # 设置客户属性之信用卡信息
    # 设置信用卡有无
    def Set_RadioCreditCardLiabilities(self, credit_card_liabilities_value):
        self.Set_RadioByIndex(self.cus_attr_credit_card_liabilities_loc,
                              self.cus_attr_credit_card_liabilities_dict[credit_card_liabilities_value])

    # 设置逾期金额
    def Set_InputCreditCardQuota(self, credit_card_quota_value):
        self.Set_input(self.cus_attr_credit_card_quota_loc, inputtext=credit_card_quota_value)

    # 设置逾期次数
    def Set_InputCreditCardUsageQuota(self, credit_card_usage_quota_value):
        self.Set_input(self.cus_attr_credit_card_usage_quota_loc, inputtext=credit_card_usage_quota_value)

    # 设置是否透支
    def Set_RadioCreditCardIsOverdraft(self, credit_card_is_overdraft_value):
        self.Set_RadioByIndex(self.cus_attr_credit_card_is_overdraft_loc,
                              self.cus_attr_credit_card_is_overdraft_dict[credit_card_is_overdraft_value])

    # 设置信用卡信息
    def Set_CreditCard(self, credit_card_info_list):
        # 设置信用卡有无
        if credit_card_info_list[0] != '':
            self.Set_RadioCreditCardLiabilities(credit_card_info_list[0])
        # 设置信用卡信息
        if credit_card_info_list[0] == '有信用卡':
            # 设置逾期金额
            if credit_card_info_list[1] != '':
                self.Set_InputCreditCardQuota(credit_card_info_list[1])
            # 设置逾期次数
            if credit_card_info_list[2] != '':
                self.Set_InputCreditCardUsageQuota(credit_card_info_list[2])
            # 设置是否透支
            if credit_card_info_list[3] != '':
                self.Set_RadioCreditCardIsOverdraft(credit_card_info_list[3])

    # 设置客户资料
    def Set_CheckboxOrSwitchCusData(self, cus_data_loc):
        self.Set_Checkbox(cus_data_loc)

    # 设置相关资料类别
    def Set_CusDataClass(self, cus_data_list):
        cus_data_type_value_all_list = []
        for cus_data_index in range(len(cus_data_list)):
            if cus_data_list[cus_data_index] != 'null':
                # 展开此项证明的相关资料
                cus_data_switch_loc = (By.XPATH, "//a[@title='" + self.cus_data_class_dict[cus_data_index] +
                                       "']/preceding-sibling::span[contains(@id,'switch')]")
                self.Set_CheckboxOrSwitchCusData(cus_data_switch_loc)
                sleep(1)

                cus_data_value_str_list = cus_data_list[cus_data_index].split(':')
                for cus_data_value_str in cus_data_value_str_list:
                    cus_data_type_value_list = cus_data_value_str.split('(')[1].split(')')[0].split(',')
                    for cus_data_type_value in cus_data_type_value_list:
                        cus_data_type_value_all_list.append(cus_data_type_value)
                    cus_data_value_list = cus_data_value_str.split('(')
                    cus_data_value_check_loc = (By.XPATH, "//a[@title='" + cus_data_value_list[0] +
                                                "']/preceding-sibling::span[contains(@id,'check')]")
                    self.Set_CheckboxOrSwitchCusData(cus_data_value_check_loc)
                    sleep(1)
        return cus_data_type_value_all_list

    # 设置客户资料的原件复印件
    def Set_CheckboxCusDataDetail(self, cus_data_detail_index):
        self.Set_CheckboxByIndex(self.cus_data_detail_checkbox_loc, cus_data_detail_index)

    # 设置资料的原件复印件
    def Set_CusDataDatil(self, cus_num, cus_data_list):
        if cus_data_list is []:
            print('无客户资料')
        else:
            for cus_index in range(cus_num):
                for cus_data_type_value_index in range(len(cus_data_list)):
                    if cus_data_list[cus_data_type_value_index] == '1':
                        self.Set_CheckboxCusDataDetail(cus_index * len(cus_data_list) + cus_data_type_value_index)