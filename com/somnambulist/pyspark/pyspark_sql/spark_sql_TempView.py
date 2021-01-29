from pyspark.sql import SparkSession

sparkSession = SparkSession.builder.appName('temp view app').master('local').getOrCreate()

file1 = 'D:\\data\\sourcedata\\20201216\\risk_tax_owed.json'
df_json = sparkSession.read.json(file1)
df_json.createOrReplaceTempView('temp_table')

df = sparkSession.sql('select address,bbd_dotime,bbd_xgxx_id from temp_table ')
print(df.columns)
df.show()
