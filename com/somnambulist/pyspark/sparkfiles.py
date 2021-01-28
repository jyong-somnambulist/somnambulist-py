from pyspark import SparkContext, SparkFiles

file1 = 'D:\\data\\sourcedata\\20201216\\risk_tax_owed.json'

sc = SparkContext('local', 'sparkfile app')

sc.addFile(file1)

print(SparkFiles.get('risk_tax_owed.json'))