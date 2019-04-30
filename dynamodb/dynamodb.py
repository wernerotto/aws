'''
An example of creating a dynamodb via the console, adding items, changing items
and deleting the table. 

First we perform the excercise via the console, followed by the CLI
and then we automate it using a python script with the boto3 SDK. 

https://run.qwiklabs.com/focuses/271?parent=catalog 

aws dynamodb create-table --table-name Music \
    --attribute-definitions \
    AttributeName=Artist,AttributeType=S \
    AttributeName=SongTitle,AttributeType=S \
    --key-schema \
    AttributeName=Artist,KeyType=HASH \
    AttributeName=SongTitle,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5

aws dynamodb put-item --table-name Music --item file:///Users/wernotto/aws/item.json --return-consumed-capacity TOTAL
aws dynamodb describe-table --table-name Music
aws dynamodb delete-table --table-name Music 
aws dynamodb describe-endpoints # returns the region name and cache period (TTL)
aws dynamodb describe-limits #account and table's read/write limits in units? 
aws dynamodb describe-time-to-live --table-name Music #it looks like we can have tables expire? 

pipenv install boto3
pipenv install -d ipython
pipenv shell
ipython

python dynamodb.py
'''
import boto3

# use the correct Amazon credentials
session = boto3.Session(profile_name='wottoamz') 

# Get the service resource
dynamodb = boto3.resource('dynamodb') 

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='Music',
    KeySchema=[
        {
            'AttributeName': 'Artist',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'SongTitle',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Artist',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'SongTitle',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='Music')

# Print out some data about the table.
print(table.item_count)

print(table.creation_date_time)

table.put_item(
    Item={
        'Artist':'Boo',
        'SongTitle':'Baa'
    }
)

