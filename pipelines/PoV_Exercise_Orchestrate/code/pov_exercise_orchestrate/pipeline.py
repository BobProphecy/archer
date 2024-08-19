from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pov_exercise_orchestrate.config.ConfigStore import *
from pov_exercise_orchestrate.functions import *
from prophecy.utils import *
from pov_exercise_orchestrate.graph import *

def pipeline(spark: SparkSession) -> None:
    df_control_batch = control_batch(spark)
    df_by_batchid_desc = by_batchid_desc(spark, df_control_batch)
    df_limit_to_one = limit_to_one(spark, df_by_batchid_desc)
    df_select_batch_id = select_batch_id(spark, df_limit_to_one)
    df_last_batch_projection = last_batch_projection(spark, df_select_batch_id)
    batch_lookup_creation(spark, df_last_batch_projection)
    df_raw_claims = raw_claims(spark)
    df_customer1_mapping = customer1_mapping(spark)
    df_rename_columns = rename_columns(spark, df_raw_claims, df_customer1_mapping)
    df_reformatted_claim_data = reformatted_claim_data(spark, df_rename_columns)
    landing_customer1_claim(spark, df_reformatted_claim_data)
    update_control_batch(spark, df_select_batch_id)
    clean_up_files(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("PoV_Exercise")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/PoV_Exercise_Orchestrate")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/PoV_Exercise_Orchestrate", config = Config)(pipeline)

if __name__ == "__main__":
    main()
