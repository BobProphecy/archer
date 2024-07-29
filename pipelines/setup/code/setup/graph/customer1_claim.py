from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from setup.config.ConfigStore import *
from setup.functions import *

def customer1_claim(spark: SparkSession, raw_customer1_claim: DataFrame):
    raw_customer1_claim.write.format("delta").mode("overwrite").saveAsTable("`archer_pov`.`landing`.`customer1_claim`")
