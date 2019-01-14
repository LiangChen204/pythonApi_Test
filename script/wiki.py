#!//usr/local/bin python
# -*- coding:utf-8 -*-

# 引入开发包
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 请求URL并把结果用UTF-8编码
resp = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")
# 使用BeautifulSoup去解析
soup = BeautifulSoup(resp, "html.parser")

# 获取两条以/wiki/开头的a标签的href属性
listUrls = soup.findAll("a", href=re.compile("^/wiki/"), limit=2)

# 输出词条对应的名称和url
for url in listUrls:
    # 过滤以.jpg或.JPG结尾的URL
    if not re.search("\.(jpg|JPG)$", url["href"]):
        # 输出URL的文字和对应的链接
        print(url.get_text(), "<------->", "https://en.wikipedia.org/wiki/Main_Page" + url["href"])
        # wikiresp = urlopen(str("https://en.wikipedia.org/wiki/Main_Page" + url["href"])).read().decode("utf-8")
        # wikisoup = BeautifulSoup(wikiresp, "html.parser")
        # print(wikisoup)
        # listHrefs = ("https://en.wikipedia.org/wiki/Main_Page" + url["href"])
# for href in listHrefs:
#     print(href)
#     wikiresp = urlopen(href).read().decode("utf-8")
#     wikisoup = BeautifulSoup(wikiresp, "html.parser")
#     print(wikisoup)