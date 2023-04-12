import json

from config import configuration
from handlers import *


def lambda_handler(event, context):
    print(json.dumps(event))
    user = get_user(event)

    if user not in configuration.IGNORED_USERS:
        process_resources(event, user)

    return


def get_user(event):
    try:
        user = event['detail']['userIdentity']['userName']
    except:
        user = event['detail']['userIdentity']['arn'].rsplit('/', 1)[-1]

    return user


def process_resources(event, user):
    source = event['source']

    event_sources = {
        "aws.acm": AcmEvent,
        "aws.aps": AmpEvent,
        "aws.cloudfront": CloudfrontEvent,
        "aws.monitoring": CloudwatchEvent,
        "aws.codeartifact": CodeartifactEvent,
        "aws.codecommit": CodecommitEvent,
        "aws.dms": DmsEvent,
        "aws.dynamodb": DynamodbEvent,
        "aws.ec2": Ec2Event,
        "aws.ecr": EcrEvent,
        "aws.ecs": EcsEvent,
        "aws.elasticloadbalancing" : LoadbalancerEvent,
        "aws.elasticfilesystem": EfsEvent,
        "aws.eks": EksEvent,
        "aws.events" : EventBridgeEvent,
        "aws.firehose": FirehoseEvent,
        "aws.grafana": GrafanaEvent,
        "aws.iam": IamEvent,
        "aws.kinesis": KinesisEvent,
        "aws.kms": KmsEvent,
        "aws.lambda": LambdaEvent,
        "aws.rds": RdsEvent,
        "aws.redshift": RedshiftEvent,
        "aws.route53": Route53Event,
        "aws.s3": S3Event,
        "aws.secretsmanager": SecretsmanagerEvent,
        "aws.sns": SnsEvent,
        "aws.sqs": SqsEvent,
        "aws.ssm": SsmEvent
    }

    source_event = event_sources.get(source, None)
    if source_event:
        source_event(event, user).handler()
    else:
        print("We will improve with other versions")
