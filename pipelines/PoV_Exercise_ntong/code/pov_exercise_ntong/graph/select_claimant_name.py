from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pov_exercise_ntong.config.ConfigStore import *
from pov_exercise_ntong.functions import *

def select_claimant_name(spark: SparkSession, customer_claim_file: DataFrame) -> DataFrame:
    return customer_claim_file.select(
        lookup("batch_lookup", lit(19)).getField("batchid").alias("BatchId"), 
        col("CLAIM_NUMBER").alias("ClaimNumber"), 
        col("SOURCE_RECORD_ID").alias("SourceRecordID"), 
        col("INSURANCE_TYPE").alias("InsuranceType"), 
        col("CLAIMANT_FIRST_NAME").alias("ClaimantFirstName"), 
        col("CLAIMANT_MI").alias("ClaimantMI"), 
        col("CLAIMANT_LAST_NAME").alias("ClaimantLastName"), 
        col("CLAIMANT_NAME").alias("ClaimantName"), 
        col("CLAIM_DESCRIPTION").alias("ClaimDescription"), 
        col("CLAIMANT_SSN").alias("ClaimantSSN"), 
        col("DATE_OF_INJURY").alias("DateOfInjury"), 
        col("DATE_OF_CLAIM").alias("DateOfClaim"), 
        col("CLAIM_STATUS").alias("ClaimStatus"), 
        col("CLAIM_AMOUNT").alias("ClaimAmount"), 
        col("CLAIM_TYPE").alias("ClaimType"), 
        col("EMPLOYER_NAME").alias("EmployerName"), 
        col("EMPLOYER_ADDRESS").alias("EmployerAddress"), 
        col("EMPLOYER_CITY").alias("EmployerCity"), 
        col("EMPLOYER_STATE").alias("EmployerState"), 
        col("EMPLOYER_POSTAL_CODE").alias("EmployerZip"), 
        col("ADJUSTER_NAME").alias("AdjusterName"), 
        col("ADJUSTER_PHONE").alias("AdjusterPhone"), 
        col("ADJUSTER_EMAIL").alias("AdjusterEmail"), 
        col("DOCTOR_NAME").alias("DoctorName"), 
        col("DOCTOR_PHONE").alias("DoctorPhone"), 
        col("DOCTOR_EMAIL").alias("DoctorEmail"), 
        col("HOSPITAL_NAME").alias("HospitalName"), 
        col("HOSPITAL_ADDRESS").alias("HospitalAddress"), 
        col("HOSPITAL_CITY").alias("HospitalCity"), 
        col("HOSPITAL_STATE").alias("HospitalState"), 
        col("HOSPITAL_POSTAL_CODE").alias("HospitalZip"), 
        col("TREATMENT_DATE").alias("TreatmentDate"), 
        col("TREATMENT_TYPE").alias("TreatmentType"), 
        col("DISABILITY_TYPE").alias("DisabilityType"), 
        col("DISABILITY_START").alias("DisabilityStart"), 
        col("DISABILITY_END").alias("DisabilityEnd"), 
        col("BENEFIT_AMOUNT").alias("BenefitAmount"), 
        col("CLAIMANT_PHONE").alias("ClaimantPhone"), 
        col("CLAIMANT_EMAIL").alias("ClaimantEmail"), 
        col("CLAIMANT_ADDRESS").alias("ClaimantAddress"), 
        col("CLAIMANT_CITY").alias("ClaimantCity"), 
        col("CLAIMANT_STATE").alias("ClaimantState"), 
        col("CLAIMANT_POSTAL_CODE").alias("ClaimantZip"), 
        col("BODY_PART").alias("BodyPart"), 
        col("NATURE").alias("Nature"), 
        col("CAUSE").alias("Cause")
    )
