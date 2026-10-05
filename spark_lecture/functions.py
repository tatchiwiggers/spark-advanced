from pyspark.sql.functions import col, regexp_replace

def remove_extra_spaces(df, column_name):
    return df.withColumn(column_name, regexp_replace(col(column_name), "\\s+", " "))
