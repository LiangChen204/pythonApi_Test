#!//usr/local/bin python
# -*- coding:utf-8 -*-

from urllib import request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#get请求
req = request.Request("http://www.baidu.com")
req.add_header("User-Agent", "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1")
resp = request.urlopen(req)

print(resp.read().decode("utf-8"))
