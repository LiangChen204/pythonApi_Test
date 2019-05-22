#!//usr/local/bin python
# -*- coding:utf-8 -*-

"""
Created on 2019/1/14 14:57
@author: liangchen
Project: SelfTestPro
"""

# 取最新的测试报告
import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import unittest
from BSTestRunner import BSTestRunner
import time

def new_file(test_dir):
    # 列举test_dir目录下的所有文件，结果以列表形式返回
    lists = os.listdir(test_dir)
    # print(lists)
    # 对list元素根据时间进行排序
    lists.sort(key=lambda fn: os.path.getctime(test_dir + '/' + fn))

    # 获取最新文件的绝对路径
    file_path = os.path.join(test_dir, lists[-1])
    return file_path


# 发送邮件：发送最新测试报告
def send_mail(newfile):
    # 发送邮箱服务器
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "1561114132@qq.com"  # 用户名
    mail_pass = "mtwpiwskwesgfgbh"  # 口令

    sender = '1561114132@qq.com'
    receivers = ['shutiao@fanhaoyue.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # message = MIMEText(mail_message, 'html', 'utf-8')
    message = MIMEMultipart()
    message['From'] = Header("定时任务", 'utf-8')
    message['To'] = Header("邮件组", 'utf-8')
    subject = '接口日报'
    message['Subject'] = Header(subject, 'utf-8')
    message.attach(MIMEText('饭好约接口日报 邮件发送……', 'html', 'utf-8'))
    # 构造附件1，传送当前目录下的最新生成的.html 文件
    att = MIMEText(open(newfile, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    # 命名filename
    att["Content-Disposition"] = 'attachment; filename=newfile.html'
    message.attach(att)

    try:
        smtpObj = smtplib.SMTP(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

#ssl._create_default_https_context = ssl._create_unverified_context

#指定测试用例和测试报告的路径

test_daily_dir = './test_case_daily'
test_public_dir = './test_case_public'
report_dir = './reports'

#加载测试用例
discover = unittest.defaultTestLoader.discover(test_public_dir, pattern='test_mailly_flow.py')

#定义报告的文件格式
now = time.strftime("%Y-%m-%d %H_%M_%S_")
report_name = report_dir + '/' + now + 'test_report.html'

#运行用例并且生成测试报告
with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title=u'饭好约接口日报', description=u"用例执行情况")

    runner.run(discover)

newfile = new_file('reports')
send_mail(newfile)

