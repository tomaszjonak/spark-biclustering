from pyspark import SparkContext, SparkConf

MASTER_IP='192.168.0.14'
MASTER_PORT=7077
APP_NAME='test_spark_runner'

DATA_FILE='./GSE2180_series_matrix.txt.gz'

# initialize spark
conf = SparkConf().setAppName(APP_NAME).setMaster('spark://{}:{}'.format(MASTER_IP, MASTER_PORT))
sc = SparkContext(conf=conf)

with open(DATA_FILE, 'r') as fd:
    file_rdd = sc.parallelize(fd)
line_lengths = file_rdd.map(len)
def loc_sum(a, b):
    return a + b;
total_lengths = line_lengths.reduce(loc_sum)
print(total_lengths)

