'''
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html

kinesis create-stream --stream-name test-stream --shard-count 1 #this creates a stream with a single shard
kinesis delete-stream --stream-name test-stream #this deletes the stream by name

'''

import boto3

ession = boto3.Session(profile_name='wottoamz')

client = boto3.client('kinesis')

response = client.create_stream(
    StreamName='string',
    ShardCount=123
)
