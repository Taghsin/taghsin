import os
from helper.grafana_helper import GrafanaHeper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def Grafana(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    arn = "arn:aws:grafana:" + \
        event['region']+":"+event['account']+":/workspaces/" + \
        event['detail']['responseElements']['workspace']['id']
    tagged = GrafanaHeper().tagging(resource=arn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(arn, user, event['account'],
                        event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(arn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


