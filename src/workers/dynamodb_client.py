import os
from helper.dynamo_helper import DynamoHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def DynamoTable(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    tableArn = event['detail']['responseElements']['tableDescription']['tableArn']
    tagged = DynamoHelper().tagging(resource=tableArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(tableArn, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(tableArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")