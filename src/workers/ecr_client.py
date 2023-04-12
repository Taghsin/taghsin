import os
from helper.ecr_helper import ECRHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def Ecr(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    repositoryArn = event['detail']['responseElements']['repository']['repositoryArn']
    tagged = ECRHelper().tagging(resource=repositoryArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(repositoryArn, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(repositoryArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")
