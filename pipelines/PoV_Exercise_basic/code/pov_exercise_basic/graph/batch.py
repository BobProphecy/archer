from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pov_exercise_basic.config.ConfigStore import *
from pov_exercise_basic.functions import *

def batch(spark: SparkSession) -> DataFrame:
    return spark.read.table("`archer_pov`.`control`.`batch`")
