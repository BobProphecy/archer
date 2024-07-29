from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from setup.config.ConfigStore import *
from setup.functions import *
from prophecy.utils import *
from setup.graph import *

def pipeline(spark: SparkSession) -> None:
    df_raw_nature_of_inj = raw_nature_of_inj(spark)
    nature_of_inj(spark, df_raw_nature_of_inj)
    df_raw_claim_status = raw_claim_status(spark)
    df_raw_disability_type = raw_disability_type(spark)
    disability_type(spark, df_raw_disability_type)
    df_raw_cause_of_inj = raw_cause_of_inj(spark)
    cause_of_inj(spark, df_raw_cause_of_inj)
    df_raw_line_of_business = raw_line_of_business(spark)
    df_raw_treatment_type = raw_treatment_type(spark)
    df_raw_body_part = raw_body_part(spark)
    df_raw_claim = raw_claim(spark)
    claim_status(spark, df_raw_claim_status)
    df_raw_customer1_claim = raw_customer1_claim(spark)
    df_raw_control_batch = raw_control_batch(spark)
    control_batch(spark, df_raw_control_batch)
    body_part(spark, df_raw_body_part)
    treatment_type(spark, df_raw_treatment_type)
    customer1_claim(spark, df_raw_customer1_claim)
    df_raw_type_of_claim = raw_type_of_claim(spark)
    claim(spark, df_raw_claim)
    type_of_claim(spark, df_raw_type_of_claim)
    line_of_business(spark, df_raw_line_of_business)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("setup")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/setup")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/setup", config = Config)(pipeline)

if __name__ == "__main__":
    main()
