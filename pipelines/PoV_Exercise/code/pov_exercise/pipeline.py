from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pov_exercise.config.ConfigStore import *
from pov_exercise.functions import *
from prophecy.utils import *
from pov_exercise.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customer1_mapping = customer1_mapping(spark)
    df_pivot_target_column = pivot_target_column(spark, df_customer1_mapping)
    df_limit_to_one = limit_to_one(spark, df_pivot_target_column)
    df_Reformat_2 = Reformat_2(spark, df_limit_to_one)
    stage_claim_table(spark, df_Reformat_2)
    df_batch = batch(spark)
    batch_lookup_creation(spark, df_batch)
    df_customer_claim_file = customer_claim_file(spark)
    df_reformat_order_category = reformat_order_category(spark, df_customer_claim_file)
    df_pivot_aggregation = pivot_aggregation(spark, df_customer1_mapping)
    landing_customer1_claim(spark)
    df_Reformat_1 = Reformat_1(spark, df_pivot_aggregation)

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
