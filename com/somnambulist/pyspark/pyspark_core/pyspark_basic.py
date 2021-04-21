from pyspark import SparkContext

# 初始化sparkContext
sc = SparkContext("local", 'first app')

lista = ['a', 'b', 'c']
rdd = sc.parallelize(lista)
# foreach
print('-------------------------------------foreach1-------------------------------------')
rdd.foreach()
print('-------------------------------------foreach2-------------------------------------')


def f(x):
    print(x)


rdd.foreach(f)

print('-------------------------------------collect-------------------------------------')
# collect
coll = rdd.collect()
print(coll)
# filter
print('-------------------------------------filter-------------------------------------')
filterRdd = rdd.filter(lambda x: 'a' in x)
print(filterRdd.collect())
# count
print('-------------------------------------count-------------------------------------')
counts = rdd.count()

print('Number of elements in RDD ->', counts)

# reduce
print('-------------------------------------reduce-------------------------------------')
from operator import add

list2 = [1, 2, 3, 4, 5]
rdd2 = sc.parallelize(list2)
adding = rdd2.reduce(add)
print(adding)
