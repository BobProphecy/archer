from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from setup.config.ConfigStore import *
from setup.functions import *

def type_of_claim(spark: SparkSession, raw_type_of_claim: DataFrame):
    raw_type_of_claim.write.format("delta").mode("overwrite").saveAsTable("`archer_pov`.`target`.`type_of_claim`")
