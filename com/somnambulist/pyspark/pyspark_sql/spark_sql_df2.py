from pyspark.sql import SparkSession, Row

spark = SparkSession.builder.appName('spark sql app').master('local').getOrCreate()

# dic to df

dict1 = ['a', 'b', 'c']
df2 = spark.createDataFrame(Row(dict1))


def operate_rows(row):
    disc = {}
    for i in range(3):
        disc[str(i)] = row[i]
    disc['6'] = 'gg'
    disc['7'] = None
    return disc


lista = df2.rdd.map(lambda row: operate_rows(row))
df = spark.createDataFrame(lista)

df.show()
