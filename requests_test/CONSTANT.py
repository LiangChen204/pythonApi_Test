#!//usr/local/bin python
# -*- coding:utf-8 -*-

import const
from requests_test.debugtalk import get_token

# 定义xtoken
const.DAILY_XTOKEN = get_token('http://consumer-api.2dfire-daily.com', '15906624143',
                               'ccd9d460f0b4713f78ef3cc9fb87ca26')
# 小程序内网环境
const.DAILY_WEB_URL = 'https://api.l.whereask.com/purchase_server/mini-program/presell'

