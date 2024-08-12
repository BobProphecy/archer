from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pov_exercise_ntong.config.ConfigStore import *
from pov_exercise_ntong.functions import *

def customer1_mapping(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("Target", StringType(), True), StructField("SourceColumn", StringType(), True), StructField("TargetColumn", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("inferSchema", True)\
        .option("sep", "|")\
        .csv("/Volumes/archer_pov/target/customer1_mapping_file/ARCHER_Customer1MappingFile2.txt")
