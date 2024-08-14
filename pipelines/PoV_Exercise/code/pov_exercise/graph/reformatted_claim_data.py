from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pov_exercise.config.ConfigStore import *
from pov_exercise.functions import *

def reformatted_claim_data(spark: SparkSession, rename_columns: DataFrame) -> DataFrame:
    return rename_columns.select(
        lookup("batch_lookup", lit(19)).getField("batchid").alias("BatchID"), 
        col("ClaimNumber"), 
        col("SourceRecordID"), 
        col("InsuranceType"), 
        col("ClaimantFirstName"), 
        col("ClaimantMI"), 
        col("ClaimantLastName"), 
        col("ClaimantName"), 
        col("ClaimDescription"), 
        col("ClaimantSSN"), 
        col("DateOfInjury"), 
        col("DateOfClaim"), 
        col("ClaimStatus"), 
        col("ClaimAmount"), 
        col("ClaimType"), 
        col("EmployerName"), 
        col("EmployerAddress"), 
        col("EmployerCity"), 
        col("EmployerState"), 
        col("EmployerZip"), 
        col("AdjusterName"), 
        col("AdjusterPhone"), 
        col("AdjusterEmail"), 
        col("DoctorName"), 
        col("DoctorPhone"), 
        col("DoctorEmail"), 
        col("HospitalName"), 
        col("HospitalAddress"), 
        col("HospitalCity"), 
        col("HospitalState"), 
        col("HospitalZip"), 
        col("TreatmentDate"), 
        col("TreatmentType"), 
        col("DisabilityType"), 
        col("DisabilityStart"), 
        col("DisabilityEnd"), 
        col("BenefitAmount"), 
        col("ClaimantPhone"), 
        col("ClaimantEmail"), 
        col("ClaimantAddress"), 
        col("ClaimantCity"), 
        col("ClaimantState"), 
        col("ClaimantZip"), 
        col("BodyPart"), 
        col("Nature"), 
        col("Cause")
    )
