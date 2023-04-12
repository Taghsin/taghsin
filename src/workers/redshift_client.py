import os
from helper.redshift_helper import RedshiftHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def RedshiftCluster(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    clusterIdentifier = event['detail']['requestParameters']['clusterIdentifier']
    eventRegion = event['region']
    eventAccount = event['account']
    clusterArn = "arn:aws:redshift:"+eventRegion + \
        ":" + eventAccount+":cluster:"+clusterIdentifier
    tagged = RedshiftHelper().tagging(resource=clusterArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(clusterArn, user, event['account'],
                        event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(clusterArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")
