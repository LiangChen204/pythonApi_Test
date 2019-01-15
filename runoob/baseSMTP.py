#!//usr/local/bin python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# sender = 'from@runoob.com'
# receivers = ['shutiao@fanhaoyue.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
# # 使用三个引号来设置邮件信息，标准邮件需要三个头部信息： From, To, 和 Subject ，每个信息直接使用空行分割
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')  # 发送者
# message['To'] = Header("测试", 'utf-8')  # 接收者
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")
from email.utils import formataddr

from pip._vendor.distlib.compat import raw_input

"""本机没有 sendmail 访问，也可以使用其他服务商的 SMTP 访问（QQ、网易、Google等）"""
# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "1561114132@qq.com"  # 用户名
mail_pass = "mtwpiwskwesgfgbh"  # 口令

sender = '1561114132@qq.com'
receivers = ['shutiao@fanhaoyue.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('该内容是邮件正文', 'plain', 'utf-8')
message['From'] = Header("薯条QQ邮箱", 'utf-8')
message['To'] = Header("薯条公司邮箱", 'utf-8')

subject = '该内容是邮件标题'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP(mail_host, 25)
    # smtpObj.set_debuglevel(1)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")

# 自动输入发送邮件
# from email.mime.text import MIMEText
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# # 输入Email地址和口令:
# from_addr = raw_input('From: ')
# password = raw_input('Password: ')
# # 输入SMTP服务器地址:
# smtp_server = raw_input('SMTP server: ')
# # 输入收件人地址:
# to_addr = raw_input('To: ')
#
# import smtplib
# server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()
