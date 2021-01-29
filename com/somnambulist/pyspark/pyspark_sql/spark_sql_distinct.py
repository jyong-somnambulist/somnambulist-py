from pyspark.sql import SparkSession, Row

spark = SparkSession.builder.appName('hive app').master('local').getOrCreate()

lista = [Row(name='zhangsan', age=5, height=80),
         Row(name='zhangsan', age=5, height=80),
         Row(name='zhangsan', age=10, height=80)]

df = spark.createDataFrame(lista)

df_distinct = df.distinct()

df_distinct.show()
