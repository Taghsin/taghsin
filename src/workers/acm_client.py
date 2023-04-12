import os
from helper.acm_helper import AcmHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event


def Certificate(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    certificateArn = event['detail']['responseElements']['certificateArn']
    tagged = AcmHelper().tagging(resource=certificateArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(certificateArn, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(certificateArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")