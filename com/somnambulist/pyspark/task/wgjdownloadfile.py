#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import os
import sys
import datetime
import urllib
import requests


def downloadErrorFile(wgj_url, output_url):
    try:
        urllib.urlretrieve(wgj_url, output_url)
        return True
    except Exception, e:
        print e.message
        return False


def get_file(geturl, out_path):  ##文件下载函数
    print geturl
    content = requests.get(geturl)
    filew = open(out_path + url.split("/")[-1], 'wb')
    for chunk in content.iter_content(chunk_size=512 * 1024):
        if chunk:  # filter out keep-alive new chunks
            filew.write(chunk)
    filew.close()


if __name__ == '__main__':
    ip_port = sys.argv[1]
    sub = url = sys.argv[2]
    output_url = sys.argv[3]
    dt = datetime.datetime.now().strftime('%Y-%m-%d')
    # output_url = 'D:\\data\\' + dt + '\\'
    if not os.path.exists(output_url):
        os.mkdir(output_url)
    print output_url
    # ip_port = 'http://localhost:8080'
    # url = ip_port + '/test_data'
    url = ip_port + sub
    content = requests.get(url).text
    sub_url = re.findall('href="(.*?)"', content)
    for url in sub_url:
        geturl = ip_port + url
        get_file(geturl, output_url)
