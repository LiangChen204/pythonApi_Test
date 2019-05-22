# #!//usr/local/bin python
# # -*- coding:utf-8 -*-
#
# """
# Created on 2019/4/28 10:04
# @author: liangchen
# @File: MailDemo
# """
# import os
# import smtplib
# from email.header import Header
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
#
# def new_file(test_dir):
#     # 列举test_dir目录下的所有文件，结果以列表形式返回
#     lists = os.listdir(test_dir)
#     # print(lists)
#     # 对list元素根据时间进行排序
#     lists.sort(key=lambda fn: os.path.getctime(test_dir + '/' + fn))
#
#     # 获取最新文件的绝对路径
#     file_path = os.path.join(test_dir, lists[-1])
#     print(file_path)
#     return file_path
#
#
# def send_mail(newfile):
#     # 第三方 SMTP 服务
#     mail_host = "smtp.qq.com"  # 设置服务器
#     mail_user = "1561114132@qq.com"  # 用户名
#     mail_pass = "mtwpiwskwesgfgbh"  # 口令
#     sender = '1561114132@qq.com'
#     receivers = ['shutiao@fanhaoyue.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#     # 创建一个实例
#     message = MIMEMultipart()
#     message['From'] = Header("1561114132@qq.com", 'utf-8')
#     message['To'] = Header("shutiao@fanhaoyue.com", 'utf-8')
#     subject = 'Python SMTP 邮件测试'
#     message['Subject'] = Header(subject, 'utf-8')
#
#     # 邮件正文内容
#     message.attach(MIMEText('这是接口日报 邮件发送测试……', 'plain', 'utf-8'))
#
#     # 构造附件
#     att = MIMEText(open(newfile, 'rb').read(), 'base64', 'utf-8')
#     att["Content-Type"] = 'application/octet-stream'
#     # 命名filename
#     att["Content-Disposition"] = 'attachment; filename=newfile.html'
#     message.attach(att)
#
#     try:
#         smtpObj = smtplib.SMTP(mail_host, 25)
#         smtpObj.login(mail_user, mail_pass)
#         smtpObj.sendmail(sender, receivers, message.as_string())
#         smtpObj.quit()
#         print("邮件发送成功")
#     except smtplib.SMTPException:
#         print("Error: 无法发送邮件")
#
#
#
#
# newfile = new_file('../reports')
# send_mail(newfile)
import json
import time

import requests


# def test_d_get_bill():
#     url = "https://meal.2dfire.com/presell/trade/v1/for_here/get_trade_bill"
#     params = {
#         'entity_id': '00026863',
#         'seat_code': 'presell_a4a6b9ad2d834487a6d3f216e33b1532',
#         'xtoken': '73a94fbc4e55e7eea62147a50b90350e',
#         's_eid': '00026863'
#     }
#     data = {
#         "requestFromApp": 1,
#         "cashierBillStatusParam": "null",
#         "orderParam": {
#             "orderId": "",
#             "waitingOrderId": '000268636a23b281016a6893ed517397',
#             "pageFrom": "cart",
#             "cartTime": 1556532686215,
#             "firstLoading": 1,
#             "recomputeFlag": "false"
#         },
#         "tipParam": {
#             "customerSelectType": 0,
#             "customerSelectRate": 0,
#             "tipFee": 0
#         },
#         "payParam": {
#             "giftPaySelected": "true",
#             "cardPaySelected": "true",
#             "cardPays": [],
#             "memberPointsSelected": "false",
#             "redPacketPay": "null",
#             "redPacketPaySelected": "false",
#             "memberPointsPay": {}
#         },
#         "promotionParam": {
#             "singleExchangeSelected": "true",
#             "mcPromotionSelected": "true",
#             "shouldReComputeKouBeiSelected": "true",
#             "kouBeiSelected": "false",
#             "cardId": "",
#             "marketCenterPromotions": []
#         }
#     }
#     header = {'Content-Type': "application/json;charset=UTF-8;"}
#     s = requests.session()
#     r = s.post(url, data=params, json=json.dumps(data), headers=header)
#     result = r.json()
#     print("^^^^^^^^^^^^^第四个接口返回结果：" + str(result))

# test_d_get_bill()
from requests_test import getSign


# def test_get_token():
#     """
#     获取token
#     :param evn: 环境(不同环境配置不一致，根据不同环境截取到.com/presell-api/或端口号)
#     :param mobile: 手机号
#     :param password: 密文密码(可以抓包获得)
#     :return: token
#     """
#
#     xtoken = []
#     # print("开始调用登陆接口>>>>>>>>>>>>")
#     url = "https://presell.fanhaoyue.com" + '/member/action/v2/login'
#     headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'version': '1160000',
#                'equipmentId': '302a0bb155cac42b8eb27a351e1af4aa'}
#     request = {'appKey': '300001', 'area_code': '+86', 'equipment_id': '9F9DEEEE707D4EF3A030062BCF6C0A82',
#                'mobile': '15906624143',
#                'password': '5b0f219ac7928fb89d069482c25c9d6f', 'timestamp': str(round(time.time() * 1000)), 'token': '',
#                'uid': ''}
#     request['sign'] = getSign.getSign(request)
#     r = requests.post(url, headers=headers, data=request)
#     # print("登陆接口登陆完毕<<<<<<<<<<<<<<")
#     print("^^^^^^^^^^^^^^^^^^^^^")
#     print(r.json()['data']['token'])
#     xtoken.append(r.json()['data']['token'])
#     print(xtoken[0])
#     # self.xtoken.append(r.json()['data']['token'])

