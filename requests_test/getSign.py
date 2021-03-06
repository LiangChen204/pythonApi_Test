#!//usr/local/bin python
# -*- coding:utf-8 -*-


import hashlib
import re

UN_PARTICIPATE_PARAMS = []
keySecretMap = {"100010": "06fd3e1fa8a34f94ac68c0062f5ec3e0", "100011": "8a56de338a8049d98ed2007924996c00", "300001": "1dd922f3094cbda19077ab8ed0c26989"}


def parseParams(paramIn):
    paramOut = {}
    for key, value in paramIn.items():
        if value and len(value) > 0:
            paramOut[key] = str(value)
        else:
            paramOut[key] = ""
    return paramOut


def getSign(paramsMap, token=''):
    params = parseParams(paramsMap)
    appKey = params['appKey']

    if appKey in keySecretMap.keys():
        params['secretKey'] = keySecretMap[appKey]

    params['token'] = token

    return generateSign(params)


def encode(origin):
    if origin:
        try:
            md = hashlib.md5()
            md.update(origin.encode(encoding='utf-8'))
            resultString = md.hexdigest()  # hexdigest()返回摘要，作为十六进制数据字符串值
            return resultString
        except ZeroDivisionError as ee2:
            print(ee2)
        return ''

    else:
        return "MULTI_000523"


def generateSign(params):
    keys = sorted(params.keys())
    UN_PARTICIPATE_PARAMS = ["sign"]
    query = ''
    first = True

    for key in keys:
        if key not in UN_PARTICIPATE_PARAMS:
            value = str(params[key])
            if str(key).replace(' ', ''):
                if first:
                    first = False
                else:
                    query += "&"
                query += key + "=" + value

    return encode(query)


def requset2sign(request):
    # type = re.findall(r'json|params|data', str(request.keys()))[0]
    # paramsMap = request[type]
    # print('获取到入参为:\n' + str(request) + '\n开始计算sign')
    if 'token' in request.keys():
        # print('获取到token：\n' + request['token'])
        sign = getSign(request, request['token'])
    else:
        # print('未获取到token')
        sign = getSign(request)
    # print('计算sign值为：\n' + sign)
    return sign


# if __name__ == '__main__':
#     appKey = "300001"
#     uid = "15157481507"
#     equipmentId = "e10001"
#     timestamp = "1446801341607"
#     sign = "7F2EEB98A37C7F8CEF7AD715F6AE8562"
#     paramsMap = {}
#     paramsMap["appKey"] = appKey
#     paramsMap["uid"] = uid
#     paramsMap["equipmentId"] = equipmentId
#     paramsMap["timestamp"] = timestamp
#     paramsMap["sign"] = sign
#     print(paramsMap)
#     print(getSign(paramsMap, "MzdmZTgzOGFhYTI3NWZhNjMyMDQ4MDJlOTI2MWU3YzI="))
#     print(generateSign(paramsMap))
#     print(requset2sign(paramsMap))