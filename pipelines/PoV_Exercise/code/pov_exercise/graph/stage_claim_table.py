from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pov_exercise.config.ConfigStore import *
from pov_exercise.functions import *

def stage_claim_table(spark: SparkSession, pivot_aggregation: DataFrame):
    pivot_aggregation.write.format("delta").mode("overwrite").saveAsTable("`archer_pov`.`staging`.`stage_claim_table`")
