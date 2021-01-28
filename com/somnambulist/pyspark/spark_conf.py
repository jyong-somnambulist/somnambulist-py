from pyspark import SparkConf, SparkContext

conf = SparkConf.setAppName('conf app').setMaster('local')
sc = SparkContext(conf)
