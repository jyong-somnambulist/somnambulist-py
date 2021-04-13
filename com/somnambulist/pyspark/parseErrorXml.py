#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
document_tree = xml.dom.minidom.parse('D:\\test\\ERR-manage_bidwinning-20201220.XML')
collection = document_tree.documentElement  # 获取所有元素
print(collection.toxml())
