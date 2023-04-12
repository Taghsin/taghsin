import os
from helper.eventbridge_helper import EventBridgeHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def EventBridgeRule(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    ruleArn = event['detail']['responseElements']['ruleArn']
    tagged = EventBridgeHelper().tagging(resource=ruleArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(ruleArn, user, event['account'],
                        event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(ruleArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


