'''
Created on 2017年2月16日

@author: fanzhaoni
'''

class Page(object):
    '''
    页面基础类，用于所有页面的继承
    '''

    RzBms_url = 'https://192.168.254.80:8037'

    def __init__(self, selenium_driver,base_url = RzBms_url,parent = None):
        '''
        Constructor
        '''
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent
    
    def _open(self,url):
        url = self.base_url +url
        print("url=%s" % url)
        self.driver.get(url)
        assert self.on_page(),'Did not land on %s' % url     #断言打开网页是否成功
        
    def find_element(self,*loc,Celement = None):
        if Celement is None:
            return self.driver.find_element(*loc)
        else:
            return Celement.find_element(*loc)
    
    def find_elements(self,*loc,Celement = None):
        if Celement is None:
            return self.driver.find_elements(*loc)
        else:
            return Celement.find_elements(*loc)
    #表单切换
    def switch_frame(self,*loc):
        return self.driver.switch_to_frame(*loc)
    #窗口切换
    def switch_windows(self,*loc):
        return self.driver.switch_to_window(*loc)
    
    #消息框切换
    def switch_Alert(self):
        return self.driver.switch_to_alert()
    
    #获取主窗口
    def Getmainwindows(self):
        return self.driver.current_window_handle
    
    def open(self):
        self._open(self.url)
        
    def on_page(self):
        return self.driver.current_url == (self.base_url +self.url)
    
    def script(self,src):
        return self.driver.execute_script(src) 
    
    #隐性等待，最长等30秒 
    def wait(self,stime):
        return self.driver.implicitly_wait(stime)
     
    
        
        