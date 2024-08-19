from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pov_exercise_orchestrate.config.ConfigStore import *
from pov_exercise_orchestrate.functions import *

def clean_up_files(spark: SparkSession):
    if not 'SColumnExpression' in locals():
        from pyspark.dbutils import DBUtils
        DBUtils(spark).fs.mv(
            "/Volumes/archer_pov/orchestrate/raw/ARCHER_Customer1SampleClaimFile_*",
            "/Volumes/archer_pov/orchestrate/processed/",
            recurse = False
        )
