#!//usr/local/bin python
# -*- coding:utf-8 -*-


# 利用图灵聊天接口（GET)
import requests

url = "http://www.tuling123.com/openapi/api"
i = 1
while (i > 0):
    myiput = input()
    params = {"key": "ec961279f453459b9248f0aeb6600bbe", "info": myiput}
    res = requests.get(url=url, params=params)
    print((res.json())['text'])
    i = i-1
print("Game Over!")


# 利用图灵查询接口（POST)
purl = "http://openapi.tuling123.com/openapi/api/v2"
data_post = data = {
    "reqType": 0,
    "perception": {
        "inputText": {
            "text": "附近的美食"
        },
        "inputImage": {
            "url": "imageUrl"
        },
        "selfInfo": {
            "location": {
                "city": "浙江",
                "province": "杭州",
                "street": "莫干山路"
            }
        }
    },
    "userInfo": {
        "apiKey": "ec961279f453459b9248f0aeb6600bbe",
        "userId": "206379"
    }
}
res = requests.post(url=purl, json=data_post) # JSON格式的请求，将数据赋给json参数
print(res.text)