import os
from helper.lambda_helper import LAMBDAHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def Lambda(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    eventName = event['detail']['requestParameters']['functionName']
    eventRegion = event['region']
    eventAccount = event['account']
    source = event['source']
    lambdaResource = "arn:aws:lambda:"+eventRegion + \
        ":" + eventAccount+":function:"+eventName
    tagged = LAMBDAHelper().tagging(resource=lambdaResource, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(lambdaResource, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(lambdaResource, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")
