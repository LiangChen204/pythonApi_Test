#!//usr/local/bin python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup as bs
import re

html_doc = """
<html><head><title>The Dormouse's story<a>Hello</a></title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://exampleScom/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = bs(html_doc, "html.parser")

# print(soup.prettify())

# print(soup.title.string)
# print(soup.title.get_text())

# print(soup.a)
#
# print(soup.find(id="link2").get_text())
#
# # print(soup.findAll("a"))
#
# # for link in soup.findAll("a"):
# #     print(link.string)
#
# print(soup.find("p", {"class":"story"}).get_text())

# for tag in soup.find_all(re.compile("^b")):
#     print(tag.name)

data = soup.findAll("a", href=re.compile(r"^http://example\.com/"))
print(data)