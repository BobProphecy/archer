from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from filepathparse.config.ConfigStore import *
from filepathparse.functions import *
from prophecy.utils import *
from filepathparse.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customer_claim_file = customer_claim_file(spark)
    df_raw_control_batch = raw_control_batch(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("FilePathParse")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/FilePathParse")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/FilePathParse", config = Config)(pipeline)

if __name__ == "__main__":
    main()
