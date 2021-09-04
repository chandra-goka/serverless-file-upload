import json
import boto3
from urllib.parse import unquote_plus
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

s3 = boto3.client('s3')

def handle(event, context):
    __parse_event(event)


def __parse_event(event=None):
    try:
        for record in event['Records']:
            bucket_name = record['s3']['bucket']['name']
            key = unquote_plus(record['s3']['object']['key'])
            json_content = _get_content_from_s3(bucket_name, key)

        words = word_tokenize(json_content)
        stop_words = set(stopwords.words('english'))

        count = len([
            word
            for word in words
            if word not in stop_words
        ])

        return {
            "conjunctions": count
        }

    except Exception as e:
        raise Exception(f"An Exception occurred while parsing the event : {e}")

def _get_content_from_s3(bucket, key):
    try:
        data = s3.get_object(Bucket=bucket, Key=key)
        contents = data['Body'].read().decode('utf-8')
        if contents:
            return contents
        else:
            raise Exception(f"report not found for key {key} in S3")
    except Exception as e:
        print(e)
        raise Exception(f"An Exception occured while fetching the report from S3 for key {key} : {e}")