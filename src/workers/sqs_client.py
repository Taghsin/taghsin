import os
from helper.sqs_helper import SqsHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def Sqs(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    queueUrl = event['detail']['responseElements']['queueUrl']
    tagged = SqsHelper().tagging(resource=queueUrl, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(queueUrl, user, event['account'],
                        event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(queueUrl, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")