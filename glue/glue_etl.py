import sys

from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql.functions import col, to_date, year, month
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Full dataset
dataFrame = spark.read.json("s3://612646556016-landing-zone/part-*.json")

# Creating better partition columns
dataFrame = dataFrame.withColumn(
    "review_date",
    to_date(col("review_date"), "d MMMM yyyy")
).withColumn(
    "review_year",
    year(col("review_date"))
).withColumn(
    "review_month",
    month(col("review_date"))
)

dataFrame = dataFrame.filter(col("review_date").isNotNull())

dynamicFrame = DynamicFrame.fromDF(dataFrame, glueContext, "reviews_dynamic_frame")

# Parquet + year and month partition keys
glueContext.write_dynamic_frame.from_options(
    frame=dynamicFrame,
    connection_type="s3",
    connection_options={
        "path": "s3://612646556016-formatted-data/",
        "partitionKeys": ["review_year", "review_month"]
    },
    format="parquet"
)

job.commit()
