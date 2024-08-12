from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pov_exercise.config.ConfigStore import *
from pov_exercise.functions import *

def batch_lookup_creation(spark: SparkSession, batch: DataFrame):
    keyColumns = ['''insertdate''']
    valueColumns = ['''status''', '''process''', '''batch_status_check''', '''batchid''']
    createLookup("batch_lookup", batch, spark, keyColumns, valueColumns)
