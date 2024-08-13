from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pov_exercise.config.ConfigStore import *
from pov_exercise.functions import *

def limit_to_one(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.limit(1)
