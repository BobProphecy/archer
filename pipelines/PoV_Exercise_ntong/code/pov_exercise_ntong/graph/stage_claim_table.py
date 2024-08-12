from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pov_exercise_ntong.config.ConfigStore import *
from pov_exercise_ntong.functions import *

def stage_claim_table(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable("`archer_pov`.`staging`.`stage_claim_table`")
