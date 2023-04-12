import os
from helper.firehose_helper import FirehoseHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def FirehoseDelivery(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    deliveryStreamName = event['detail']['requestParameters']['deliveryStreamName']
    tagged = FirehoseHelper().tagging(resource=deliveryStreamName, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(deliveryStreamName, user, event['account'],
                        event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(deliveryStreamName, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")
