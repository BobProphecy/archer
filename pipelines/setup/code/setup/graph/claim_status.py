from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from setup.config.ConfigStore import *
from setup.functions import *

def claim_status(spark: SparkSession, raw_claim_status: DataFrame):
    raw_claim_status.write.format("delta").mode("overwrite").saveAsTable("`archer_pov`.`target`.`claim_status`")
