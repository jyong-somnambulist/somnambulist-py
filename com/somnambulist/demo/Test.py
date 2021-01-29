from pyspark.sql import SparkSession

if __name__ == '__main__':
    dict_a = {'name': 'aa'}
    dict_a['age'] = 22
    dict_a['address'] = None
    print(dict_a)
