'''
Created on 2017年2月17日

@author: fanzhaoni
'''
import sys
sys.path.append("./models")  #将models添加到系统环境变量path下面
sys.path.append("./page_obj") #将page_obj添加到系统环境变量path下面
sys.path.append("./DataDriver")#将DataDriver添加到系统环境变量path下面
sys.path.append("./page_com") #将page_com添加到系统环境变量path下面
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import unittest
import time
import os



''' 定义发送邮件 '''
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    
    
    #发送邮箱服务器
    smtpserver = "smtp.163.com"
    
    #发送邮箱
    sender = "fanzhaoni@163.com"
    #接受邮箱
    receiver = ["fanzhaoni@dgg.net"]
    #发送邮箱用户/密码
    User = "fanzhaoni@163.com"
    password = "0359422400"
    
    #文件名
    file_name = file_new.split('/')[2]
    print("输出文件名%s"% file_name)
    subject = "融资自动化测试报告"
    
    
    #HTML格式
    msg = MIMEText(mail_body,'html','utf-8')
    
    #附件格式
    att = MIMEText(mail_body,'base64','utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"]='attachment;filename=%s' % file_name
    
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot['from'] = sender
    msgRoot['to'] = ",".join(receiver)   #为多人发送邮件
    msgRoot.attach(msg)
    msgRoot.attach(att)
    
    
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(User,password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()
    print('email has send out!')
    
    
''' 查找测试报告目录，找到最新生成的测试报告文件'''
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getatime(testreport + "\\"+fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new


if __name__ == '__main__':
    print("开始测试")
    description = '环境：windows7 浏览器：Chrome'
    now = time.strftime("%Y-%m-%d-%H_%M_%S")
    filename = './report/'+now+'result.html'
    print(filename)
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='融资bms自动化测试报告',
                            description=description)
    discover = unittest.defaultTestLoader.discover('.//src/test_case', pattern='*_sta.py')
    runner.run(discover)
    fp.close()
    file_path=new_report('./report/')
    send_mail(file_path)
    
    
    
    
    
    