from pyspark import SparkContext

sc = SparkContext('local', 'broadcast app')

lista = ['a','b','c']
broadcast_data = sc.broadcast(lista)
data = broadcast_data.value
print(data)
print(broadcast_data.value[2])
