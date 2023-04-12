import os
from helper.iam_helper import IamPolicyHelper, IamRoleHelper, IamUserHelper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event



def IamPolicy(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    policyArn = event['detail']['responseElements']["policy"]['arn']
    tagged = IamPolicyHelper().tagging(resource=policyArn, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(policyArn, user, event['account'],
                        event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(policyArn, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def IamRole(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    roleName = event['detail']['requestParameters']['roleName']
    tagged = IamRoleHelper().tagging(resource=roleName, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(roleName, user, event['account'],
                        event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(roleName, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def IamUser(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    userName = event['detail']['responseElements']["user"]['userName']
    tagged = IamUserHelper().tagging(resource=userName, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(userName, user, event['account'],
                        event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(userName, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")
