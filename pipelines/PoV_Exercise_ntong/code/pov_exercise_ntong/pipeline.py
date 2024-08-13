from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pov_exercise_ntong.config.ConfigStore import *
from pov_exercise_ntong.functions import *
from prophecy.utils import *
from pov_exercise_ntong.graph import *

def pipeline(spark: SparkSession) -> None:
    df_batch = batch(spark)
    df_customer_claim_file = customer_claim_file(spark)
    df_select_claimant_name = select_claimant_name(spark, df_customer_claim_file)
    batch_lookup_creation(spark, df_batch)
    landing_customer1_claim(spark, df_select_claimant_name)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("PoV_Exercise")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/PoV_Exercise_ntong")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/PoV_Exercise_ntong", config = Config)(pipeline)

if __name__ == "__main__":
    main()
