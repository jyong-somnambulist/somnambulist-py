# -*- coding: UTF-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import io
from pyspark.sql import SparkSession


def get_cfje_qx_rule():
    dict2 = {'index': '欠薪、拖欠社保、损害员工权益',
             'cfyj': ['劳动保障监察条例', '劳动监察行政处罚自由裁量标准'],
             'cfmc': ['恶意欠薪', '拖欠劳动者工资', '拖欠员工工资', '拖欠农民工工资', '未按规定为其办理社会保险登记', '未依法为其参加社会保险', '拖欠社保', '损害员工权益', '欠薪',
                      '拖欠工资'],
             'cfbm': ['人社', '人力资源和社会保障', '劳动和社会保障监察', '人力'],
             'cfje': 100000}
    return dict2


def get_cfje_rules():
    lista = []

    dict1 = {'index': '虚假广告（金额）', 'cfyj': ['反不正当竞争法', '反不正当竞争条例', '广告法'],
             'cfmc': ['欺骗', '误导', '混淆', '虚假', '虚构', '杜撰', '低俗', '性暗示', '赌博', '迷信', '未经审查', '审核', '与客观实际不符', '与其宣传内容不符',
                      '损害国家尊严', '违法广告', '虚假广告'],
             'cfbm': ['市场监督', '市场监管', '市场综合执法', '工商'], 'cfje': 1000000}
    dict2 = {'index': '破坏网络空间传播秩序', 'cfyj': ['网络安全法', '互联网信息服务管理办法'],
             'cfmc': ['严重破坏网络空间传播秩序'],
             'cfbm': ['网信办', '互联网信息办公室'], 'cfje': 100000}
    lista.append(dict1)
    lista.append(dict2)
    return lista


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def readRules(url):
    lists = []
    with io.open(url, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            splits = line.split('\t')
            dict_ele = {'index': splits[0], 'cfyj': splits[1].split('、'), 'cfmc': splits[2].split('、'),
                        'cfbm': splits[3].split('、'), 'cfje': splits[4].split('、'),
                        'cflb': splits[5].split('、')}
            lists.append(dict_ele)
    return lists


def get_maxdt(spark, in_table):
    sql = 'show partitions ' + in_table
    print(sql)
    return spark.sql(sql).rdd.max()['partition'].replace('dt=', '')


def operator_row(rules, row, columns):
    row_dict = {}
    for idx, field in enumerate(columns):
        row_dict[field] = row[idx]

    cf_nr_fk = row['cf_nr_fk']
    money = 0
    if cf_nr_fk is None:
        money = 0
    if is_number(cf_nr_fk):
        money = float(cf_nr_fk) * 10000

    cf_yj = row['cf_yj']
    cf_cfmc = row['cf_cfmc']
    cf_sy = row['cf_sy']
    cf_xzjg = row['cf_xzjg']
    cf_cflb1 = row['cf_cflb1']
    cf_cflb2 = row['cf_cflb2']

    cflb_rule1 = '其他-警告|警告;|警告；|其他-不予行政处罚|其他-不予处罚|其他-免于处罚|警告-其他-其他|警告；其他-其他|警告;其他-其他'.split('|')
    if (('罚款' in cf_cflb1 or '罚款' in cf_cflb2) and money < 1000) or (
            cf_cflb1 in cflb_rule1 or cf_cflb2 in cflb_rule1):
        row_dict['cf_type_jx'] = '简易'
        row_dict['serious_dishonesty_punishment'] = None
        return row_dict

    row_dict['cf_type_jx'] = '非简易'
    cflb_bool = cf_cflb1 in rules['cflb'] or cf_cflb2 in rules['cflb']

    index = []
    for rule in rules:
        cf_yj_bool = cf_yj in rule['cf_yj']
        cf_cfmc_bool = cf_cfmc in rule['cf_cfmc'] or cf_sy in rule['cf_cfmc']
        cf_xzjg_bool = cf_xzjg in rule['cf_xzjg']
        if cflb_bool and (cf_yj_bool or (cf_xzjg_bool and cf_cfmc_bool)):
            index.append(rule['index'])

    if cflb_bool and (cf_cfmc in ['恶意逃废债务', '恶意拖欠货款', '恶意拖欠服务费'] or cf_sy in ['恶意逃废债务', '恶意拖欠货款', '恶意拖欠服务费']):
        index.append('恶意逃废债务、恶意拖欠货款或服务费')

    if cflb_bool and (cf_sy in '非法集资' or cf_cfmc in '非法集资'):
        index.append('非法集资')

    for rule in get_cfje_rules():
        cfje_bool = cf_yj > rule['cfje']
        cf_yj_bool = cf_yj in rule['cf_yj']
        cf_cfmc_bool = cf_cfmc in rule['cf_cfmc'] or cf_sy in rule['cf_cfmc']
        cf_xzjg_bool = cf_xzjg in rule['cf_xzjg']
        if cfje_bool and (cf_yj_bool or (cf_xzjg_bool and cf_cfmc_bool)):
            index.append(rule['index'])

    rule = get_cfje_qx_rule()
    cfje_bool = cf_yj > rule['cfje']
    cf_yj_bool = cf_yj in rule['cf_yj']
    cf_cfmc_bool = cf_cfmc in rule['cf_cfmc'] or cf_sy in rule['cf_cfmc']
    cf_jg_bool = cf_xzjg in rule['cf_xzjg']

    basic_bool = cf_yj_bool or (cf_jg_bool and cf_cfmc_bool)
    if (cflb_bool and basic_bool) or (cfje_bool and basic_bool):
        index.append(rule['index'])

    if len(index) == 0 and cflb_bool:
        index.append('其他')

    if len(index) == 0:
        index.append(None)
    row_dict['serious_dishonesty_punishment'] = ','.join(map(str, index))
    return row_dict


def operator_data(spark, rules):
    in_table = 'tmp_pub_penalty'
    out_table = 'tmp_pub_penalty_tmp'
    max_dt = get_maxdt(spark, in_table)
    select_fields = 'area_code ,bbd_dotime ,bbd_source ,bbd_table ,bbd_type ,bbd_uptime ,bbd_xgxx_id ,bz ,cf_cfjgdm ,' \
                    'cf_cflb1 ,cf_cflb2 ,cf_cfmc ,cf_fr ,cf_fr_zjhm ,cf_fr_zjlx ,cf_gsjzq ,cf_jdrq ,cf_jg ,cf_nr ,' \
                    'cf_nr_fk ,cf_nr_wfff ,cf_nr_zkdx ,cf_qx ,cf_sjlydm ,cf_sy ,cf_wfxw ,cf_wsh ,cf_xdr_gsdj ,' \
                    'cf_xdr_lb ,cf_xdr_sfz ,cf_xdr_shxym ,cf_xdr_shzz ,cf_xdr_swdj ,cf_xdr_sydw ,cf_xdr_zdm ,' \
                    'cf_xdr_zjlx ,cf_xzbm ,cf_xzjg ,cf_yj ,cf_zt ,collecttime ,createtime_dept ,currency_case ,' \
                    'data_type ,entity_name ,finger_print ,id ,lately_modify_time ,money_case ,providetime ,' \
                    'punish_status ,punish_type ,rksj ,sjc ,ctime,bbd_qyxx_id'
    datasets = spark.sql('select ' + select_fields + ' from ' + in_table + ' where dt=' + max_dt)
    broadcast = spark.sparkContext.broadcast(rules)
    columns = datasets.columns
    rows = datasets.rdd.map(lambda row: operator_row(broadcast.value, row, columns))
    spark.createDataFrame(rows).show()
    # spark.sql(
    #     'insert overwrite  table ' + out_table + ' partition(dt=' + max_dt + ')  select * from tmp_penatly')
    spark.stop


if __name__ == '__main__':
    url = sys.argv[0]
    # url = 'D:\\data\\xzcf_rules.txt'
    # /data3/bbdoffline/dp-wangjunyong/py_job/xzcf_rules.txt
    rules = readRules(url)
    spark = SparkSession.builder.master('local').appName('pub_penalty app').enableHiveSupport().getOrCreate()
    operator_data(spark, rules)
