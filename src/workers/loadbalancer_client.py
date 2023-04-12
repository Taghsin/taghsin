import os
from helper.loadbalancer_helper import LoadbalancerHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def Loadbalancer(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    loadbalancer  = event['detail']['requestParameters']['loadBalancerName']
    tagged = LoadbalancerHelper().tagging(resource=loadbalancer, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(loadbalancer, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(loadbalancer, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")
