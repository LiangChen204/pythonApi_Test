#!//usr/local/bin python
# -*- coding:utf-8 -*-

import const
from requests_test.debugtalk import get_token

# 定义xtoken
const.DAILY_XTOKEN = get_token('http://consumer-api.2dfire-daily.com', '15906624143',
                               'ccd9d460f0b4713f78ef3cc9fb87ca26')

const.PRE_XTOKEN = get_token('https://presell-pre.fanhaoyue.com', '15906624143',
                               '5b0f219ac7928fb89d069482c25c9d6f')

const.PUBLIC_XTOKEN = get_token('https://presell.fanhaoyue.com', '15906624143',
                               '5b0f219ac7928fb89d069482c25c9d6f')

# 小程序内网环境
const.DAILY_WEB_URL = 'https://api.l.whereask.com/purchase_server/mini-program/presell'

# 小程序预发环境
# const.PRE_WEB_URL = 'https://meal.2dfire-pre.com/mini-program/presell'
const.PRE_WEB_URL = 'https://meal.2dfire-pre.com'


# 小程序外网环境
const.PUBLIC_WEB_URL = 'https://meal.2dfire.com/mini-program/presell'

# app线上环境
const.PUBLIC_APP_URL = 'https://presell.fanhaoyue.com'

# 获取sign值
# 线上环境




