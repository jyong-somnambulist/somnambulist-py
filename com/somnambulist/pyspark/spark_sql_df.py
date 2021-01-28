from pyspark.sql import SparkSession

session = SparkSession.builder.appName('pyspark').master('local').getOrCreate()
file1 = 'D:\\data\\sourcedata\\20201216\\risk_tax_owed.json'
df = session.read.json(file1)
df.show()
df1 = df.select('announce_version', 'bbd_dotime')
df1.show()

df1.printSchema

df1.select(df1['bbd_dotime']).show()

