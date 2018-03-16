'''
Created on 2017年2月20日

@author: 20170207
'''
import csv
from idlelib.iomenu import encoding

class ReadCSVFilelist(object):
    '''
    读取CSV文件
    '''
    def __init__(self, filepath):
        '''
        初始化将文件内容读取内存中，然后关闭文件
        '''
        self.filepath = filepath
        with open(self.filepath, encoding='utf-8') as Test_file:
            self.AllData = csv.reader(Test_file)
            self.length = self.AllData.line_num
    #文件行数
    def GetfileLength(self):
        return self.length
    
    #读取相应的字段 (Columnindex,lineindex)
    def GetIndexData(self,Columnindex=0,lineindex=0):
        self.Index_Data = []
        if lineindex < self.length:
            TempData = self.AllData[lineindex]
            if Columnindex < len(TempData):
                self.Index_Data.append(TempData[Columnindex])    
        return self.Index_Data
        
    #直接读取一行所有数据
    def GetLineData(self,lineIndex=0):
        self.Line_Data = []
        if lineIndex < self.length:
            self.Line_Data =self.All_line[lineIndex]
        return self.Line_Data    


class ReadCSVFiledict(object):
    '''
    读取CSV文件
    '''
    def __init__(self, filepath):    
        '''
        初始化将文件内容读取内存中，然后关闭文件
        '''
        self.filepath = filepath
        with open(self.filepath,encoding="utf-8") as Test_file:
            AllData = csv.DictReader(Test_file)
            
            #将OrderedDict有序字典序列存放在list中
            self.LDict =[]
            for d in AllData:
                self.LDict.append(d)
            self.length = len(self.LDict)
            #获取key值
            self.keys = AllData.fieldnames
            

    
    #文件行数
    def GetfileLength(self):
        return self.length
    #获取keys
    def Getkeys(self):
        return self.keys
           
    #读取指定的“键-值”数据
    def GetKeyData(self,keynalue = "Column1",lineindex=0):
        if  lineindex < self.length:
            TempData = self.LDict[lineindex]
            return TempData.key(keynalue,"no key")
        return " error:index bound"
        
    #直接读取一行所有数据
    def GetLineData(self,lineIndex=0):
        self.Line_Data = []
        if lineIndex < self.length:
            return self.LDict[lineIndex]
        
        return " error:index bound"   
            
if __name__ == '__main__':
    
    #list测试
    
#     Testfile = ReadCSVFilelist(filepath="F:\\test.csv")
#     FileLen = Testfile.GetfileLength()
#     print(FileLen)
#     print(Testfile.GetIndexData(0))
#     print(Testfile.GetLineData(0))  
    
    
    #dict测试
#     for d in csv.DictReader(open("F:\\test.csv",encoding="utf-8")):  
#         print(d)  
    Testfile = ReadCSVFiledict(filepath="F:\\test.csv")
    print(Testfile.GetfileLength())  
    print(Testfile.Getkeys())