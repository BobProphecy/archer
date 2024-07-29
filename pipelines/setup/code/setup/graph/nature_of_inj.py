from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from setup.config.ConfigStore import *
from setup.functions import *

def nature_of_inj(spark: SparkSession, raw_nature_of_inj: DataFrame):
    raw_nature_of_inj.write.format("delta").mode("overwrite").saveAsTable("`archer_pov`.`target`.`nature_of_inj`")
