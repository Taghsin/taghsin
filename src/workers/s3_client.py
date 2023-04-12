import os
from helper.s3_helper import S3Helper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def S3Bucket(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    bucketName = event['detail']['requestParameters']['bucketName']
    tagged = S3Helper().tagging(resource=bucketName, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(bucketName, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(bucketName, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")