#!//usr/local/bin python
# -*- coding:utf-8 -*-


import requests

import ssl
import json

from requests.auth import HTTPBasicAuth, HTTPDigestAuth

ssl._create_default_https_context = ssl._create_unverified_context

base_url = "http://httpbin.org"

# #发送get类型的请求
# r = requests.get(base_url+'/get')
# print(r.status_code)
#
# #发送post类型的请求
# r = requests.post(base_url+'/post')
# print(r.status_code)
#
# #发送put类型的请求
# r = requests.put(base_url+'/put')
# print(r.status_code)
#
# #发送Delete类型的请求
# r = requests.delete(base_url+'/delete')
# print(r.status_code)

#参数传递
# param_data = {'user':'zxw', 'password':'6666'}
# r = requests.get(base_url+'/get', params=param_data)
# print(r.url)
# print(r.status_code)

#请求体定制
# form_data = {'user':'51zxw', 'password':'9999'}
# r = requests.post(base_url+'/post', data=form_data)
# print(r.text)

#请求头定制(x-www-form-urlencoded)
# form_data = {'user':'51zxw', 'password':'9999'}
# header = {'user-agent':'Mozilla/5.0'}
# r = requests.post(base_url+'/post', data=form_data, headers=header)
# # print(r.text)
# print(r.json())

# post请求体制定（application/json）
# json_data = """{
#             "user'":"51zxw",
#             "password":'"9999"
#             }"""
# header = {'user-agent':'Mozilla/5.0'}
# r = requests.post(base_url+'/post', data=json_data, headers=header)
# # print(r.text)
# print(r.json())

# json.dumps():方法把data转换为合法的JSON字符串格式
# url = "http://httpbin.org/post"
# data = {
#         "name": "hanzhichao",
#         "age": 18
#         }  # 字典格式，方便添加
# headers = {"Content-Type":"application/json"} # 严格来说，我们需要在请求头里声明我们发送的格式
# res = requests.post(url=url, data=json.dumps(data), headers=headers) #  将字典格式的data变量转换为合法的JSON字符串传给post的data参数
# print(res.text)


# header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
# r = requests.get('https://www.zhihu.com/explore', headers=header)
# # print(r.text)
# print(r.headers)

#cookie设置
# cookie = {'user':'51zxw'}
# r = requests.get(base_url+'/cookies', cookies=cookie, timeout=3)
# print(r.text)

# r = requests.get('http://www.baidu.com')
# print(r.cookies)
# print(type(r.cookies))
# for key, value in r.cookies.items():
#     print(key + ':' + value)

#文件上传
# file = {'file': open('picture.png', 'rb')}
# r = requests.post(base_url+'/post', files=file)
# print(r.text)

# r = requests.get(base_url+'/cookies/set/user/51zxw')
# print(r.text)
#
# r = requests.get(base_url+'/cookies')
# print(r.text)

#会话对象
# s = requests.Session()
#
# r = s.get(base_url+'/cookies/set/user/51zxw')
# print(r.text)
#
# r = s.get(base_url+'/cookies')
# print(r.text)

#证书验证
# r = requests.get('https://www.12306.cn', verify=False)
# print(r.text)

#代理设置
# proxies = {'https':'https://118.190.94.224:9001'}
# r = requests.get(base_url+'/get', proxies=proxies)
# print(r.text)

#身份认证
# r = requests.get(base_url+'/basic-auth/51zxw/8888', auth=HTTPBasicAuth('51zxw', '8888'))
# print(r.text)
#
# r = requests.get(base_url+'/digest-auth/auth/zxw/6666', auth=HTTPDigestAuth('zxw', '6666'))
# print(r.text)

#流式请求
r = requests.get(base_url+'/stream/10', stream=True)

if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    data = json.loads(line)
    print(data)
    print(data['id'])

