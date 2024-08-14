from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pov_exercise_orchestrate.config.ConfigStore import *
from pov_exercise_orchestrate.functions import *

def last_batch_projection(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(lit("last").alias("last_batch"), col("batchid"))
