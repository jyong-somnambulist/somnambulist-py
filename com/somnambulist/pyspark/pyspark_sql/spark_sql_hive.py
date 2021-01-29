from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder.appName('hive app').enableHiveSupport().getOrCreate()

    df = spark.sql('select * from test_sort')
    df.show()
