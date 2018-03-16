'''
Created on 2018年2月22日

@author: fanzhaoni
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
import unittest, time, re


class BusinessTestCase(unittest.TestCase):
    def setUp(self):
 
        # 加启动配置 （用于去掉启动浏览器出现‘Chrome正在受到自动软件的控制’）
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
    
        # 打开chrome浏览器
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.base_url = "https://192.168.254.80:8037"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_Business(self):
        driver = self.driver
        url = self.base_url + "/platform/index.shtml"
        driver.get(url)
        time.sleep(3)
        driver.find_element_by_id("userName").click()
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("51376245")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("666666")
        driver.find_element_by_xpath("//button[@onclick='return login();']").click()
        time.sleep(5)

        # 进入跟进中页面
        driver.find_element_by_xpath("//span[starts-with(text(),'商机')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//span[starts-with(text(),'跟进中')]").click()
        time.sleep(3)

        driver.switch_to.frame(driver.find_element_by_xpath(
            "//iframe[starts-with(@src,'/bus/list/followingIndex.shtml?type=all&is_first_request=1')]"))
        # 刷新跟进中列表数据，需要等待刷新时间
        time.sleep(3)

        # # 方法一：直接取出表中的每列，存入一个列表
        # # 获取跟进中商机列表
        # table = driver.find_elements_by_xpath("//*[@id='businessList']/*")
        #
        # # table的总行数，不包含标题
        # print("总行数:", len(table))
        #
        # # table的总列数
        #
        # # 获取某单元格的text:获取第一行第二列的text,[不算标题行]
        # row1_col3= table[1].find_elements_by_tag_name('td')[3].text
        # print("第一行第三列的text:", row1_col3)

        # 方法二：整表取出
        # 获取跟进中商机列表
        table = driver.find_element_by_xpath("//table[@id='businessList']")

        # table的总行数，不包含标题
        table_cows = table.find_elements_by_tag_name('tr')
        print("总行数:", len(table_cows))

        # table的总列数
        row1_cols = table_cows[1].find_elements_by_tag_name('td')
        print("总列数:", len(row1_cols))

        # 获取某单元格的text:获取第一行第二列的text，获取商机业态,[不算标题行]
        if len(table_cows) > 1:
            row1_col2 = table_cows[1].find_elements_by_tag_name('td')[2].text
        print("第一行第三列的text:", row1_col2)

        # 进行下单操作
        if len(table_cows) > 1:
            right_table = driver.find_element_by_xpath("//div[@class='DTFC_RightBodyLiner']/table")
            operation_col = right_table.find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[-1]
            operation_col.find_elements_by_tag_name('a')[-1].click()
            time.sleep(1)

            # # 此行代码用来定位当前页面
            # current_window = driver.current_window_handle
            # time.sleep(3)
            # 获取所有窗口，并切换至新打开页签
            all_h = driver.window_handles
            driver.switch_to.window(all_h[0])
            time.sleep(1)

            driver.switch_to.frame(driver.find_element_by_xpath(
                "//iframe[contains(@src,'/orf/order/businessOrder.shtml?')]"))
            # 刷新下单页面，需要等待刷新时间
            time.sleep(3)

            # 设置借贷人
            # 获取借贷人信息表
            loans_table = driver.find_element_by_id('loansTable')
            loans_table_cows = loans_table.find_elements_by_tag_name('tr')
            # 设置第一个借贷人信息
            loans_table_cows[2].find_element_by_name('lenderStatus').click()
            Select(loans_table_cows[2].find_element_by_name('lenderStatus')).select_by_visible_text(u"主借贷人")
            loans_table_cows[2].find_element_by_name('name').click()
            loans_table_cows[2].find_element_by_name('name').clear()
            loans_table_cows[2].find_element_by_name('name').send_keys("第一个借贷人")
            loans_table_cows[2].find_element_by_name('idCard').click()
            loans_table_cows[2].find_element_by_name('idCard').clear()
            loans_table_cows[2].find_element_by_name('idCard').send_keys("429001198702060001")
            loans_table_cows[2].find_element_by_name('no').click()
            loans_table_cows[2].find_element_by_name('no').clear()
            loans_table_cows[2].find_element_by_name('no').send_keys("13708010001")
            loans_table_cows[2].find_element_by_name('maritalStatus').click()
            Select(loans_table_cows[2].find_element_by_name('maritalStatus')).select_by_visible_text(u"已婚")
            loans_table_cows[2].find_element_by_name('childrenNum').click()
            loans_table_cows[2].find_element_by_name('childrenNum').clear()
            loans_table_cows[2].find_element_by_name('childrenNum').send_keys("1")
            loans_table_cows[2].find_element_by_name('noKnow').click()
            Select(loans_table_cows[2].find_element_by_name('noKnow')).select_by_visible_text(u"知晓")
            loans_table_cows[2].find_element_by_name('relationshipOfCus').click()
            Select(loans_table_cows[2].find_element_by_name('relationshipOfCus')).select_by_visible_text(u"本人")
            loans_table_cows[2].find_element_by_name('isSelf').click()
            Select(loans_table_cows[2].find_element_by_name('isSelf')).select_by_visible_text(u"是")

            # 如果需要新建一个借贷人，则需要点击‘新增一行’，然后进行参数的填写
            # driver.find_element_by_link_text('新增一行').click()
            loans_table_cows[-1].find_element_by_link_text('新增一行').click()
            # 重新获取借贷人信息表，因为新增一行后，整表刷新过一次
            loans_table = driver.find_element_by_id('loansTable')
            loans_table_cows = loans_table.find_elements_by_tag_name('tr')
            # 第二个借贷人信息
            loans_table_cows[3].find_element_by_name('lenderStatus').click()
            Select(loans_table_cows[3].find_element_by_name('lenderStatus')).select_by_visible_text(u"次借贷人")
            loans_table_cows[3].find_element_by_name('name').click()
            loans_table_cows[3].find_element_by_name('name').clear()
            loans_table_cows[3].find_element_by_name('name').send_keys("第二个借贷人")
            loans_table_cows[3].find_element_by_name('idCard').click()
            loans_table_cows[3].find_element_by_name('idCard').clear()
            loans_table_cows[3].find_element_by_name('idCard').send_keys("429001198702060002")
            loans_table_cows[3].find_element_by_name('no').click()
            loans_table_cows[3].find_element_by_name('no').clear()
            loans_table_cows[3].find_element_by_name('no').send_keys("13708010002")
            loans_table_cows[3].find_element_by_name('maritalStatus').click()
            Select(loans_table_cows[3].find_element_by_name('maritalStatus')).select_by_visible_text(u"未婚")
            loans_table_cows[3].find_element_by_name('childrenNum').click()
            loans_table_cows[3].find_element_by_name('childrenNum').clear()
            loans_table_cows[3].find_element_by_name('childrenNum').send_keys("0")
            loans_table_cows[3].find_element_by_name('noKnow').click()
            Select(loans_table_cows[3].find_element_by_name('noKnow')).select_by_visible_text(u"知晓")
            loans_table_cows[3].find_element_by_name('relationshipOfCus').click()
            Select(loans_table_cows[3].find_element_by_name('relationshipOfCus')).select_by_visible_text(u"夫妻")
            loans_table_cows[3].find_element_by_name('isSelf').click()
            Select(loans_table_cows[3].find_element_by_name('isSelf')).select_by_visible_text(u"否")
            time.sleep(1)

            # 如果需要删除一个借贷人，则需要点击‘删除’
            loans_table_cows[3].find_elements_by_tag_name('td')[-1].find_elements_by_tag_name('a')[-1].click()
            # time.sleep(2)

            # 设置合同约定
            driver.find_element_by_id("loansAmountId").click()
            driver.find_element_by_id("loansAmountId").clear()
            driver.find_element_by_id("loansAmountId").send_keys("36")
            driver.find_element_by_id("loansNumId").click()
            driver.find_element_by_id("loansNumId").clear()
            driver.find_element_by_id("loansNumId").send_keys("10")
            driver.find_element_by_id("loansInterestId").click()
            driver.find_element_by_id("loansInterestId").clear()
            driver.find_element_by_id("loansInterestId").send_keys("1")
            driver.find_element_by_id("loansRateTypeId").click()
            Select(driver.find_element_by_id("loansRateTypeId")).select_by_visible_text(u"日息")
            driver.find_element_by_id("earnestMoneyId").click()
            driver.find_element_by_id("earnestMoneyId").clear()
            driver.find_element_by_id("earnestMoneyId").send_keys("3600")

            # 设置办理业务
            # 获取业务信息表
            order_business_table = driver.find_element_by_id('orderBusinesId')
            order_business_table_cows = order_business_table.find_elements_by_tag_name('tr')
            # 设置第一个办理的业务信息
            order_business_table_cows[2].find_element_by_name('btName').click()
            Select(order_business_table_cows[2].find_element_by_name('btName')).select_by_visible_text(u"资金业务")
            order_business_table_cows[2].find_element_by_name('productName').click()
            # 刷新产品列表，需要等待刷新时间
            time.sleep(5)

            # 选择产品
            driver.find_element_by_id("btId").click()
            Select(driver.find_element_by_id("btId")).select_by_visible_text(u"资金业务")
            # Select(driver.find_element_by_id("productId")).select_by_index(1)
            # Select(driver.find_element_by_id("channelList")).select_by_index(1)
            time.sleep(2)
            driver.find_element_by_xpath("//button[@onclick='submitBusParam()']").click()
            time.sleep(5)
            product_table = driver.find_element_by_id('productTable')
            product_table_cows = product_table.find_elements_by_tag_name('tr')
            for index in range(len(product_table_cows)):
                # 选中状态
                checked = False
                # 首行不判断
                if index is not 0:
                    business_format = product_table_cows[index].find_elements_by_tag_name('td')[3].text
                    if business_format == '空放':
                        # if product_table_cows[index].is_selected is False:
                        #     print("000000000000")
                        product_table_cows[index].click()
                        checked = True
                if checked is True:
                    break
            time.sleep(1)
            driver.find_element_by_link_text('保存').click()
            time.sleep(1)
            order_business_table_cows[2].find_element_by_name('serviceCharge').click()
            order_business_table_cows[2].find_element_by_name('serviceCharge').clear()
            order_business_table_cows[2].find_element_by_name('serviceCharge').send_keys("1")
            order_business_table_cows[2].find_element_by_name('rateType').click()
            Select(order_business_table_cows[2].find_element_by_name('rateType')).select_by_visible_text(u"日息")
            order_business_table_cows[2].find_element_by_name('loansAmount').click()
            order_business_table_cows[2].find_element_by_name('loansAmount').clear()
            order_business_table_cows[2].find_element_by_name('loansAmount').send_keys("36")
            order_business_table_cows[2].find_element_by_name('contractNo').click()
            order_business_table_cows[2].find_element_by_name('contractNo').clear()
            order_business_table_cows[2].find_element_by_name('contractNo').send_keys("CD13708010002")
            Select(order_business_table_cows[2].find_element_by_name('channel')).select_by_index(1)
            Select(order_business_table_cows[2].find_element_by_name('flowUserName')).select_by_index(1)

            # 如果需要新增一个业务，则需要点击‘新增一行’，然后进行参数的填写
            # driver.find_element_by_link_text('新增一行').click()
            order_business_table_cows[-1].find_element_by_link_text('新增一行').click()

            # 重新获取业务信息表，因为新增一行后，整表刷新过一次
            order_business_table = driver.find_element_by_id('orderBusinesId')
            order_business_table_cows = order_business_table.find_elements_by_tag_name('tr')
            # 第二个业务信息
            order_business_table_cows[3].find_element_by_name('btName').click()
            Select(order_business_table_cows[3].find_element_by_name('btName')).select_by_visible_text(u"资金业务")
            order_business_table_cows[3].find_element_by_name('productName').click()
            # 刷新产品列表，需要等待刷新时间
            time.sleep(5)

            # 选择产品
            driver.find_element_by_id("btId").click()
            Select(driver.find_element_by_id("btId")).select_by_visible_text(u"资金业务")
            # Select(driver.find_element_by_id("productId")).select_by_index(1)
            # Select(driver.find_element_by_id("channelList")).select_by_index(1)
            time.sleep(2)
            driver.find_element_by_xpath("//button[@onclick='submitBusParam()']").click()
            time.sleep(5)
            product_table = driver.find_element_by_id('productTable')
            product_table_cows = product_table.find_elements_by_tag_name('tr')

            for index in range(len(product_table_cows)):
                # 选中状态
                checked = False
                # 首行不判断
                if index is not 0:
                    business_format = product_table_cows[index].find_elements_by_tag_name('td')[3].text
                    if business_format == '空放':
                        # if product_table_cows[index].is_selected is False:
                        #     print("000000000000")
                        product_table_cows[index].click()
                        checked = True
                if checked is True:
                    break
            time.sleep(1)
            driver.find_element_by_link_text('保存').click()
            time.sleep(1)
            order_business_table_cows[3].find_element_by_name('serviceCharge').click()
            order_business_table_cows[3].find_element_by_name('serviceCharge').clear()
            order_business_table_cows[3].find_element_by_name('serviceCharge').send_keys("1")
            order_business_table_cows[3].find_element_by_name('rateType').click()
            Select(order_business_table_cows[3].find_element_by_name('rateType')).select_by_visible_text(u"日息")
            order_business_table_cows[3].find_element_by_name('loansAmount').click()
            order_business_table_cows[3].find_element_by_name('loansAmount').clear()
            order_business_table_cows[3].find_element_by_name('loansAmount').send_keys("36")
            order_business_table_cows[3].find_element_by_name('contractNo').click()
            order_business_table_cows[3].find_element_by_name('contractNo').clear()
            order_business_table_cows[3].find_element_by_name('contractNo').send_keys("CD13708010003")
            Select(order_business_table_cows[3].find_element_by_name('channel')).select_by_index(1)
            Select(order_business_table_cows[3].find_element_by_name('flowUserName')).select_by_index(1)

            time.sleep(1)

            # 如果需要删除一个业务信息，则需要点击‘删除’
            order_business_table_cows[3].find_elements_by_tag_name('td')[-1].find_elements_by_tag_name('a')[-1].click()
            time.sleep(2)

            # 设置抵押物地址
            driver.find_element_by_id('mortgageAddress').click()
            driver.find_element_by_id('mortgageAddress').clear()
            driver.find_element_by_id('mortgageAddress').send_keys("抵押物地址")

            # 设置包装费
            # 获取业务信息表
            subject_table = driver.find_element_by_id('subjectId')
            subject_table_cows = subject_table.find_elements_by_tag_name('tr')
            # 设置第一个科目的包装费信息
            subject_table_cows[2].find_element_by_name('subjectName').click()
            Select(subject_table_cows[2].find_element_by_name('subjectName')).select_by_visible_text(u"刻章费")
            subject_table_cows[2].find_element_by_name('subjectNum').click()
            subject_table_cows[2].find_element_by_name('subjectNum').clear()
            subject_table_cows[2].find_element_by_name('subjectNum').send_keys("2")
            subject_table_cows[2].find_element_by_name('subjectPrice').click()
            subject_table_cows[2].find_element_by_name('subjectPrice').clear()
            subject_table_cows[2].find_element_by_name('subjectPrice').send_keys("20")
            subject_table_cows[2].find_element_by_name('subjectContractNo').click()
            subject_table_cows[2].find_element_by_name('subjectContractNo').clear()
            subject_table_cows[2].find_element_by_name('subjectContractNo').send_keys("CD13708010002_1")

            # 如果需要新增一个科目的包装费，则需要点击‘新增一行’，然后进行参数的填写
            subject_table_cows[-1].find_element_by_link_text('新增一行').click()

            # 重新获取业务信息表，因为新增一行后，整表刷新过一次
            subject_table = driver.find_element_by_id('subjectId')
            subject_table_cows = subject_table.find_elements_by_tag_name('tr')
            # 第二个科目的包装费信息
            subject_table_cows[3].find_element_by_name('subjectName').click()
            Select(subject_table_cows[3].find_element_by_name('subjectName')).select_by_visible_text(u"刻章费")
            subject_table_cows[3].find_element_by_name('subjectNum').click()
            subject_table_cows[3].find_element_by_name('subjectNum').clear()
            subject_table_cows[3].find_element_by_name('subjectNum').send_keys("2")
            subject_table_cows[3].find_element_by_name('subjectPrice').click()
            subject_table_cows[3].find_element_by_name('subjectPrice').clear()
            subject_table_cows[3].find_element_by_name('subjectPrice').send_keys("20")
            subject_table_cows[3].find_element_by_name('subjectContractNo').click()
            subject_table_cows[3].find_element_by_name('subjectContractNo').clear()
            subject_table_cows[3].find_element_by_name('subjectContractNo').send_keys("CD13708010002_1")
            time.sleep(1)

            # 如果需要删除一个科目的包装费信息，则需要点击‘删除’
            subject_table_cows[3].find_elements_by_tag_name('td')[-1].find_elements_by_tag_name('a')[-1].click()
            time.sleep(2)

            # 客户属性
            driver.find_element_by_link_text(u"编辑").click()
            # 刷新客户属性页面，需要等待刷新时间
            time.sleep(8)

            # 设置房产信息
            house_pay_type_elements = driver.find_elements_by_xpath(
                "//*[@type='radio' and contains(@name,'payType') and contains(@name,'attrBuildings')]")
            house_pay_type_value = '按揭房'
            house_pay_type_dict = {'全款房': 0, '按揭房': 1, '无': 2}
            house_type_value = '住宅'
            house_type_dict = {'住宅': 0, '商铺': 1, '别墅': 2, '厂房': 3, '写字楼': 4, '安置房': 5,
                               '经济适用房': 6, '政策性住房': 7}
            house_position_value = '主城区'
            house_position_dict = {'主城区': 0, '郊区': 1, '外地': 2}
            house_area_value = '60㎡以下'
            house_area_dict = {'60㎡以下': 0, '60㎡~80㎡': 1, '80㎡~140㎡': 2, '140㎡~180㎡': 3, '180㎡以上': 4}
            house_certificate_value = '与他人共有'
            house_certificate_dict = {'与他人共有': 0, '夫妻共有': 1, '单独所有': 2, '无': 3}
            house_mortgage_bank_value = '中国银行'
            house_mortgage_bank_dict = {'请选择': 0, '中国银行': 1, '建设银行': 2, '农业银行': 3, '工商银行': 4, '交通银行': 5,
                                        '兴业银行': 6}
            house_mortgage_way_value = '商贷'
            house_mortgage_way_dict = {'商贷': 0, '公积金': 1, '公积金+商贷': 2}
            house_repayment_way_value = '等额本息'
            house_repayment_way_dict = {'等额本息': 0, '等额本金': 1, '先息后本': 2, '组合还款': 3, '其它方式': 4}
            # 设置房屋付款类型的信息
            house_pay_type_index = house_pay_type_dict[house_pay_type_value]
            house_pay_type_elements[house_pay_type_index].click()
            time.sleep(1)
            # 设置全款房或按揭房的公共信息
            if house_pay_type_value == '全款房' or house_pay_type_value == '按揭房':
                # 设置房屋类型
                house_type_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'buildingType') and contains(@name,'attrBuildings')]")
                house_type_index = house_type_dict[house_type_value]
                house_type_elements[house_type_index].click()
                time.sleep(1)
                # 设置建立时间
                house_built_time_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'builtUpTime') and contains(@name,'attrBuildings')]")
                house_built_time_element.click()
                time.sleep(1)
                driver.switch_to.parent_frame()
                driver.switch_to.frame(3)
                driver.find_element_by_xpath("//td[@onclick='day_Click(2016, 1, 1,0,0,0);']").click()
                time.sleep(1)
                driver.switch_to.parent_frame()
                driver.switch_to.frame(2)
                # 设置房屋位置
                house_position_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'buildingPosition') and contains(@name,'attrBuildings')]")
                house_position_index = house_position_dict[house_position_value]
                house_position_elements[house_position_index].click()
                time.sleep(1)
                # 设置房屋面积
                house_area_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'buildingArea') and contains(@name,'attrBuildings')]")
                house_area_index = house_area_dict[house_area_value]
                house_area_elements[house_area_index].click()
                time.sleep(1)
                # 设置市场价格
                house_market_price_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'marketPrice') and contains(@name,'attrBuildings')]")
                house_market_price_element.click()
                house_market_price_element.clear()
                house_market_price_element.send_keys(u'100')
                # 设置房产证
                house_certificate_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'certificate') and contains(@name,'attrBuildings')]")
                house_certificate_index = house_certificate_dict[house_certificate_value]
                house_certificate_elements[house_certificate_index].click()
                time.sleep(1)
            # 设置按揭房的额外信息
            if house_pay_type_value == '按揭房':
                # 设置按揭银行
                house_mortgage_bank_element = driver.find_element_by_xpath(
                    "//select[contains(@name,'mortgageBank') and contains(@name,'attrBuildings')]")
                house_mortgage_bank_index = house_mortgage_bank_dict[house_mortgage_bank_value]
                Select(house_mortgage_bank_element).select_by_index(house_mortgage_bank_index)
                # 设置按揭金额
                house_mortgage_amount_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'mortgageAmount') and contains(@name,'attrBuildings')]")
                house_mortgage_amount_element.click()
                house_mortgage_amount_element.clear()
                house_mortgage_amount_element.send_keys(u'50')
                # 设置按揭开始时间
                house_mortgage_time_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'mortgageTime') and contains(@name,'attrBuildings')]")
                house_mortgage_time_element.click()
                time.sleep(1)
                driver.switch_to.parent_frame()
                driver.switch_to.frame(3)
                driver.find_element_by_xpath("//td[@onclick='day_Click(2018,3,6);']").click()
                time.sleep(1)
                driver.switch_to.parent_frame()
                driver.switch_to.frame(2)
                # 设置月供
                house_month_pay_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'monthPay') and contains(@name,'attrBuildings')]")
                house_month_pay_element.click()
                house_month_pay_element.clear()
                house_month_pay_element.send_keys(u'50')
                # 设置按揭年限
                house_mortgage_years_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'mortgageYears') and contains(@name,'attrBuildings')]")
                house_mortgage_years_element.click()
                house_mortgage_years_element.clear()
                house_mortgage_years_element.send_keys(u'20')
                # 设置按揭方式
                house_mortgage_way_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'mortgageWay') and contains(@name,'attrBuildings')]")
                house_mortgage_way_index = house_mortgage_way_dict[house_mortgage_way_value]
                house_mortgage_way_elements[house_mortgage_way_index].click()
                time.sleep(1)
                # 设置还款方式
                house_repayment_way_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'repaymentWay') and contains(@name,'attrBuildings')]")
                house_repayment_way_index = house_repayment_way_dict[house_repayment_way_value]
                house_repayment_way_elements[house_repayment_way_index].click()
                time.sleep(1)

            # 添加房产（添加房产参数比较复杂，且不常用，暂时先遗留）
            if house_pay_type_value != '无':
                driver.find_element_by_xpath("//a[@onclick='addHouse(this)']").click()
                time.sleep(1)
                # driver.find_element_by_xpath("//a[@onclick='removeFold(this)']").click()
                time.sleep(1)

            # 设置车辆信息
            car_pay_type_elements = driver.find_elements_by_xpath(
                "//*[@type='radio' and contains(@name,'payType') and contains(@name,'attrVehicles')]")
            car_pay_type_value = '按揭车'
            car_pay_type_dict = {'全款车': 0, '按揭车': 1, '无': 2}
            car_vehicle_brand_value = 'A_ABT'
            car_vehicle_brand_dict = {'请选择': 0, 'A_ABT': 1}
            car_vehicle_type_value = '个人名下'
            car_vehicle_type_dict = {'个人名下': 0, '公司名下': 1}
            car_is_mortgage_value = '是'
            car_is_mortgage_dict = {'是': 0, '否': 1}
            car_mortgage_way_value = '金融公司'
            car_mortgage_way_dict = {'金融公司': 0, '银行': 1, '信用卡': 2}
            car_vehicle_insurance_value = '双险'
            car_vehicle_insurance_dict = {'无': 0, '其它商业险': 1, '双险': 2, '交强险': 3}
            car_insurance_company_value = '平安'
            car_insurance_company_dict = {'平安': 1, '中国人保': 2, '太平洋': 3, '中华联合': 4}
            # 设置车辆付款类型的信息
            car_pay_type_index = car_pay_type_dict[car_pay_type_value]
            car_pay_type_elements[car_pay_type_index].click()
            time.sleep(1)
            # 设置全款车或按揭车的公共信息
            if car_pay_type_value == '全款车' or car_pay_type_value == '按揭车':
                # 设置车辆品牌
                car_vehicle_brand_element = driver.find_element_by_xpath(
                    "//select[contains(@name,'vehicleBrand')]")
                car_vehicle_brand_index = car_vehicle_brand_dict[car_vehicle_brand_value]
                Select(car_vehicle_brand_element).select_by_index(car_vehicle_brand_index)
                # 设置购车时间
                car_buying_time_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'buyingTime') and contains(@name,'attrVehicles')]")
                car_buying_time_element.click()
                # car_buying_time_element.send_keys(u'2010-03-06')
                driver.switch_to.parent_frame()
                driver.switch_to.frame(3)
                driver.find_element_by_xpath("//td[@onclick='day_Click(2018,3,6);']").click()
                time.sleep(1)
                driver.switch_to.parent_frame()
                driver.switch_to.frame(2)
                # 设置裸车价
                car_bare_car_price_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'bareCarPrice') and contains(@name,'attrVehicles')]")
                car_bare_car_price_element.click()
                car_bare_car_price_element.clear()
                car_bare_car_price_element.send_keys(u'30')
                # 设置车辆所属类型
                car_vehicle_type_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'vehicleType') and contains(@name,'attrVehicles')]")
                car_vehicle_type_index = car_vehicle_type_dict[car_vehicle_type_value]
                car_vehicle_type_elements[car_vehicle_type_index].click()
                time.sleep(1)
                # 设置车辆是否被抵押
                car_is_mortgage_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'isMortgage') and contains(@name,'attrVehicles')]")
                car_is_mortgage_index = car_is_mortgage_dict[car_is_mortgage_value]
                car_is_mortgage_elements[car_is_mortgage_index].click()
                time.sleep(1)
                # 设置车辆地域
                car_vehicle_area_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'vehicleArea') and contains(@name,'attrVehicles')]")
                car_vehicle_area_element.click()
                car_vehicle_area_element.clear()
                car_vehicle_area_element.send_keys(u'成都')
            # 设置按揭车的额外信息
            if car_pay_type_value == '按揭车':
                # 设置按揭方式
                car_mortgage_way_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'mortgageWay') and contains(@name,'attrVehicles')]")
                car_mortgage_way_index = car_mortgage_way_dict[car_mortgage_way_value]
                car_mortgage_way_elements[car_mortgage_way_index].click()
                time.sleep(1)
                # 设置按揭开始时间
                car_mortgage_time_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'mortgageTime') and contains(@name,'attrVehicles')]")
                car_mortgage_time_element.click()
                driver.switch_to.parent_frame()
                driver.switch_to.frame(3)
                driver.find_element_by_xpath("//td[@onclick='day_Click(2018,3,6);']").click()
                time.sleep(1)
                driver.switch_to.parent_frame()
                driver.switch_to.frame(2)
                # 设置按揭金额
                car_mortgage_amount_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'mortgageAmount') and contains(@name,'attrVehicles')]")
                car_mortgage_amount_element.click()
                car_mortgage_amount_element.clear()
                car_mortgage_amount_element.send_keys(u'10')
                # 设置月供
                car_month_pay_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'monthPay') and contains(@name,'attrVehicles')]")
                car_month_pay_element.click()
                car_month_pay_element.clear()
                car_month_pay_element.send_keys(u'1500')
                # 设置按揭年限
                car_mortgage_years_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'mortgageYears') and contains(@name,'attrVehicles')]")
                car_mortgage_years_element.click()
                car_mortgage_years_element.clear()
                car_mortgage_years_element.send_keys(u'2')
                # 设置车辆保险
                car_vehicle_insurance_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'vehicleInsurance') and contains(@name,'attrVehicles')]")
                car_vehicle_insurance_index = car_vehicle_insurance_dict[car_vehicle_insurance_value]
                car_vehicle_insurance_elements[car_vehicle_insurance_index].click()
                time.sleep(1)
                if car_vehicle_insurance_value != '无':
                    # 设置车辆保险公司
                    car_insurance_company_element = driver.find_element_by_xpath(
                        "//select[contains(@name,'insuranceCompany') and contains(@name,'attrVehicles')]")
                    car_insurance_company_index = car_insurance_company_dict[car_insurance_company_value]
                    Select(car_insurance_company_element).select_by_index(car_insurance_company_index)
                    time.sleep(1)
                    # 设置车辆保险金额
                    car_insurance_amount_element = driver.find_element_by_xpath(
                        "//*[@type='text' and contains(@name,'insuranceAmount') and contains(@name,'attrVehicles')]")
                    car_insurance_amount_element.click()
                    car_insurance_amount_element.clear()
                    car_insurance_amount_element.send_keys(u'2000')
            # 添加车辆（添加车辆参数比较复杂，且不常用，暂时先遗留）
            if house_pay_type_value != '无':
                driver.find_element_by_xpath("//a[@onclick='addCar(this)']").click()
                time.sleep(1)
                # driver.find_element_by_xpath("//a[@onclick='removeFold(this)']").click()
                time.sleep(1)

            # 设置保单信息
            insurance_policy_elements = driver.find_elements_by_xpath(
                "//*[@type='radio' and contains(@name,'warranty')]")
            insurance_policy_value = '有保单'
            insurance_policy_dict = {'有保单': 0, '无': 1}
            insurance_company_value = '中国人寿'
            insurance_company_dict = {'中国人寿': 1, '中国人保': 2, '中国平安': 3, '太平洋': 4}
            insurance_payment_way_value = '趸缴'
            insurance_payment_way_dict = {'趸缴': 0, '月缴': 1, '季缴': 2, '年缴': 3}
            insurance_payment_years_value = '1年'
            insurance_payment_years_dict = {'1年': 0, '2年': 1, '3年': 1, '5年': 2, '5年以上': 3}
            insurance_policy_holder_value = '本人'
            insurance_policy_holder_dict = {'本人': 0, '他人': 1}
            insurance_is_change_value = '是'
            insurance_is_change_dict = {'是': 0, '否': 1}
            # 设置保单有无
            insurance_policy_index = insurance_policy_dict[insurance_policy_value]
            insurance_policy_elements[insurance_policy_index].click()
            time.sleep(1)
            # 设置保单信息
            if insurance_policy_value == '有保单':
                # 设置保险公司
                insurance_company_element = driver.find_element_by_xpath(
                    "//select[contains(@name,'attrPolicy.insuranceCompany')]")
                insurance_company_index = insurance_company_dict[insurance_company_value]
                Select(insurance_company_element).select_by_index(insurance_company_index)
                time.sleep(1)
                # 设置缴费方式
                insurance_payment_way_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'attrPolicy.paymentWay')]")
                insurance_payment_way_index = insurance_payment_way_dict[insurance_payment_way_value]
                insurance_payment_way_elements[insurance_payment_way_index].click()
                time.sleep(1)
                # 设置缴费金额
                insurance_payment_amount_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'attrPolicy.paymentAmount')]")
                insurance_payment_amount_element.click()
                insurance_payment_amount_element.clear()
                insurance_payment_amount_element.send_keys(u'2000')
                # 设置缴费开始时间
                insurance_payment_time_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'attrPolicy.paymentTime')]")
                insurance_payment_time_element.click()
                driver.switch_to.parent_frame()
                driver.switch_to.frame(3)
                driver.find_element_by_xpath("//td[@onclick='day_Click(2018,3,6);']").click()
                time.sleep(1)
                driver.switch_to.parent_frame()
                driver.switch_to.frame(2)
                # 设置已缴费年限
                insurance_payment_years_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'attrPolicy.paymentYears')]")
                insurance_payment_years_index = insurance_payment_years_dict[insurance_payment_years_value]
                insurance_payment_years_elements[insurance_payment_years_index].click()
                time.sleep(1)
                # 设置投保人
                insurance_policy_holder_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'attrPolicy.policyHolder')]")
                insurance_policy_holder_index = insurance_policy_holder_dict[insurance_policy_holder_value]
                insurance_policy_holder_elements[insurance_policy_holder_index].click()
                time.sleep(1)
                # 设置是否变更投保人
                insurance_is_change_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'attrPolicy.isChange')]")
                insurance_is_change_index = insurance_is_change_dict[insurance_is_change_value]
                insurance_is_change_elements[insurance_is_change_index].click()
                time.sleep(1)
                # 如果变更投保人，设置变更时间
                if insurance_is_change_value == '是':
                    insurance_change_time_element = driver.find_element_by_xpath(
                        "//*[@type='text' and contains(@name,'attrPolicy.changeTime')]")
                    insurance_change_time_element.click()
                    driver.switch_to.parent_frame()
                    driver.switch_to.frame(3)
                    driver.find_element_by_xpath("//td[@onclick='day_Click(2018,3,6);']").click()
                    time.sleep(1)
                    driver.switch_to.parent_frame()
                    driver.switch_to.frame(2)

            # 设置工作信息
            job_nature_elements = driver.find_elements_by_xpath(
                "//*[@type='radio' and contains(@name,'jobNature')]")
            job_nature_value = '军人'
            job_nature_dict = {'工薪': 0, '个体户': 1, '企业主': 2, '军人': 3, '无': 4}
            job_enterprise_nature_value = '国企'
            job_enterprise_nature_dict = {'国企': 0, '事业编制': 1, '公务员': 2, '民营': 3, '无': 4}
            job_is_quality_value = '是'
            job_is_quality_dict = {'是': 0, '否': 1}
            job_wages_pay_form_value = '打卡'
            job_wages_pay_form_dict = {'打卡': 0, '现金': 1, '转账': 1, '其它': 2}
            job_business_license_value = '有'
            job_business_license_dict = {'有': 0, '无': 1}
            job_management_industry_value = '食品'
            job_management_industry_dict = {'食品': 1, '商贸': 2, '服饰': 3, '建材': 4}
            job_civilian_soldier_value = '是'
            job_civilian_soldier_dict = {'是': 0, '否': 1}
            job_own_id_card_value = '有'
            job_own_id_card_dict = {'有': 0, '无': 1}
            # 设置工作类型
            job_nature_index = job_nature_dict[job_nature_value]
            job_nature_elements[job_nature_index].click()
            time.sleep(1)
            # 设置工薪信息
            if job_nature_value == '工薪':
                # 设置企业性质
                job_enterprise_nature_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'attrJob.enterpriseNature')]")
                job_enterprise_nature_index = job_enterprise_nature_dict[job_enterprise_nature_value]
                job_enterprise_nature_elements[job_enterprise_nature_index].click()
                time.sleep(1)
                # 设置是否优质企业
                job_is_quality_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'attrJob.isQuality')]")
                job_is_quality_index = job_is_quality_dict[job_is_quality_value]
                job_is_quality_elements[job_is_quality_index].click()
                time.sleep(1)
                # 设置工资发放形式
                job_wages_pay_form_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'attrJob.wagesPayForm')]")
                job_wages_pay_form_index = job_wages_pay_form_dict[job_wages_pay_form_value]
                job_wages_pay_form_elements[job_wages_pay_form_index].click()
                time.sleep(1)
                # 设置工资
                job_wages_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'attrJob.wages')]")
                job_wages_element.click()
                job_wages_element.clear()
                job_wages_element.send_keys(u'10000')
            # 设置个体户或企业主的公共信息
            if job_nature_value == '个体户' or job_nature_value == '企业主':
                # 设置开始经营时间
                job_start_operate_time_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'attrJob.startOperateTime')]")
                job_start_operate_time_element.click()
                driver.switch_to.parent_frame()
                driver.switch_to.frame(3)
                driver.find_element_by_xpath("//td[@onclick='day_Click(2018,3,6);']").click()
                time.sleep(1)
                driver.switch_to.parent_frame()
                driver.switch_to.frame(2)
                # 设置经营流水
                job_operating_stream_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'attrJob.operatingStream')]")
                job_operating_stream_element.click()
                job_operating_stream_element.clear()
                job_operating_stream_element.send_keys(u'1000')
                # 设置营业执照
                job_business_license_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'attrJob.businessLicense')]")
                job_business_license_index = job_business_license_dict[job_business_license_value]
                job_business_license_elements[job_business_license_index].click()
                time.sleep(1)
                # 设置经营行业
                job_management_industry_element = driver.find_element_by_xpath(
                    "//select[contains(@name,'attrJob.managementIndustry')]")
                job_management_industry_index = job_management_industry_dict[job_management_industry_value]
                Select(job_management_industry_element).select_by_index(job_management_industry_index)
            # 设置企业主的额外信息
            if job_nature_value == '企业主':
                # 设置占股
                job_total_shares_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'attrJob.totalShares')]")
                job_total_shares_element.click()
                job_total_shares_element.clear()
                job_total_shares_element.send_keys(u'49.9')
            # 设置军人信息
            if job_nature_value == '军人':
                # 设置是否文职军人
                job_civilian_soldier_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'attrJob.civilianSoldier')]")
                job_civilian_soldier_index = job_civilian_soldier_dict[job_civilian_soldier_value]
                job_civilian_soldier_elements[job_civilian_soldier_index].click()
                time.sleep(1)
                # 设置是否有身份证
                job_own_id_card_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'attrJob.ownIdCard')]")
                job_own_id_card_index = job_own_id_card_dict[job_own_id_card_value]
                job_own_id_card_elements[job_own_id_card_index].click()
                time.sleep(1)
            # 设置社保信息
            social_security_elements = driver.find_elements_by_xpath(
                "//*[@type='radio' and contains(@name,'social')]")
            social_security_value = '有社保'
            social_security_dict = {'有社保': 0, '无': 1}
            social_security_purchaser_value = '本单位'
            social_security_purchaser_dict = {'本单位': 0, '本人': 1, '第三方': 2}
            # 设置社保有无
            social_security_index = social_security_dict[social_security_value]
            social_security_elements[social_security_index].click()
            time.sleep(1)
            # 设置社保信息
            if social_security_value == '有社保':
                # 设置购买人
                social_security_purchaser_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'attrSocialSecurity.purchaser')]")
                social_security_purchaser_index = social_security_purchaser_dict[social_security_purchaser_value]
                social_security_purchaser_elements[social_security_purchaser_index].click()
                time.sleep(1)
                # 设置社保基数
                social_security_base_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'attrSocialSecurity.socialSecurityBase')]")
                social_security_base_element.click()
                social_security_base_element.clear()
                social_security_base_element.send_keys(u'7000')
                time.sleep(1)
                # 设置已缴费年限
                social_security_years_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'attrSocialSecurity.socialSecurityYears')]")
                social_security_years_element.click()
                social_security_years_element.clear()
                social_security_years_element.send_keys(u'8')
                time.sleep(1)
            # 设置公积金信息
            acc_fund_elements = driver.find_elements_by_xpath(
                "//*[@type='radio' and contains(@name,'money')]")
            acc_fund_value = '有公积金'
            acc_fund_dict = {'有公积金': 0, '无': 1}
            acc_fund_purchaser_unit_value = '本单位'
            acc_fund_purchaser_unit_dict = {'本单位': 0, '第三方': 1}
            # 设置公积金有无
            acc_fund_index = acc_fund_dict[acc_fund_value]
            acc_fund_elements[acc_fund_index].click()
            time.sleep(1)
            # 设置公积金信息
            if acc_fund_value == '有公积金':
                # 设置公积金基数
                acc_fund_base_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'attrAccFund.accFundBase')]")
                acc_fund_base_element.click()
                acc_fund_base_element.clear()
                acc_fund_base_element.send_keys(u'7000')
                # 设置缴纳年限
                acc_fund_payment_years_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'attrAccFund.paymentYears')]")
                acc_fund_payment_years_element.click()
                acc_fund_payment_years_element.clear()
                acc_fund_payment_years_element.send_keys(u'8')
                # 设置购买单位
                acc_fund_purchaser_unit_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'attrAccFund.purchaseUnit')]")
                acc_fund_purchaser_unit_index = acc_fund_purchaser_unit_dict[acc_fund_purchaser_unit_value]
                acc_fund_purchaser_unit_elements[acc_fund_purchaser_unit_index].click()
                time.sleep(1)
            # 设置负债信息
            liability_elements = driver.find_elements_by_xpath(
                "//*[@type='radio' and contains(@name,'attrLiability.liabilityType')]")
            liability_value = '抵押贷款'
            liability_dict = {'抵押贷款': 0, '银行信贷': 1, '车贷': 2, '小贷': 3, '房屋抵押': 4, '无': 5}
            liability_is_overdue_value = '1年内有逾期'
            liability_is_overdue_dict = {'无': 0, '1年内有逾期': 1, '2年内有逾期': 2, '2-5年内有逾期': 3, '呆账/坏账/冻结': 4,
                                         '法院执行': 5}
            # 设置负债有无
            liability_index = liability_dict[liability_value]
            liability_elements[liability_index].click()
            time.sleep(1)
            # 设置抵押贷款或银行信贷或车贷或房屋抵押的公共信息
            if liability_value != '无':
                # 设置是否逾期
                liability_is_overdue_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'attrLiability.isOverdue')]")
                liability_is_overdue_index = liability_is_overdue_dict[liability_is_overdue_value]
                liability_is_overdue_elements[liability_is_overdue_index].click()
                time.sleep(1)
                if liability_is_overdue_value != '无':
                    # 设置逾期金额
                    liability_overdue_amount_element = driver.find_element_by_xpath(
                        "//*[@type='text' and contains(@name,'attrLiability.overdueAmount')]")
                    liability_overdue_amount_element.click()
                    liability_overdue_amount_element.clear()
                    liability_overdue_amount_element.send_keys(u'2000')
                    time.sleep(1)
                    # 设置逾期次数
                    liability_overdue_times_element = driver.find_element_by_xpath(
                        "//*[@type='text' and contains(@name,'attrLiability.overdueTimes')]")
                    liability_overdue_times_element.click()
                    liability_overdue_times_element.clear()
                    liability_overdue_times_element.send_keys(u'1')
                    time.sleep(1)
            # 设置信用卡信息attrCreditCard.isOverdraft
            credit_card_liabilities_elements = driver.find_elements_by_xpath(
                "//*[@type='radio' and contains(@name,'liabilities')]")
            credit_card_liabilities_value = '有信用卡'
            credit_card_liabilities_dict = {'有信用卡': 0, '无': 1}
            credit_card_is_overdraft_value = '是'
            credit_card_is_overdraft_dict = {'是': 0, '否': 1}
            # 设置信用卡有无
            credit_card_liabilities_index = credit_card_liabilities_dict[credit_card_liabilities_value]
            credit_card_liabilities_elements[credit_card_liabilities_index].click()
            time.sleep(1)
            # 设置信用卡信息
            if credit_card_liabilities_value == '有信用卡':
                # 设置逾期金额
                credit_card_quota_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'attrCreditCard.quota')]")
                credit_card_quota_element.click()
                credit_card_quota_element.clear()
                credit_card_quota_element.send_keys(u'100000')
                # 设置逾期次数
                credit_card_usage_quota_element = driver.find_element_by_xpath(
                    "//*[@type='text' and contains(@name,'attrCreditCard.usageQuota')]")
                credit_card_usage_quota_element.click()
                credit_card_usage_quota_element.clear()
                credit_card_usage_quota_element.send_keys(u'13999')
                # 设置是否透支
                credit_card_is_overdraft_elements = driver.find_elements_by_xpath(
                    "//*[@type='radio' and contains(@name,'attrCreditCard.isOverdraft')]")
                credit_card_is_overdraft_index = credit_card_is_overdraft_dict[credit_card_is_overdraft_value]
                credit_card_is_overdraft_elements[credit_card_is_overdraft_index].click()
                time.sleep(1)

            driver.find_element_by_link_text('保存').click()
            time.sleep(2)

            # 客户资料
            driver.find_element_by_link_text(u"选择资料").click()
            # 刷新客户资料页面，需要等待刷新时间
            time.sleep(2)

            # 客户需要选择的资料类型cus_info_list的5个元素表示（工作证明、房产证明、婚姻证明、身份证明、其它资料），没有为‘’，有多项则以':'分隔
            # 每项资料后面（），表示资料需要原件或复印件，1表示需要，0表示不需要，有多项则以','分隔
            cus_info_list = ['社保(1,0):打卡工资(0,1)', '', '结婚证(1,1)', '', '']
            cus_info_dict = {0: '工作证明', 1: '房产证明', 2: '婚姻证明', 3: '身份证明', 4: '其它资料'}
            cus_info_type_value_all_list = []
            # 设置相关资料
            for cus_info_index in range(len(cus_info_list)):
                if cus_info_list[cus_info_index] != '':
                    # 展开此项证明的相关资料
                    cus_info_switch_xpath = "//a[@title='" + cus_info_dict[cus_info_index] + \
                                            "']/preceding-sibling::span[contains(@id,'switch')]"
                    cus_info_switch_element = driver.find_element_by_xpath(cus_info_switch_xpath)
                    cus_info_switch_element.click()
                    time.sleep(1)
                    cus_info_value_str_list = cus_info_list[cus_info_index].split(':')
                    for cus_info_value_str in cus_info_value_str_list:
                        cus_info_type_value_list = cus_info_value_str.split('(')[1].split(')')[0].split(',')
                        for cus_info_type_value in cus_info_type_value_list:
                            cus_info_type_value_all_list.append(cus_info_type_value)
                        cus_info_value_list = cus_info_value_str.split('(')
                        cus_info_value_check_xpath = "//a[@title='" + cus_info_value_list[0] + \
                                                     "']/preceding-sibling::span[contains(@id,'check')]"
                        cus_info_value_check_element = driver.find_element_by_xpath(cus_info_value_check_xpath)
                        cus_info_value_check_element.click()
                        time.sleep(1)

            driver.find_element_by_link_text('保存').click()
            time.sleep(2)

            # 设置资料的原件复印件
            cus_info_type_value_all_elements = driver.find_elements_by_xpath(
                "//input[@type = 'checkbox' and contains(@name,'IdCardName')]")
            for cus_info_type_value_index in range(len(cus_info_type_value_all_list)):
                if cus_info_type_value_all_list[cus_info_type_value_index] == '1':
                    cus_info_type_value_all_elements[cus_info_type_value_index].click()
                    time.sleep(1)

            # 点击‘提交审核’按钮进行下单
            driver.find_element_by_xpath("//button[@onclick='this.disabled=true;saveOrder(this);']").click()
            time.sleep(2)
    
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True
    
    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()