#!/usr/bin/python
# -*- coding: UTF-8 -*-
from hdfs.client import Client
import urllib


def downloadErrorFile(wgj_url, output_url):
    try:
        urllib.urlretrieve(wgj_url, output_url)
        return True
    except Exception, e:
        print e.message
        return False


def writeToHdfs(outputfilepath):
    pass


if __name__ == '__main__':
    client = Client("http://dataompro02.test.bbdops.com:50070")
    filepath = "/user/bbdoffline/wangjunyong/gjwgj/20201214"
    outputfilepath = "/user/bbdoffline/wangjunyong/err"
    file_names = []
    for filename in client.list(filepath):
        file_names.append(str(filename).replace('.json', ''))
    # 开始下载Err反馈文件
    for name in file_names:
        print name

    writeToHdfs(outputfilepath)