# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')





if __name__ == '__main__':
    cflb_rule1 = '其他-警告|警告;|警告；|其他-不予行政处罚|其他-不予处罚|其他-免于处罚|警告-其他-其他|警告；其他-其他|警告;其他-其他'.split('|')
    for rule in cflb_rule1:
        print rule