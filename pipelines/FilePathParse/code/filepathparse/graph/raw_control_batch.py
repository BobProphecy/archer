from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from filepathparse.config.ConfigStore import *
from filepathparse.functions import *

def raw_control_batch(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("batchid", IntegerType(), True), StructField("insertdate", TimestampType(), True), StructField("status", IntegerType(), True), StructField("process", StringType(), True), StructField("batch_status_check", IntegerType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/FileStore/bobwelshmer/archer/table_stage/batch.csv")
