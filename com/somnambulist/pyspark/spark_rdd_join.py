from pyspark import SparkContext

sc = SparkContext('local', 'join app')

x = sc.parallelize([('spark', 1), ('hadoop', 4)])
y = sc.parallelize([('spark', 2), ('hadoop', 5)])

joined = x.join(y)
finalRdd = joined.collect()
print(finalRdd)

