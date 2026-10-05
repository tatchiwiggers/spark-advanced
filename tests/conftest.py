import pytest
from pyspark.sql import SparkSession

@pytest.fixture(scope="session")
def spark_fixture():
    spark = SparkSession.builder.appName("Testing PySpark Example").getOrCreate()
    yield spark
    spark.stop()
