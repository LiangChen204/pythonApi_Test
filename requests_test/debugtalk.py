#!//usr/local/bin python
# -*- coding:utf-8 -*-

# 获取时间戳
import datetime
import time

import pymysql

from requests_test import getSign
import requests

def get_timestamp(i=0,j=0):
    """
    获取时间戳，接受整数参数两个，默认为0，是当天0点时间戳
    :param i，传1为明天0点时间戳，传-1为昨天0点时间戳
    :param j，为距离0点的分钟数,用来获取制定时间点时间戳
    :return: timestamp，时间戳
    """
    try:
        i = int(i)
        j = int(j)
        timestamp = (int(time.mktime(time.strptime(str(datetime.date.today() + datetime.timedelta(days=i)), '%Y-%m-%d'))) + j*60) * 1000
        return str(timestamp)  # mktime(t):它接收struct_time对象作为参数，返回用秒数来表示时间的浮点数.[t -- 结构化的时间或者完整的9位元组元素]
                                #  time.strptime(string[, format]):函数根据指定的格式把一个时间字符串解析为时间元组.[string -- 时间字符串。 format -- 格式化字符串]。
    except:
        return '请传入正确参数(正负整数)'

# 获取xtoken
def get_token(evn, mobile, password):
    """
    获取token
    :param evn: 环境(不同环境配置不一致，根据不同环境截取到.com/presell-api/或端口号)
    :param mobile: 手机号
    :param password: 密文密码(可以抓包获得)
    :return: token
    """
    url = evn + '/member/action/v2/login'
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'version': '1090000',
               'equipmentId': '869072034065382'}
    request = {'appKey': '300001', 'area_code': '+86', 'equipment_id': '869072034065382', 'mobile': str(mobile),
               'password': str(password), 'timestamp': str(get_timestamp()), 'token': '', 'uid': ''}
    request['sign'] = getSign.getSign(request)
    try:
        r = requests.post(url, headers=headers, data=request)
        return r.json()['data']['token']
    except BaseException:
        return 'Invalid parameter, please check!'


def run_sqldaily_presell(sql):
    """
    查询某个具体的值
    :param sql，要执行的sql语句，不要用select *
    :return: data，查询结果
    """
    db = pymysql.connect(host='common101.my.2dfire-daily.com', user='twodfire', passwd='123456', db='presell',
                         port=3306, charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchone()
        return data
    except ZeroDivisionError as e:
        print(e)
        db.rollback()
    cursor.close()
    db.close()