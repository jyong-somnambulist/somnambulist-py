import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import io

from pyspark.sql import SparkSession


def writeToEs(data):
    bbd_qyxx_id = data['bbd_qyxx_id']
    industry = data['industry']
    cqxd_industry = strToArrayStr(industry)

    query = {
        "script": {
            "lang": "painless",
            "inline": "ctx._source.cqxd_industry= params.cqxd_industry",
            "params": {
                "cqxd_industry": cqxd_industry
            }
        }
    }

    url = ''
    requests.post(url, query)


def strToArrayStr(str):
    return str(str.split(','));


if __name__ == '__main__':
    spark = SparkSession.Builder.appName('request_es').getOrCreate()
    data = spark.read.parquet('/user/cqxdcyfzyjy/temp/basic_temp').select('bbd_qyxx_id', 'industry')

    data.foreach(lambda row: writeToEs(row))
