import os
from helper.secretsmanager_helper import SecretsManagerHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def SecretsManager(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    name = event['detail']['requestParameters']['name']
    tagged = SecretsManagerHelper().tagging(resource=name, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(name, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(name, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")
