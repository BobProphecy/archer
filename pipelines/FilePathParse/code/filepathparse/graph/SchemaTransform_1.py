from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from filepathparse.config.ConfigStore import *
from filepathparse.functions import *

def SchemaTransform_1(spark: SparkSession, customer_claim_file: DataFrame) -> DataFrame:
    return customer_claim_file\
        .withColumn("file_input_path", expr("_metadata.file_path"))\
        .withColumn("file_input_split", split(col("file_input_path"), "/"))
