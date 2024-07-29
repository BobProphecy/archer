from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from setup.config.ConfigStore import *
from setup.functions import *

def line_of_business(spark: SparkSession, raw_line_of_business: DataFrame):
    raw_line_of_business.write.format("delta").mode("overwrite").saveAsTable("`archer_pov`.`target`.`line_of_business`")
