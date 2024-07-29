from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from setup.config.ConfigStore import *
from setup.functions import *

def raw_customer1_claim(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("BatchID", IntegerType(), True), StructField("ClaimNumber", StringType(), True), StructField("SourceRecordID", StringType(), True), StructField("InsuranceType", StringType(), True), StructField("ClaimantFirstName", StringType(), True), StructField("ClaimantMI", StringType(), True), StructField("ClaimantLastName", StringType(), True), StructField("ClaimantName", StringType(), True), StructField("ClaimDescription", StringType(), True), StructField("ClaimantSSN", StringType(), True), StructField("DateOfInjury", StringType(), True), StructField("DateOfClaim", StringType(), True), StructField("ClaimStatus", StringType(), True), StructField("ClaimAmount", StringType(), True), StructField("ClaimType", StringType(), True), StructField("EmployerName", StringType(), True), StructField("EmployerAddress", StringType(), True), StructField("EmployerCity", StringType(), True), StructField("EmployerState", StringType(), True), StructField("EmployerZip", StringType(), True), StructField("AdjusterName", StringType(), True), StructField("AdjusterPhone", StringType(), True), StructField("AdjusterEmail", StringType(), True), StructField("DoctorName", StringType(), True), StructField("DoctorPhone", StringType(), True), StructField("DoctorEmail", StringType(), True), StructField("HospitalName", StringType(), True), StructField("HospitalAddress", StringType(), True), StructField("HospitalCity", StringType(), True), StructField("HospitalState", StringType(), True), StructField("HospitalZip", StringType(), True), StructField("TreatmentDate", StringType(), True), StructField("TreatmentType", StringType(), True), StructField("DisabilityType", StringType(), True), StructField("DisabilityStart", StringType(), True), StructField("DisabilityEnd", StringType(), True), StructField("BenefitAmount", StringType(), True), StructField("ClaimantPhone", StringType(), True), StructField("ClaimantEmail", StringType(), True), StructField("ClaimantAddress", StringType(), True), StructField("ClaimantCity", StringType(), True), StructField("ClaimantState", StringType(), True), StructField("ClaimantZip", StringType(), True), StructField("BodyPart", StringType(), True), StructField("Nature", StringType(), True), StructField("Cause", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", "\t")\
        .csv("dbfs:/FileStore/bobwelshmer/archer/table_stage/customer1_claim.csv")
