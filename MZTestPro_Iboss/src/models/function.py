'''
Created on 2017年2月16日

@author: fanzhaoni
'''
import os
from selenium import webdriver
from models.driver import browser


#截图函数
def insert_img(driver,file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/src')[0]
    file_path = base +"/report/image/"+file_name
    print(file_path)
    driver.get_screenshot_as_file(file_path)

#返回data路径
def Get_datafilepath(file_name):  
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/src')[0]
    file_path = base +"/data/"+file_name
    return  file_path

    
if __name__ == '__main__':
    driver = browser()
    driver.get("http://172.16.0.25:8011")
    insert_img(driver, 'rzbms.jpg')
    driver.quit()
    