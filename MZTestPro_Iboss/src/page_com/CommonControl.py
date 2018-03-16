'''
Created on 2017年3月11日

@author: 20170207
'''
from selenium.webdriver.common.action_chains import ActionChains     #鼠标事件
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from page_com.base import Page
from time import sleep
from xlwt.ExcelFormulaLexer import false_pattern

class CommonControl(Page):
    '''
    基于框架的一些公共的控件
    '''
    # 按钮
    def Set_Button(self, Button_loc, Celement=None):
        ele_Button = self.IS_element_present(Button_loc, Celement)
        if ele_Button != None:
            ele_Button.click()
    
    # 输入框
    def Set_input(self, input_loc, inputtext="HT001", Celement=None):
        if inputtext != "":
            ele_input = self.IS_element_present(input_loc, Celement)
            if ele_input != None:
                ele_input.click()
                if ele_input.is_enabled() == True:
                    ele_input.clear()
                    ele_input.send_keys(inputtext)
            else:
                print("找不到", input_loc)
        
    # 是否等单选按钮
    def Set_IsButtonCheck(self, Button_loc, Buttontext="是", Celement=None):
        if Buttontext != "":
            ele_ButtonChecks = self.IS_element_present(Button_loc, Celement=Celement)
            if ele_ButtonChecks != None:
                for i in ele_ButtonChecks:
                    if i.get_attribute("value") == Buttontext:
                        i.click()
            else:
                print("找不到", Button_loc)

    # 按索引选中单选按钮
    def Set_RadioByIndex(self, radio_loc, radio_index, Celement=None):
        if radio_index != '':
            radio_elements = self.IS_elements_present(radio_loc, Celement)
            if radio_elements is not None:
                if len(radio_elements) > radio_index:
                    radio_elements[radio_index].click()
                else:
                    print('单选项这此索引项')
            else:
                print('找不到', radio_loc)
        else:
            print('不提供索引项时，无法根据索引选中对应单选项')

    # 复选按钮
    def Set_Checkbox(self, checkbox_loc, Celement=None):
        checkbox_element = self.IS_element_present(checkbox_loc, Celement)
        if checkbox_element is not None:
            checkbox_element.click()
        else:
            print('找不到', checkbox_loc)

    # 复选按钮按索引选中
    def Set_CheckboxByIndex(self, checkboxs_loc, checkbox_index, Celement=None):
        checkbox_elements = self.IS_elements_present(checkboxs_loc, Celement)
        if checkbox_elements is not None:
            checkbox_elements[checkbox_index].click()
        else:
            print('找不到', checkboxs_loc)

    # 下拉框选择
    def Set_Droplist(self, Droplist_loc, selectlist_loc, listtitle="信贷业务", Celement=None):
        if listtitle != "":
            ele_Drop = self.IS_element_present(Droplist_loc, Celement)
            if ele_Drop != None:
                ele_Drop.click()
                if self.IS_element_present(selectlist_loc, Celement)!=None:
                    Select(ele_Drop).select_by_visible_text(listtitle)
                else:
                    print("找不到", selectlist_loc)
            else:
                print("找不到", Droplist_loc)

    # 动态下拉框按索引选择
    def Set_SelectByIndex(self, select_loc, select_list_index, Celement=None):
        if select_list_index != "":
            select_element = self.IS_element_present(select_loc, Celement)
            if select_element != None:
                Select(select_element).select_by_index(select_list_index)
            else:
                print("找不到", select_loc)
        else:
            print('索引为空，无法选择下拉列表中的对应值')
            
    '''
           输入选择框   （可以支持多选）
    Select_loc--------------下拉选择框    如果没有的话就用 Select_Options_loc
    InputSelect_loc---------输入框
    Select_Options_loc------选项
    SelectText------选项内容   
    '''
    def Set_InputSelect(self, Select_loc, InputSelect_loc, Select_Options_loc, SelectText="王燕莉6302928,樊兆妮4222787", Celement=None):
        if SelectText != "":
            SelectText_arr = SelectText.strip().split(',')   # strip()去掉末尾的\n
            Select_main = self.IS_element_present(Select_loc, Celement)
            if Select_main != None:
                Select_main.click()
                InputSelect = self.IS_element_present(InputSelect_loc, Celement)
                if InputSelect != None:
                    for i in SelectText_arr:
                        InputSelect.click()
                        InputSelect.clear()
                        InputSelect.send_keys(i[0:2])
                        sleep(1)
                        Select_Options = []
                        if self.IS_elements_present(Select_Options_loc, Celement) != None:
                            Select_Options = self.find_elements(*Select_Options_loc, Celement=Celement)
                            bflag = False
                            for j in Select_Options:
                                if j.text.find(i) != -1:
                                    j.click()
                                    bflag = True
                                    break
                            if bflag == False:
                                print("没有找到当前人员，默认选择第一个")
                                Select_Options[0].click()
                        else:
                            print("找不到", Select_Options_loc)
                                    
                else:
                    print("找不到", InputSelect_loc)
            else:
                print("找不到", Select_loc)
         
        
    # 联级选择框
    def Set_CascadeSelect(self, select_loc, selecttitle="信用贷款/空放", Celement=None):
        if selecttitle != "":
            Select_element = self.IS_element_present(select_loc, Celement)
            if Select_element != None:
                Select_element.click()   # 点击选择框
                TempData = selecttitle.strip().split('/')  # 查找多级
                if len(TempData) > 0:
                    for i in TempData:
                        temp_loc = (By.LINK_TEXT, i)
                        temp_element = self.IS_element_present(temp_loc, Celement)
                        if temp_element != None:
                            temp_element.click()
                        else:
                            print("找不到 ", temp_loc)
                            break
                else:
                    print("联级选择框内容输入有误")
            else:
                print("找不到联级选择框", select_loc)
            
                
    #消息提示框   
    def GetMsgText(self):
        message_loc = (By.XPATH,"//*[starts-with(@class,'layui-layer-content layui-layer-padding')]")
        elementmessage = self.IS_ele_present(message_loc,10)
        if elementmessage != None:
            return  elementmessage.text
        else:
            return None
    
    #消息提示框，以Type类型dialog定位的
    def GetMsgTextDlalog(self):
        message_loc = (By.XPATH,"//*[@type='dialog']")
        elementmessage = self.IS_ele_present(message_loc,10)
        if elementmessage != None:
            return  elementmessage.text
        else:
            return None
        
        
    #气泡提示框
    def GetBubbleText(self):
        Bubble_loc = (By.XPATH,"//*[@class='layui-layer-content']")
        Bubble = self.IS_element_present(Bubble_loc)
        if Bubble != None:
            return Bubble.text
        else:
            return None
        
    #red提示框
    def GetRedText(self):
        Red_loc = (By.XPATH,"//*[@class='red']")
        Red = self.IS_element_present(Red_loc)
        if Red != None:
            return Red.TEXT
        else:
            return None
           
    # 显示等待判断元素是否存在
    def IS_ele_present(self,loc,time,Celement=None):   
        try:
            if Celement is None:
                sub_driver = self.driver
                print("sub_driver = self.driver")
            else:
                sub_driver= Celement
            bElement = WebDriverWait(sub_driver,time).until(lambda x: x.find_element(*loc))
            return bElement
        except:
            return None
    # 判断元素是否存在
    def IS_element_present(self, loc, Celement=None):
        try:
            bElement = self.find_element(*loc, Celement=Celement)
            return bElement
        except:
            return None
            
    # 判断多个元素是否存在
    def IS_elements_present(self, loc, Celement=None):
        try:
            bElements = self.find_elements(*loc, Celement=Celement)
            return bElements
        except:
            return None
                    
        
    
# class Tablegrid(Page):  
#     '''
#     表格操作
#     '''   
#     def         
#        
if __name__ == '__main__':
    pass