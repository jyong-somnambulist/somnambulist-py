from pyspark.sql import SparkSession
from pyspark.sql import Row

session = SparkSession.builder.appName('row app ').master('local').getOrCreate()
sc = session.sparkContext

# row to df
lista = [('zhangsan', 12), ('lisi', 33)]

rdd = sc.parallelize(lista)
df1 = session.createDataFrame(rdd, ['name', 'age'])
df1.show()
print '-'*100
# map to df
Person = Row('name', 'age')
p = rdd.map(lambda r: Person(*r))
df2 = session.createDataFrame(p)
df2.show()

# create StructType to df
from pyspark.sql.types import *

schema = StringType(
    [StructField('name', StringType(), True),
     StructField('age', IntegerType(), True)]
)

df3 = session.createDataFrame(rdd, schema)

df3.show()
