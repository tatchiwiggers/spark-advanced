from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def main():
    spark = SparkSession.builder \
        .appName("Simple PySpark Dataproc DataFrame Job") \
        .getOrCreate()
    numbers_df = spark.createDataFrame([(i,) for i in range(1, 11)], ["number"])
    squared_numbers_df = numbers_df.withColumn("squared", col("number") ** 2)
    squared_numbers_df.show()
    filtered_numbers_df = squared_numbers_df.filter(col("squared") > 10)
    count = filtered_numbers_df.count()
    print("Count of squared numbers greater than 10:", count)
    spark.stop()

if __name__ == "__main__":
    main()
