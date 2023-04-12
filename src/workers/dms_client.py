import os
from helper.database_migration_service_helper import DatabaseMigrationServiceHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def EndPoint(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    endpointArn = event['detail']['responseElements']['endpoint']['endpointArn']
    tagged = DatabaseMigrationServiceHelper().tagging(resource=endpointArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(endpointArn, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(endpointArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")

def Certificate(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    certificateArn = event['detail']['responseElements']['certificate']['certificateArn']
    tagged = DatabaseMigrationServiceHelper().tagging(
        resource=certificateArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(certificateArn, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(certificateArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def Subnet(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    SubnetGroupIdentifier = event['detail']['responseElements']['replicationSubnetGroup']['replicationSubnetGroupIdentifier']
    replicationSubnetGroupArn = 'arn:aws:dms:' + event['region'] + ':' + event[
        'account'] + ':subgrp:' + SubnetGroupIdentifier
    tagged = DatabaseMigrationServiceHelper().tagging(
        resource=replicationSubnetGroupArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(replicationSubnetGroupArn, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(replicationSubnetGroupArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")

def EventSubscription(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    custSubscriptionId = event['detail']['responseElements']['eventSubscription']['custSubscriptionId']
    eventSubscriptionArn = 'arn:aws:dms:' + \
        event['region'] + ':' + event['account'] + ':es:' + custSubscriptionId
    tagged = DatabaseMigrationServiceHelper().tagging(
        resource=eventSubscriptionArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(eventSubscriptionArn, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(eventSubscriptionArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def ReplicationInstance(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    replicationInstanceArn = event['detail']['responseElements']['replicationInstance']['replicationInstanceArn']
    tagged = DatabaseMigrationServiceHelper().tagging(
        resource=replicationInstanceArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(replicationInstanceArn, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(replicationInstanceArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")
