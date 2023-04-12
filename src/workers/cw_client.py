import os
from helper.cloudwatch_helper import CloudWatchHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def CwAlarm(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    alarmArn = "arn:aws:cloudwatch:" + \
        event['region']+":"+event['account']+":alarm:" + \
        event['detail']['requestParameters']['alarmName']
    tagged = CloudWatchHelper().tagging(resource=alarmArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(alarmArn, user, event['account'],
                        event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(alarmArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")