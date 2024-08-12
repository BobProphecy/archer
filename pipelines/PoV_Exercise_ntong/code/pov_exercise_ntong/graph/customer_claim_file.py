from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pov_exercise_ntong.config.ConfigStore import *
from pov_exercise_ntong.functions import *

def customer_claim_file(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("CLAIM_NUMBER", IntegerType(), True), StructField("SOURCE_RECORD_ID", StringType(), True), StructField("INSURANCE_TYPE", StringType(), True), StructField("CLAIMANT_FIRST_NAME", StringType(), True), StructField("CLAIMANT_MI", StringType(), True), StructField("CLAIMANT_LAST_NAME", StringType(), True), StructField("CLAIMANT_NAME", StringType(), True), StructField("CLAIM_DESCRIPTION", StringType(), True), StructField("CLAIMANT_SSN", StringType(), True), StructField("DATE_OF_INJURY", DateType(), True), StructField("DATE_OF_CLAIM", DateType(), True), StructField("CLAIM_STATUS", StringType(), True), StructField("CLAIM_AMOUNT", IntegerType(), True), StructField("CLAIM_TYPE", StringType(), True), StructField("EMPLOYER_NAME", StringType(), True), StructField("EMPLOYER_ADDRESS", StringType(), True), StructField("EMPLOYER_CITY", StringType(), True), StructField("EMPLOYER_STATE", StringType(), True), StructField("EMPLOYER_POSTAL_CODE", IntegerType(), True), StructField("ADJUSTER_NAME", StringType(), True), StructField("ADJUSTER_PHONE", StringType(), True), StructField("ADJUSTER_EMAIL", StringType(), True), StructField("DOCTOR_NAME", StringType(), True), StructField("DOCTOR_PHONE", StringType(), True), StructField("DOCTOR_EMAIL", StringType(), True), StructField("HOSPITAL_NAME", StringType(), True), StructField("HOSPITAL_ADDRESS", StringType(), True), StructField("HOSPITAL_CITY", StringType(), True), StructField("HOSPITAL_STATE", StringType(), True), StructField("HOSPITAL_POSTAL_CODE", StringType(), True), StructField("TREATMENT_DATE", StringType(), True), StructField("TREATMENT_TYPE", StringType(), True), StructField("DISABILITY_TYPE", StringType(), True), StructField("DISABILITY_START", StringType(), True), StructField("DISABILITY_END", StringType(), True), StructField("BENEFIT_AMOUNT", StringType(), True), StructField("CLAIMANT_PHONE", StringType(), True), StructField("CLAIMANT_EMAIL", StringType(), True), StructField("CLAIMANT_ADDRESS", StringType(), True), StructField("CLAIMANT_CITY", StringType(), True), StructField("CLAIMANT_STATE", StringType(), True), StructField("CLAIMANT_POSTAL_CODE", StringType(), True), StructField("BODY_PART", StringType(), True), StructField("NATURE", StringType(), True), StructField("CAUSE", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("inferSchema", True)\
        .option("sep", "|")\
        .csv("/Volumes/archer_pov/staging/raw_customer_claims_files/ARCHER_Customer1SampleClaimFile_20240726120535.txt")
