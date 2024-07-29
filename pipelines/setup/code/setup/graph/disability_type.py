from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from setup.config.ConfigStore import *
from setup.functions import *

def disability_type(spark: SparkSession, raw_disability_type: DataFrame):
    raw_disability_type.write.format("delta").mode("overwrite").saveAsTable("`archer_pov`.`target`.`disability_type`")
