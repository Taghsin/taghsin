import os
from helper.efs_helper import EFSHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def Efs(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    fileleSystemId = event['detail']['responseElements']['fileSystemId']
    tagged = EFSHelper().tagging(resource=fileleSystemId, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(fileleSystemId, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(fileleSystemId, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")
