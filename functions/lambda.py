'''
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.create_function

https://docs.aws.amazon.com/lambda/latest/dg/with-userapp.html
aws> lambda list-functions
aws> lambda create-function --function-name lambda_function \
    --zip-file fileb:///Users/wernotto/Downloads/sayHello-9bb2f7e1-8686-4b1d-a0d0-5eebfba4a14a.zip \
    --handler lambda_handler \
    --runtime python3.7 \
    --role arn:aws:iam::174318856950:role/service-role/lambdaSayHello

aws> lambda delete-function --function-name lambda_function
aws> lambda create-alias
aws> lambda delete-alias

'''

import boto3

session = boto3.Session(profile_name='wottoamz')

client = boto3.client('lambda')

response = client.create_function(
    FunctionName='lambdaSayHelloFunction',
    Runtime='python3.7',
    Role='lambdaSayHelloRole',
    Handler='lambdaSayHelloHandler',
    Code={
        'ZipFile': b'bytes',
        'S3Bucket': 'string',
        'S3Key': 'string',
        'S3ObjectVersion': 'string'
    },
    Description='string',
    Timeout=123,
    MemorySize=123,
    Publish=True|False,
    VpcConfig={
        'SubnetIds': [
            'string',
        ],
        'SecurityGroupIds': [
            'string',
        ]
    },
    DeadLetterConfig={
        'TargetArn': 'string'
    },
    Environment={
        'Variables': {
            'string': 'string'
        }
    },
    KMSKeyArn='string',
    TracingConfig={
        'Mode': 'Active'|'PassThrough'
    },
    Tags={
        'string': 'string'
    },
    Layers=[
        'string',
    ]
)