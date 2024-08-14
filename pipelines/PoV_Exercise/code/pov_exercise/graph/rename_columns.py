from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pov_exercise.config.ConfigStore import *
from pov_exercise.functions import *

def rename_columns(spark: SparkSession, data: DataFrame, rename_col: DataFrame) -> DataFrame:
    # Extract the renaming mappings from rename_col
    rename_mappings = {row['SourceColumn']: row['TargetColumn'] for row in rename_col\
                            .collect(
                          )}
    # Rename columns in out0 based on the mappings
    out0 = data.withColumnsRenamed(rename_mappings)

    return out0
