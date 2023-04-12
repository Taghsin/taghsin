import os
from helper.amp_helper import AmpHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event


def Amp(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    arn = event['detail']['responseElements']['arn']
    tagged = AmpHelper().tagging(resource=arn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(arn, user, event['account'],
                        event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(arn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")



