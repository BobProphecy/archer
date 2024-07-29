from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from setup.config.ConfigStore import *
from setup.functions import *

def control_batch(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable("`archer_pov`.`control`.`batch`")
