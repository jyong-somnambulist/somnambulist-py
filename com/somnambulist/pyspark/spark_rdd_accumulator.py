from pyspark import SparkContext

sc = SparkContext('local', 'accumulator app')

num = sc.accumulator(0)


def f(x):
    global num
    num += x


rdd = sc.parallelize([1, 2, 3, 4, 5])
rdd.foreach(f)

final = num.value

print(final)
