import os
from helper.kms_helper import KmsHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def Kms(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    keyId = event['detail']['responseElements']['keyMetadata']['keyId']
    tagged = KmsHelper().tagging(resource=keyId, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(keyId, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(keyId, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")
            