from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pov_exercise_orchestrate.config.ConfigStore import *
from pov_exercise_orchestrate.functions import *

def select_batch_id(spark: SparkSession, batch: DataFrame) -> DataFrame:
    return batch.select(
        (col("batchid") + lit(1)).alias("batchid"), 
        current_timestamp().alias("insertdate"), 
        col("status"), 
        lit("ProphecyJOB-Sample Claim Ingestion Process").alias("process"), 
        col("batch_status_check")
    )
