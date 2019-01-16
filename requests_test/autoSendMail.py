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


def new_file(test_dir):
    # 列举test_dir目录下的所有文件，结果以列表形式返回
    lists = os.listdir(test_dir)
    # print(lists)
    # 对list元素根据时间进行排序
    lists.sort(key=lambda fn: os.path.getctime(test_dir + '/' + fn))

    # 获取最新文件的绝对路径
    file_path  = os.path.join(test_dir, lists[-1])
    print(file_path)
    return file_path

# 发送邮件：发送最新测试报告
def send_mail(newfile):
    # 打开文件
    f = open(newfile, 'rb')
    # 读取文件内容
    mail_message = f.read()
    # 关闭文件
    f.close()

    # 发送邮箱服务器
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "1561114132@qq.com"  # 用户名
    mail_pass = "mtwpiwskwesgfgbh"  # 口令

    sender = '1561114132@qq.com'
    receivers = ['shutiao@fanhaoyue.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 编写HTML类型的邮件正文
    # msg = MIMEMultipart('mixed')
    # msg_html1 = MIMEText(mail_message, 'html', 'utf-8')
    # msg.attach(msg_html1)
    #
    # msg_html = MIMEText(mail_message, 'html', 'utf-8')
    # msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    # msg.attach(msg_html)
    # msg = MIMEText(mail_message, 'html', 'utf-8')
    # msg['From'] = Header("薯条QQ邮箱", 'utf-8')
    # msg['To'] = Header("薯条公司邮箱", 'utf-8')


    message = MIMEText(mail_message, 'html', 'utf-8')
    message['From'] = Header("薯条QQ邮箱", 'utf-8')
    message['To'] = Header("薯条公司邮箱", 'utf-8')

    subject = '自动定时发送测试报告'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


