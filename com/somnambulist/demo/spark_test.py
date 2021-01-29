from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('spark sql app').master('local').getOrCreate()

# list to df
lista = [{'partition': 'dt=20200112'}, {'partition': 'dt=20200111'}, {'partition': 'dt=20200116'}]
df1 = spark.createDataFrame(lista).toDF('a')

df1.show()
