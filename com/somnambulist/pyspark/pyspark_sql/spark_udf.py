from pyspark.sql import SparkSession

sparkSession = SparkSession.builder.appName('udf app').master('local').getOrCreate()


# udf
def strLen(x):
    if x is None:
        return 0
    return len(x)


sparkSession.udf.register('strLen', lambda x: strLen(x))

file1 = 'D:\\data\\sourcedata\\20201216\\risk_tax_owed.json'

df_json = sparkSession.read.json(file1)

df_json.createOrReplaceTempView('tmp_json')

df = sparkSession.sql('select strLen(address) from tmp_json')
df.show()
