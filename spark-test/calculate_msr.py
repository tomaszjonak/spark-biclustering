from pyspark import SparkContext, SparkConf
import numpy as np

MASTER_IP='192.168.0.14'
MASTER_PORT=7077
APP_NAME='data load test'

DATA_FILE='./GDS1319.npz'

# initialize spark
conf = SparkConf().setAppName(APP_NAME).setMaster('spark://{}:{}'.format(MASTER_IP, MASTER_PORT))
sc = SparkContext(conf=conf)

# load data from disk
zip_desc = np.load(DATA_FILE)
matrix = zip_desc['arr_0']

# load into cluster
matrix_rdd = sc.parallelize(matrix)

# perform operations
column_means = matrix_rdd.reduce(lambda a, b: np.sum([a, b], axis=0))
row_means = matrix_rdd.map(np.sum)
print(column_means)
print(np.array(row_means.collect()))

