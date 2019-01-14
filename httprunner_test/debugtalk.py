#!//usr/local/bin python
# -*- coding:utf-8 -*-

import hashlib

def getSign(user, passwd):
    str = user + passwd
    md5 = hashlib.md5()
    md5.update(str.encode(encoding='utf-8'))
    sign = md5.hexdigest()
    return sign

print(getSign('51zxw', '8888'))