# import requests
#
# url = "https://meal.2dfire.com/presell/trade/v1/for_here/get_trade_bill"
#
# querystring = {"entity_id": "00026863", "seat_code": "presell_a4a6b9ad2d834487a6d3f216e33b1532", "xtoken":"2825ef690c7e6e732c87f40526f54cd6","s_eid":"00026863"}

# payload = "{\n\t\"requestFromApp\": 1,\n\t\"cashierBillStatusParam\": null,\n\t\"orderParam\": {\n\t\t\"orderId\": \"\",\n\t\t\"waitingOrderId\": \"000268636a23b23a016a6cf171f63616\",\n\t\t\"pageFrom\": \"cart\",\n\t\t\"cartTime\": 1556605923910,\n\t\t\"firstLoading\": 1,\n\t\t\"recomputeFlag\": false\n\t},\n\t\"tipParam\": {\n\t\t\"customerSelectType\": 0,\n\t\t\"customerSelectRate\": 0,\n\t\t\"tipFee\": 0\n\t},\n\t\"payParam\": {\n\t\t\"giftPaySelected\": true,\n\t\t\"cardPaySelected\": true,\n\t\t\"cardPays\": [],\n\t\t\"memberPointsSelected\": false,\n\t\t\"redPacketPay\": null,\n\t\t\"redPacketPaySelected\": false,\n\t\t\"memberPointsPay\": {}\n\t},\n\t\"promotionParam\": {\n\t\t\"singleExchangeSelected\": true,\n\t\t\"mcPromotionSelected\": true,\n\t\t\"shouldReComputeKouBeiSelected\": true,\n\t\t\"kouBeiSelected\": false,\n\t\t\"cardId\": \"\",\n\t\t\"marketCenterPromotions\": []\n\t}\n}"
# payload = {
#                 "requestFromApp": 1,
#                 "cashierBillStatusParam": "null",
#                 "orderParam": {
#                     "orderId": "",
#                     "waitingOrderId": '000268636a23b23a016a6cf171f63616',
#                     "pageFrom": "cart",
#                     "cartTime": 1556605923910,
#                     "firstLoading": 1,
#                     "recomputeFlag": "false"
#                 },
#                 "tipParam": {
#                     "customerSelectType": 0,
#                     "customerSelectRate": 0,
#                     "tipFee": 0
#                 },
#                 "payParam": {
#                     "giftPaySelected": "true",
#                     "cardPaySelected": "true",
#                     "cardPays": [],
#                     "memberPointsSelected": "false",
#                     "redPacketPay": "null",
#                     "redPacketPaySelected": "false",
#                     "memberPointsPay": {}
#                 },
#                 "promotionParam": {
#                     "singleExchangeSelected": "true",
#                     "mcPromotionSelected": "true",
#                     "shouldReComputeKouBeiSelected": "true",
#                     "kouBeiSelected": "false",
#                     "cardId": "",
#                     "marketCenterPromotions": []
#                 }
#         }
# headers = {
#     'Content-Type': "application/json"
#     }
# print(type(json.dumps(payload)))
# response = requests.post(url, json=json.dumps(payload), headers=headers, data=querystring)
#
# print(response.text)

def test_e_get_bill():
    print("%%%%%%%%%%%%%%%%%%%%%%self.cart_list:")
    # print(self.cart_list)
    url = "https://meal.2dfire.com/presell/trade/v1/for_here/get_trade_bill"
    params = {
        "entity_id": "00026863",
        "seat_code": "presell_a4a6b9ad2d834487a6d3f216e33b1532",
        "xtoken": "2825ef690c7e6e732c87f40526f54cd6",
        "s_eid": "00026863"
    }
    # params = {"entity_id": "00026863", "seat_code": "presell_a4a6b9ad2d834487a6d3f216e33b1532",
    #                "xtoken": "2825ef690c7e6e732c87f40526f54cd6", "s_eid": "00026863"}

    data = {
        "requestFromApp": 1,
        "cashierBillStatusParam": None,
        "orderParam": {
            "orderId": "",
            "waitingOrderId": "000268636a23b33a016a6da0e0cd3b83",
            "pageFrom": "cart",
            "cartTime": "1556617421134",
            "firstLoading": 1,
            "recomputeFlag": False
        },
        "tipParam": {
            "customerSelectType": 0,
            "customerSelectRate": 0,
            "tipFee": 0
        },
        "payParam": {
            "giftPaySelected": True,
            "cardPaySelected": True,
            "cardPays": [],
            "memberPointsSelected": False,
            "redPacketPay": None,
            "redPacketPaySelected": False,
            "memberPointsPay": {}
        },
        "promotionParam": {
            "singleExchangeSelected": True,
            "mcPromotionSelected": True,
            "shouldReComputeKouBeiSelected": True,
            "kouBeiSelected": False,
            "cardId": "",
            "marketCenterPromotions": []
        }
    }
    header = "'Content-Type': 'application/json'"
    r = requests.post(url, data=json.dumps(data), headers=header, params=params)
    result = r.json()
    print("^^^^^^^^^^^^^第四个接口返回结果：" + str(result))
    # self.assertEqual(result['code'], 1)

test_e_get_bill()

# test_get_token(),
