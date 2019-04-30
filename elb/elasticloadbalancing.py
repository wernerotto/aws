'''
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client.create_load_balancer

https://docs.aws.amazon.com/cli/latest/reference/elb/create-load-balancer.html
aws> 
elb create-load-balancer  \
    --load-balancer-name my-load-balancer \
    --listeners "Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80" \
    --subnets subnet-15aaab61 \
    --security-groups sg-a61988c3

aws> 
elb create-load-balancer-listener
'''

import boto3

session = boto3.Session(profile_name='wottoamz')

client = boto3.client('elb')

response = client.create_load_balancer(
    LoadBalancerName='string',
    Listeners=[
        {
            'Protocol': 'TCP',
            'LoadBalancerPort': 80,
            'InstanceProtocol': 'TCP',
            'InstancePort': 8080,
            'SSLCertificateId': 'string'
        },
    ],
    AvailabilityZones=[
        'eu-west-1',
    ],
    Subnets=[
        'string',
    ],
    SecurityGroups=[
        'string',
    ],
    Scheme='string',
    Tags=[
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
)