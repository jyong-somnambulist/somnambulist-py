# -*- coding: utf-8 -*-
# python 27

# 实现从ftp上下载文件到本地
from ftplib import FTP


def ftpconnect(host, username, password):
    ftp = FTP()
    timeout = 30
    port = 21
    ftp.connect(host, port, timeout)
    ftp.login(username, password)
    return ftp


def deletefile(ftp, remotepath, localpath):
    ftp.cwd(remotepath)
    list = ftp.nlst()
    for name in list:
        path = remotepath + name
        print path
        ftp.delete(path)
    ftp.set_debuglevel(0)


def downloadfile(ftp, remotepath, localpath):
    ftp.cwd(remotepath)
    list = ftp.nlst()
    for name in list:
        path = localpath + name
        f = open(path, 'wb')
        filename = 'RETR ' + name
        ftp.retrbinary(filename, f.write)
    ftp.set_debuglevel(0)
    f.close()


if __name__ == "__main__":
    ftp_url = '/2021-03-15/'
    file_url = 'D:\\data\\2021-03-15\\'
    ftp = ftpconnect('192.168.6.211', "wangjunyong", '123456')
    downloadfile(ftp, ftp_url, file_url)
    deletefile(ftp, ftp_url, file_url)
    ftp.quit()
