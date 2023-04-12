import os
from helper.eks_helper import EKSHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def Eks(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    clusterArn = event['detail']['responseElements']['cluster']['arn']
    tagged = EKSHelper().tagging(resource=clusterArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(clusterArn, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(clusterArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")
