from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pov_exercise.config.ConfigStore import *
from pov_exercise.functions import *

def reformat_order_category(spark: SparkSession, customer_claim_file: DataFrame) -> DataFrame:
    return customer_claim_file.select(
        lookup("batch_lookup", lit("2024-07-01T17:34:22.455Z")).getField("batchid").alias("BatchID"), 
        col("CLAIM_NUMBER"), 
        col("SOURCE_RECORD_ID"), 
        col("INSURANCE_TYPE"), 
        col("CLAIMANT_FIRST_NAME"), 
        col("CLAIMANT_MI"), 
        col("CLAIMANT_LAST_NAME"), 
        col("CLAIMANT_NAME"), 
        col("CLAIM_DESCRIPTION"), 
        col("CLAIMANT_SSN"), 
        col("DATE_OF_INJURY"), 
        col("DATE_OF_CLAIM"), 
        col("CLAIM_STATUS"), 
        col("CLAIM_AMOUNT"), 
        col("CLAIM_TYPE"), 
        col("EMPLOYER_NAME"), 
        col("EMPLOYER_ADDRESS"), 
        col("EMPLOYER_CITY"), 
        col("EMPLOYER_STATE"), 
        col("EMPLOYER_POSTAL_CODE"), 
        col("ADJUSTER_NAME"), 
        col("ADJUSTER_PHONE"), 
        col("ADJUSTER_EMAIL"), 
        col("DOCTOR_NAME"), 
        col("DOCTOR_PHONE"), 
        col("DOCTOR_EMAIL"), 
        col("HOSPITAL_NAME"), 
        col("HOSPITAL_ADDRESS"), 
        col("HOSPITAL_CITY"), 
        col("HOSPITAL_STATE"), 
        col("HOSPITAL_POSTAL_CODE"), 
        col("TREATMENT_DATE"), 
        col("TREATMENT_TYPE"), 
        col("DISABILITY_TYPE"), 
        col("DISABILITY_START"), 
        col("DISABILITY_END"), 
        col("BENEFIT_AMOUNT"), 
        col("CLAIMANT_PHONE"), 
        col("CLAIMANT_EMAIL"), 
        col("CLAIMANT_ADDRESS"), 
        col("CLAIMANT_CITY"), 
        col("CLAIMANT_STATE"), 
        col("CLAIMANT_POSTAL_CODE"), 
        col("BODY_PART"), 
        col("NATURE"), 
        col("CAUSE")
    )
