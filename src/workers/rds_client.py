import os
from helper.rds_helper import RDSHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def RdsInstance(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    dBInstanceArn = event['detail']['responseElements']['dBInstanceArn']
    tagged = RDSHelper().tagging(resource=dBInstanceArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(dBInstanceArn, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(dBInstanceArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def RdsParameterGroup(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    dBParameterGroupArn = event['detail']['responseElements']['dBParameterGroupArn']
    tagged = RDSHelper().tagging(resource=dBParameterGroupArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(dBParameterGroupArn, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(dBParameterGroupArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def RdsDBSnapshot(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    dbSnapshotArn = event['detail']['responseElements']['dbSnapshotArn']
    tagged = RDSHelper().tagging(resource=dbSnapshotArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(dbSnapshotArn, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(dbSnapshotArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")

def RdsDBCLusterSnapshot(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    dBClusterSnapshotArn = event['detail']['responseElements']['dBClusterSnapshotArn']
    tagged = RDSHelper().tagging(resource=dBClusterSnapshotArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(dBClusterSnapshotArn, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(dBClusterSnapshotArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")
            
            
def RdsEventSubscription(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    eventSubscriptionArn = event['detail']['responseElements']['eventSubscriptionArn']
    tagged = RDSHelper().tagging(resource=eventSubscriptionArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(eventSubscriptionArn, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(eventSubscriptionArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")

def RdsOptionGroup(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    optionGroupArn = event['detail']['responseElements']['optionGroupArn']
    tagged = RDSHelper().tagging(resource=optionGroupArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(optionGroupArn, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(optionGroupArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")

def RdsDbSubnetGroup(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    dBSubnetGroupArn = event['detail']['responseElements']['dBSubnetGroupArn']
    tagged = RDSHelper().tagging(resource=dBSubnetGroupArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(dBSubnetGroupArn, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(dBSubnetGroupArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")