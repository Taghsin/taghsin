import os
from helper.ecs_helper import ECSHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def EcsCluster(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    clusterArn = event['detail']['responseElements']['cluster']['clusterArn']
    tagged = ECSHelper().tagging(resource=clusterArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(clusterArn, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(clusterArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def EcsTaskDefinition(event, user): 
    tag = TagModel(key="CreatedBy", value=user)
    taskDefinitionArn = event['detail']['responseElements']['taskDefinition']['taskDefinitionArn']
    tagged = ECSHelper().tagging(resource=taskDefinitionArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(taskDefinitionArn, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(taskDefinitionArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")

def EcsClusterService(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    serviceArn = event['detail']['responseElements']['service']['serviceArn']
    tagged = ECSHelper().tagging(resource=serviceArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(serviceArn, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(serviceArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")