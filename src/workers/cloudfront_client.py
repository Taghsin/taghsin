import os
from helper.cloudfront_helper import CloudFrontHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def Cloudfront(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    aRN = event['detail']['responseElements']['distribution']['aRN']
    tagged = CloudFrontHelper().tagging(resource=aRN, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(aRN, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(aRN, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")