import os
import boto3

ACCESS = os.environ.get('AWS_ACCESS_KEY_ID')
SECRET = os.environ.get('AWS_SECRET_ACCESS_KEY')


def connect():
    s3 = boto3.resource(
        service_name='s3',
        region_name='us-west-1',
        aws_access_key_id=ACCESS,
        aws_secret_access_key=SECRET
    )
    print(ACCESS)
    print(SECRET)
    return s3
