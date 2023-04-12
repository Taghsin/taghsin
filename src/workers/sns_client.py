import os
from helper.sns_helper import SnsHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def SnsTopic(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    topicArn = event['detail']['responseElements']['topicArn']
    tagged = SnsHelper().tagging(resource=topicArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(topicArn, user, event['account'],
                        event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(topicArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")