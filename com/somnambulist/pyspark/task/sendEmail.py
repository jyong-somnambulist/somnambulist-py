#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = u"dataplatform@bbdservice.com"
receivers = [u'wangjunyong@bbdservice.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

mail_msg = u"""
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""
message = MIMEText(mail_msg, u'html', u'utf-8')
message[u'From'] = Header(u"菜鸟教程", u'utf-8')
message[u'To'] = Header(u"测试", u'utf-8')

subject = u'Python SMTP 邮件测试'
message[u'Subject'] = Header(subject, u'utf-8')

try:
    smtpObj = smtplib.SMTP(u'smtp.bbdservice.com')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print u"邮件发送成功"
except smtplib.SMTPException:
    print u"Error: 无法发送邮件"
