from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from setup.config.ConfigStore import *
from setup.functions import *

def raw_claim(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("claim_id", IntegerType(), True), StructField("claim_number", StringType(), True), StructField("source_system_record_id", StringType(), True), StructField("line_of_business_cd", StringType(), True), StructField("claimant_first_nm", StringType(), True), StructField("claimant_mi", StringType(), True), StructField("claimant_last_nm", StringType(), True), StructField("claimant_nm", StringType(), True), StructField("claimant_address1", StringType(), True), StructField("claimant_address2", StringType(), True), StructField("claimant_state", StringType(), True), StructField("claimant_postal_code", StringType(), True), StructField("claimant_phone", StringType(), True), StructField("claimant_email", StringType(), True), StructField("body_part_cd", StringType(), True), StructField("nature_of_inj_cd", StringType(), True), StructField("cause_of_inj_cd", StringType(), True), StructField("accident_description", StringType(), True), StructField("tax_id", StringType(), True), StructField("date_of_accident", DateType(), True), StructField("date_claim_recd", DateType(), True), StructField("claim_status_cd", StringType(), True), StructField("claim_amount", DoubleType(), True), StructField("type_of_claim_cd", StringType(), True), StructField("employer_name", StringType(), True), StructField("employer_address1", StringType(), True), StructField("employer_address2", StringType(), True), StructField("employer_state", StringType(), True), StructField("employer_postal_code", StringType(), True), StructField("adjuster_nm", StringType(), True), StructField("adjuster_phone", StringType(), True), StructField("adjuster_email", StringType(), True), StructField("medical_provider_nm", StringType(), True), StructField("medical_provider_phone", StringType(), True), StructField("medical_provider_email", StringType(), True), StructField("medical_facility_nm", StringType(), True), StructField("medical_facility_address1", StringType(), True), StructField("medical_facility_address2", StringType(), True), StructField("medical_facility_state", StringType(), True), StructField("medical_facility_postal_code", StringType(), True), StructField("treatment_dt", DateType(), True), StructField("treatment_type_cd", StringType(), True), StructField("disability_type_cd", StringType(), True), StructField("disability_start_dt", DateType(), True), StructField("disability_end_dt", DateType(), True), StructField("benefit_amt", DoubleType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/FileStore/bobwelshmer/archer/table_stage/claim.csv")
