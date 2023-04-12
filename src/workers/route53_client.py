import os
from helper.route53_helper import Route53HealthCheckHelper, Route53HostZoneHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def HostZone(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    hostedZoneId = event['detail']['responseElements']['hostedZone']['id']
    resourceId = hostedZoneId.split("/")[2]
    tagged = Route53HostZoneHelper().tagging(resource=resourceId, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(resourceId, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(resourceId, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def HealthCheck(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    healthCheckId = event['detail']['responseElements']['healthCheck']['id']
    tagged = Route53HealthCheckHelper().tagging(resource=healthCheckId, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(healthCheckId, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(healthCheckId, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")
