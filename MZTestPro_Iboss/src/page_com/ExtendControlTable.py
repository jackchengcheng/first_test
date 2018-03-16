"""
Created on 2018年3月9日

@author: 王贝贝 89144029
"""

from selenium.webdriver.common.by import By
from page_com.CommonControl import CommonControl


class ExtendControlTable(CommonControl):
    """
    基于公共控件的一些扩展控件Table
    """
    # 按行索引找对应行
    def Select_TableRowByRowNum(self, table_loc, table_row_num, table_row_tag='tr'):
        if table_row_num > -1:
            if self.IS_element_present(table_loc):
                # 获取列表的行数，用于判断列表中是否有数据
                table_rows = self.find_element(*table_loc).find_elements(By.TAG_NAME, table_row_tag)
                # 确认去掉首行后，还要有业务数据
                if len(table_rows) > 1 and len(table_rows) > table_row_num:
                    return table_rows[table_row_num]
                else:
                    print("列表中无业务数据或无此索引行", table_loc, table_row_num)
                    return None
            else:
                print("页面找不到列表元素", table_loc)
                return None
        else:
            print("行索引为负值，无法查找", table_row_num)
            return None

    # 按某值和某列的值找对应行
    # 如提供值所在的列，查找效率会提升，否则遍历查找
    def Select_TableRowByValue(self, table_loc, key_value, table_col_num=None, table_row_tag='tr', table_col_tag='td'):
        if self.IS_element_present(table_loc):
            # 获取列表的行数，用于判断列表中是否有数据
            table_rows = self.find_element(*table_loc).find_elements(By.TAG_NAME, table_row_tag)
            # 确认去掉首行后，还要有业务数据
            if len(table_rows) > 1:
                # 是否查找到的标识
                be_checked = False
                # 如跟进中商机列表中，查询客户名称或客户号包含‘****’的行
                if key_value is not None:
                    for table_row_index in range(len(table_rows)):
                        if table_row_index != 0:
                            table_cols = table_rows[table_row_index].find_elements(By.TAG_NAME, table_col_tag)
                            if table_col_num is None:
                                for table_col in table_cols:
                                    if key_value in table_col.text:
                                        be_checked = True
                                        return table_rows[table_row_index]
                            else:
                                if key_value in table_cols[table_col_num]:
                                    be_checked = True
                                    return table_rows[table_row_index]
                    if be_checked is False:
                        print("列表中找不到此值", key_value)
                        return None
                else:
                    print("查找值都不给，查找啥呀?!", key_value)
                    return None
        else:
            print("页面找不到列表元素", table_loc)
            return None

    # 列表行按列索引返回对应的列
    def Select_TableColByColNum(self, table_row_element, table_col_num, table_col_tag='td'):
        table_cols = table_row_element.find_elements(By.TAG_NAME, table_col_tag)
        if len(table_cols) > table_col_num:
            return table_cols[table_col_num]
        else:
            print("列表行中无此索引列", table_row_element, table_col_num)
            return None

    # 列表格按控件定位返回对应的控件
    def Select_TableControlByControlLoc(self, table_element, control_loc):
        if self.IS_element_present(control_loc, table_element):
            return self.find_element(*control_loc, Celement=table_element)
        else:
            print("列表行中无此控件", table_element, control_loc)

    # 列表格按列定位返回对应的控件列表
    def Select_TableControlsByControlLoc(self, table_element, control_loc):
        if self.IS_element_present(control_loc, table_element):
            return self.find_elements(*control_loc, Celement=table_element)
        else:
            print("列表行中无此控件", table_element, control_loc)

    # 控件列表中找到对应控件
    def Select_TableControlByControlNum(self, table_elements, control_num):
        if len(table_elements) > control_num:
            return table_elements[control_num]
        else:
            print("列表列表中无此索引对应控件", table_elements, control_num)

    # 列表行复选框
    def Select_CheckboxTableRow(self, table_row_element):
        table_row_element.click()