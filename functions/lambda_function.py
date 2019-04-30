'''
This file is compressed into a zip archive for the command-line
interface to work for "sayHello-9bb2f7e1-8686-4b1d-a0d0-5eebfba4a14a.zip"
'''

import json

print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['key1'])
    print("value2 = " + event['key2'])
    print("value3 = " + event['key3'])
    return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')
