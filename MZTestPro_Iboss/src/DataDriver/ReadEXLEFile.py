'''
Created on 2017年2月20日

@author: fanzhaoni
'''
import xlrd
import  xdrlib ,sys
from _markupbase import _declname_match
class ReadEXLEFile(object):
    '''
    读取exle文件
    '''

    def __init__(self, filepath):
        '''
        Constructor
        '''
        self.filepath = filepath
        with  xlrd.open_workbook(self.filepath) as xlsData:
            self.xlsData = xlsData
    
    
    def GetTablehead_byindex(self,by_index=0):  #获取指定的工作薄的表头
        Tempcolnames = []
        table = self.xlsData.sheets()[by_index]
        nrows = table.nrows #行数
        if nrows > 0 :
            Tempcolnames =  table.row_values(0) #某一行数据
        return  Tempcolnames
        
        
    
    def excel_table_byindex(self,by_index=0,by_rowNo = 0):  #根据索引获取Excel表格中的数据        colnameindex：表头列名所在行的索引  ，by_index：表的索引
        colnames = self.GetTablehead_byindex(by_index)
        table = self.xlsData.sheets()[by_index]
        
        nrows = table.nrows #行数
        list =[]
            
        if nrows>1:
            if by_rowNo != 0 and by_rowNo>0 and by_rowNo<=nrows:
                row = table.row_values(by_rowNo)
                if row:
                    app = {}
                    for i in range(len(colnames)):
                        app[colnames[i]] = row[i] 
                    return app
            else:
                for rownum in range(1,nrows):
                    row = table.row_values(rownum)
                    if row:
                        app = {}
                        for i in range(len(colnames)):
                            app[colnames[i]] = row[i] 
                        list.append(app)
        return list
    
    

    def GetKeyValue_byindex(self,by_index=0,rowNum = 0,Key=""):#获取指定位置的值
        list = self.excel_table_byindex(by_index)
        return list[rowNum][Key]
    

    
    
    
    
    def GetTablehead_byname(self,by_name='Sheet1'):  #获取指定的工作薄的表头
        Tempcolnames = []
        table = self.xlsData.sheet_by_name(by_name)
        nrows = table.nrows #行数
        if nrows > 0 :
            Tempcolnames =  table.row_values(0) #某一行数据
        return  Tempcolnames
    
    def excel_table_byname(self,by_name='Sheet1',by_rowNo = 0): #根据名称获取Excel表格中的数据        colnameindex：表头列名所在行的索引  ，by_name：Sheet1名称
        colnames = self.GetTablehead_byname(by_name)
        table = self.xlsData.sheet_by_name(by_name)
        nrows = table.nrows #行数 
        list =[]
        if nrows>1:
            if by_rowNo != 0 and by_rowNo>0 and by_rowNo<=nrows:
                row = table.row_values(by_rowNo)
                if row:
                    app = {}
                    for i in range(len(colnames)):
                        app[colnames[i]] = row[i] 
                    return app
            else:
                for rownum in range(1,nrows):
                    row = table.row_values(rownum)
                    if row:
                        app = {}
                        for i in range(len(colnames)):
                            app[colnames[i]] = row[i] 
                        list.append(app)
        return list
    
    
    def GetKeyValue_byname(self,by_name='Sheet1',rowNum = 0,Key=""):
        list = self.excel_table_byname(by_name)
        return list[rowNum][Key]
    

if __name__ == '__main__':
    
    TestFile = ReadEXLEFile(filepath ="F:\\test.xls")
    tables =TestFile.excel_table_byindex(by_rowNo=1)
    for row in tables:
        print(row)

    keyValue = TestFile.GetKeyValue_byindex(Key='年龄')
    print(keyValue)
    
    tables = TestFile.excel_table_byname(by_rowNo=2)
    for row in tables:
        print(row)
      