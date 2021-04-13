# -*- coding: UTF-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import io
import xlrd

data = xlrd.open_workbook('D:\\appinstall\\a.xlsx')

sheet1 = data.sheets()[0]
for i in range(sheet1.nrows):
    for line in sheet1.row_values(i):
        print line,
    print
