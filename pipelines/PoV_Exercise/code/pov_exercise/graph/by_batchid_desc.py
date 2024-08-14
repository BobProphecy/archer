from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pov_exercise.config.ConfigStore import *
from pov_exercise.functions import *

def by_batchid_desc(spark: SparkSession, control_batch: DataFrame) -> DataFrame:
    return control_batch.orderBy(col("batchid").desc())
