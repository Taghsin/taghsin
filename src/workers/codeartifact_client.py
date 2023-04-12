import os
from helper.codeartifact_helper import CodeArtifactHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def CodeArtifactRepository(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    arn = event['detail']['responseElements']['repository']['arn']
    tagged = CodeArtifactHelper().tagging(resource=arn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(arn, user, event['account'],
                        event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(arn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def CodeArtifactDomain(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    arn = event['detail']['responseElements']['domain']['arn']
    tagged = CodeArtifactHelper().tagging(resource=arn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(arn, user, event['account'],
                        event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(arn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")
