#!//usr/local/bin python
# -*- coding:utf-8 -*-

import json
import requests
from urllib import parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


#构造接口测试数据
data = {'xtoken': 'bef3f20a8ab58952017380bb8435169d', 'city_id': '76', 'latitude': '30.34698486328125', 'longitude': '120.00152126736111'}
url = 'https://meal.2dfire.com/mini-program/presell/v1/home_info_reform'

# data = {'city': '杭州'}
# city = parse.urlencode(data).encode('utf-8')
# url = 'https://www.sojson.com/open/api/weather/json.shtml'

#发送请求
r = requests.get(url, params=data)
#print(r.json())

#将返回结果转化为json类型
response_data = r.json()

#分别获取响应信息，状态
print(response_data['code'])
# print(response_data['data'])
# print(response_data['status'])
# print(response_data['city'])
#
# #获取第一家店logo,content,shopName,showType
# print(response_data['data']['barrageMessageTwoVOS'][0]['logo'])
# print(response_data['data']['barrageMessageTwoVOS'][0]['content'])
# print(response_data['data']['barrageMessageTwoVOS'][0]['shopName'])
# print(response_data['data']['barrageMessageTwoVOS'][0]['showType'])
print(response_data['data']['barrageMessageTwoVOS'])
print(type(response_data['data']['barrageMessageTwoVOS']))
shop_list = response_data['data']['barrageMessageTwoVOS']
# print(len(shop_list))

for i in range(len(shop_list)):
    print(shop_list[i]['shopName'])

