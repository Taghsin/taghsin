import os
from helper.ssm_helper import ParameterHelper,  MWHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def ParameterStore(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    name = event['detail']['requestParameters']['name']
    tagged = ParameterHelper().tagging(resource=name, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(name, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(name, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")

def MaintenanceWindow(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    windowId = event['detail']['responseElements']['windowId']
    print(windowId)
    tagged = MWHelper().tagging(resource=windowId, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(windowId, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(windowId, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")
