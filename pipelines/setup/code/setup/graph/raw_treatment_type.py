from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from setup.config.ConfigStore import *
from setup.functions import *

def raw_treatment_type(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(StructType([StructField("code", StringType(), True), StructField("description", StringType(), True)]))\
        .option("header", True)\
        .option("sep", "\t")\
        .csv("dbfs:/FileStore/bobwelshmer/archer/table_stage/treatment_type.csv")
