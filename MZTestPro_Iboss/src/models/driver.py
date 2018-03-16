'''
Created on 2017年2月16日

@author: fanzhaoni
'''

from selenium.webdriver import Remote
from selenium import webdriver
from asyncio.tasks import sleep



#启动浏览器驱动
def browser():
    
    # 加启动配置 （用于去掉启动浏览器出现‘Chrome正在受到自动软件的控制’）
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')

    # 打开chrome浏览器
    driver = webdriver.Chrome(chrome_options=option)
    '''host = '127.0.0.1:4444' #运行主机：端口号（本机默认：127.0.0.1：4444）
    dc = {'browserName':'chrome'}  #指定浏览器（'chrome','firefor',）
    driver = Remote(command_executor='http://'+host+'/wd/nub',
                    desired_capabilities=dc)'''
    return driver
if __name__ == '__main__':
    dr =browser()
    dr.get("http://172.16.0.25:8011")
    sleep(10)
    dr.quit()
    
    
    