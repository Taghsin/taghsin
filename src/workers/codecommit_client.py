import os
from helper.codecommit_helper import CodeCommitHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def CodeCommitRepository(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    arn = event['detail']['resources'][0]['ARN']
    tagged = CodeCommitHelper().tagging(resource=arn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(arn, user, event['account'],
                        event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(arn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


