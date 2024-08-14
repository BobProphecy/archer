from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pov_exercise.config.ConfigStore import *
from pov_exercise.functions import *

def update_control_batch(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("append").saveAsTable("`archer_pov`.`control`.`batch`")
