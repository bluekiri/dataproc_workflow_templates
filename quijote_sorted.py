import pyspark
sc = pyspark.SparkContext()
rdd = sc.textFile('gs://bk-dataproc-template/quijote.txt')
print(sorted(rdd.collect()))
