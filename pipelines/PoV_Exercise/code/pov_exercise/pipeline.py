from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pov_exercise.config.ConfigStore import *
from pov_exercise.functions import *
from prophecy.utils import *
from pov_exercise.graph import *

def pipeline(spark: SparkSession) -> None:
    df_batch = batch(spark)
    batch_lookup_creation(spark, df_batch)
    df_customer_claim_file = customer_claim_file(spark)
    landing_customer1_claim(spark)
    df_customer1_mapping = customer1_mapping(spark)
    df_rename_columns = rename_columns(spark, df_customer_claim_file, df_customer1_mapping)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("PoV_Exercise")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/PoV_Exercise")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/PoV_Exercise", config = Config)(pipeline)

if __name__ == "__main__":
    main()
