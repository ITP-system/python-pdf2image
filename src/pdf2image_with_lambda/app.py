from pathlib import Path
from pdf2image import convert_from_bytes
import boto3
import os
import io
from botocore.config import Config


def lambda_handler(event, context):

    s3 = boto3.client(
        "s3",
        region_name="ap-northeast-1",
        endpoint_url="http://localstack:4566",
        config=Config(),
    )
    response = s3.get_object(Bucket="bucket", Key="Catalogue.pdf")
    data = response["Body"].read()

    pages = convert_from_bytes(data)

    img_bytes = io.BytesIO()
    pages[0].save(img_bytes, format="JPEG")
    img_bytes = img_bytes.getvalue()

    base = os.path.splitext(os.path.basename("Catalogue.pdf"))[0]
    s3.put_object(Body=img_bytes, Bucket="bucket", Key=base + ".jpg")

    return {"statusCode": 200, "body": "DONE!"}
