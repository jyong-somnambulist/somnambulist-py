from pyspark import SparkContext
import pyspark

sc = SparkContext('local', 'Cache app')
words = sc.parallelize(['a', 'b', 'c'])

# cache 缓存
words.cache()
# MEMORY_AND_DISK
# words.persist(pyspark.storagelevel.MEMORY_AND_DISK)
caching = words.persist().is_cached

print(caching)
