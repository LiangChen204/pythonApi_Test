#!//usr/local/bin python
# -*- coding:utf-8 -*-
from urllib import parse
from urllib.request import Request, urlopen

req = Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")

postData = parse.urlencode([
    ("StartStation", "977abb69-413a-4ccf-a109-0272c24fd490"),
    ("EndStation", "3301e395-46b8-47aa-aa37-139e15708779"),
    ("DepartueSearchDate", "2018/11/22"),
    ("DepartueSearchTime", "22:30"),
    ("SearchType", "S")
])

req.add_header("Origin", "http://www.thsrc.com.tw")
req.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36")
resp = urlopen(req, data=postData.encode("utf-8"))

print(resp.read().decode("utf-8"))