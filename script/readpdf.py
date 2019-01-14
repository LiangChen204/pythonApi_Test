#!//usr/local/bin python
# -*- coding:utf-8 -*-
from urllib.request import urlopen

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfparser import PDFParser, PDFDocument

#获取文档对象
fp = open("jemter.pdf", "rb")
#fp = urlopen("")

#创建一个与文档关联的解释器
parser = PDFParser(fp)

#PDF文档的对象
doc = PDFDocument()

#连接解释器和文档对象
parser.set_document(doc)
doc.set_parser(parser)

#初始化文档
doc.initialize("")

#创建PDF资源管理器
resource = PDFResourceManager()

#参数分享器
laparam = LAParams()

#创建一个聚合器
device = PDFPageAggregator(resource, laparams=laparam)

#创建PDF页面解析器
interpreter = PDFPageInterpreter(resource, device)

#使用文档对象从页面得到内容
for page in doc.get_pages():
    #使用页面解析器来读取
    interpreter.process_page(page)

    #使用聚合器来获得内容
    layout = device.get_result()

    for out in layout:
        if hasattr(out, "get_text"):
            print(out.get_text())
