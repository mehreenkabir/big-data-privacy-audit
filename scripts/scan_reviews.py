import re
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import ArrayType, StringType

# Isolated PII detection logic for testability
def find_pii(text):
    if not isinstance(text, str):
        return []
    pii_matches = []
    email_pattern = r"[\\w\\.-]+@[\\w\\.-]+"
    ipv4_pattern = r"\\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b"
    pii_matches.extend(re.findall(email_pattern, text))
    pii_matches.extend(re.findall(ipv4_pattern, text))
    return pii_matches

# Register as a Spark UDF
find_pii_udf = udf(find_pii, ArrayType(StringType()))

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("BigDataPrivacyAudit") \
    .config("spark.hadoop.fs.s3a.impl", 
"org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.aws.credentials.provider", 
"com.amazonaws.auth.DefaultAWSCredentialsProviderChain") \
    .getOrCreate()

# Read Parquet data from S3
input_path = 
"s3a://amazon-reviews-pds/parquet/product_category=Digital_Video_Games/"
df = spark.read.parquet(input_path)

# Apply UDF to scan for PII
df = df.withColumn("found_pii", find_pii_udf(df["review_body"]))

# Filter records that contain PII
pii_df = df.filter(df.found_pii.isNotNull() & (df.found_pii != []))

# Display and count
pii_df.show(truncate=False)
print("Total records with PII:", pii_df.count())

spark.stop()

