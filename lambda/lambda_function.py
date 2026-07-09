import boto3
import json
import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

STREAM_NAME = "reviews"
BUCKET = "612646556016-landing-zone"
KEY = "sample.json"

s3_client = boto3.resource("s3")
kinesis_client = boto3.client("kinesis", region_name="us-east-1")


def lambda_handler(event, context):
    logger.info("Lambda invoked")

    obj = s3_client.Object(BUCKET, KEY)
    data = obj.get()["Body"].read().decode("utf-8")
    json_data = json.loads(data)

    for record in json_data:
        put_to_stream(record)

    logger.info("Lambda finished")


def put_to_stream(record):
    payload = {
        "review_id": record["review_id"],
        "reviewer": record["reviewer"],
        "movie": record["movie"],
        "rating": record["rating"],
        "review_summary": record["review_summary"],
        "review_date": record["review_date"],
        "spoiler_tag": record["spoiler_tag"],
        "review_detail": record["review_detail"],
        "helpful": record["helpful"],
        "event_time": datetime.datetime.now().isoformat()
    }

    logger.info(payload)

    response = kinesis_client.put_record(
        StreamName=STREAM_NAME,
        Data=json.dumps(payload),
        PartitionKey=payload["review_id"]
    )

    logger.info(response)
