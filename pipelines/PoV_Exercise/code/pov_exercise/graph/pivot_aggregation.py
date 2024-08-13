from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pov_exercise.config.ConfigStore import *
from pov_exercise.functions import *

def pivot_aggregation(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy()
    df2 = df1.pivot("TargetColumn")

    return df2.agg(first(col("TargetColumn")).alias("TargetColumn"))
