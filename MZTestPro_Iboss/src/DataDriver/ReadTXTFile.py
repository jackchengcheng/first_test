'''
Created on 2017年2月20日

@author: fanzhaoni
'''


class ReadTXTFile(object):
    '''
    用于读取txt格式的文件
    '''
    def __init__(self, filepath):
        '''
        初始化将文件内容读取内存中，然后关闭文件
        '''
        self.filepath = filepath
        #print(self.filepath)
        #方法一：不安全
        '''
        Test_file = open(self.filepath, 'r')
        All_line = Test_file.readlines()
        Test_file.close()
        '''
        
        with open(self.filepath, 'r') as Test_file:
            self.All_line = Test_file.readlines()
            self.length = len(self.All_line)
    
    #文件行数
    def GetfileLength(self):
        return self.length
    
    #读取相应的字段 (固定字段)
    def GetIndexData(self,Columnindex,lineindex = 255):
        
        self.Index_Data = []
        if lineindex !=255 and lineindex < self.length:
            TempData = self.All_line[lineindex].strip().split(',')
            if Columnindex < len(TempData):
                self.Index_Data.append(TempData[Columnindex]) 
        elif lineindex == 255:
            for line in self.All_line:
                TempData = line.strip().split(',')
                if Columnindex < len(TempData):
                    self.Index_Data.append(TempData[Columnindex]) 
        else:
            return self.Index_Data    
        return self.Index_Data
    
    #直接读取一行所有数据
    def GetLineData(self,lineIndex):
        
        if lineIndex > self.length:
            return []
        L_Data = self.All_line[lineIndex].strip()     #strip() 去掉末尾的\n
        self.Line_Data =L_Data.split(',')
        return self.Line_Data    
    
            
if __name__ == '__main__':
    Testfile = ReadTXTFile(filepath="F:\\test.txt")
    FileLen = Testfile.GetfileLength()
    print(Testfile.GetIndexData(1))
    print(Testfile.GetLineData(1))
    
                   
        
        
       
        