import os
from helper.kinesis_helper import KinesisHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event


def KinesisStream(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    streamName = event['detail']['requestParameters']['streamName']
    tagged = KinesisHelper().tagging(resource=streamName, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(streamName, user, event['account'],
                        event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(streamName, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")