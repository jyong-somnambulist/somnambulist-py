from pyspark.sql import SparkSession

session = SparkSession.builder.appName('row app ').master('local').getOrCreate()
sc = session.sparkContext

# row to df
lista = [('zhangsan', 12), ('lisi', 33)]
rdd = sc.parallelize(lista)
df1 = session.createDataFrame(rdd, ['name', 'age'])
df1.show()
