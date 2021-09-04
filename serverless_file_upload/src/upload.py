import json
import boto3

s3 = boto3.client('s3')

def handle(event, context):
    url = s3_client.generate_presigned_url(
        Params={"Bucket": files, "Key": 'sample.txt'},
        ExpiresIn=900,  # 15 minutes
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"statusCode": 200, "data": url}),
        "isBase64Encoded": False,
    }
