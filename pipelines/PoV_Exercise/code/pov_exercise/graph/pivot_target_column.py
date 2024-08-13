from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pov_exercise.config.ConfigStore import *
from pov_exercise.functions import *

def pivot_target_column(spark: SparkSession, customer1_mapping: DataFrame) -> DataFrame:
    df1 = customer1_mapping.groupBy(col("TargetColumn"))
    df2 = df1.pivot("TargetColumn")

    return df2.agg(first(col("TargetColumn")).alias("TargetColumn"))
