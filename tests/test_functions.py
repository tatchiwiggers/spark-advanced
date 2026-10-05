from pyspark.testing.utils import assertDataFrameEqual
from spark_lecture.functions import remove_extra_spaces


def test_single_space(spark_fixture):
    spark = spark_fixture
    sample_data = [{"name": "John    D.", "age": 30},
                   {"name": "Alice   G.", "age": 25},
                   {"name": "Bob  T.", "age": 35},
                   {"name": "Eve   A.", "age": 28}]

    original_df = spark.createDataFrame(sample_data)

    transformed_df = remove_extra_spaces(original_df, "name")

    expected_data = [{"name": "John D.", "age": 30},
    {"name": "Alice G.", "age": 25},
    {"name": "Bob T.", "age": 35},
    {"name": "Eve A.", "age": 28}]

    expected_df = spark.createDataFrame(expected_data)

    assertDataFrameEqual(transformed_df, expected_df)
