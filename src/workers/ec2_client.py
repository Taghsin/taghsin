import os
from helper.ec2_helper import EC2Helper
from schemas.tag import TagModel
from notification.slack import slack_event
from notification.teams import teams_event

def Ami(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    imageId = event['detail']['responseElements']['imageId']
    tagged = EC2Helper().tagging(resource=imageId, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(imageId, user, event['account'],
                        event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(imageId, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def Instance(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    instances = event['detail']['responseElements']['instancesSet']['items']
    for instance in instances:
        tagged = EC2Helper().tagging(resource=instance["instanceId"], tag=tag)
        if tagged:
            if os.getenv("ENABLE_SLACK"):
                slack_event(instance["instanceId"], user,
                            event['account'], event['region'], event['source'])
            elif os.getenv("ENABLE_TEAMS"):
                teams_event(instance["instanceId"], user, event['account'],
                            event['region'], event['source'])
            else:
                print("We will improve with other versions")

def Dhcp(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    dhcpOptionsId = event['detail']['responseElements']['dhcpOptions']['dhcpOptionsId']
    tagged = EC2Helper().tagging(resource=dhcpOptionsId, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(dhcpOptionsId, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(dhcpOptionsId, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def EbsVolume(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    volume = event['detail']['responseElements']['volumeId']
    tagged = EC2Helper().tagging(resource=volume, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(volume, user, event['account'],
                        event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(volume, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def ElasticIp(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    allocationId = event['detail']['responseElements']['allocationId']
    tagged = EC2Helper().tagging(resource=allocationId, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(allocationId, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(allocationId, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def Eni(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    networkInterfaceId = event['detail']['responseElements']['networkInterface']['networkInterfaceId']
    tagged = EC2Helper().tagging(resource=networkInterfaceId, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(networkInterfaceId, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(networkInterfaceId, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def LodBalancer(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    loadbalancer = event['detail']['requestParameters']['loadBalancerName']
    tagged = EC2Helper().tagging(resource=loadbalancer, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(loadbalancer, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(loadbalancer, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def RouteTable(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    routeTableId = routeTableId = event['detail']['responseElements']['routeTable']['routeTableId']
    tagged = EC2Helper().tagging(resource=routeTableId, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(routeTableId, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(routeTableId, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def NatGateway(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    natGatewayId = event['detail']['responseElements']['CreateNatGatewayResponse']['natGateway']['natGatewayId']
    tagged = EC2Helper().tagging(resource=natGatewayId, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(natGatewayId, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(natGatewayId, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def NAcl(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    networkAclId = event['detail']['responseElements']['networkAcl']['networkAclId']
    tagged = EC2Helper().tagging(resource=networkAclId, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(networkAclId, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(networkAclId, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def SecurityGroup(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    groupId = event['detail']['responseElements']['groupId']
    tagged = EC2Helper().tagging(resource=groupId, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(groupId, user, event['account'],
                        event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(groupId, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def Snapshot(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    snapshotId = event['detail']['responseElements']['snapshotId']
    tagged = EC2Helper().tagging(resource=snapshotId, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(snapshotId, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(snapshotId, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def SubnetGroup(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    subnetId = event['detail']['responseElements']['subnet']['subnetId']
    tagged = EC2Helper().tagging(resource=subnetId, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(subnetId, user, event['account'],
                        event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(subnetId, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def VpcPeeringConnection(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    vpcPeeringConnectionId = event['detail']['responseElements']['vpcPeeringConnection']['vpcPeeringConnectionId']
    tagged = EC2Helper().tagging(resource=vpcPeeringConnectionId, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(vpcPeeringConnectionId, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(vpcPeeringConnectionId, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def Vpc(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    vpcId = event['detail']['responseElements']['vpc']['vpcId']
    tagged = EC2Helper().tagging(resource=vpcId, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(vpcId, user, event['account'],
                        event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(vpcId, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")


def InternetGateway(event, user):
    tag = TagModel(key="CreatedBy", value=user)
    internetGatewayId = event['detail']['responseElements']['internetGateway']['internetGatewayId']
    tagged = EC2Helper().tagging(resource=internetGatewayId, tag=tag)
    if tagged:
        if os.getenv("ENABLE_SLACK"):
            slack_event(internetGatewayId, user,
                        event['account'], event['region'], event['source'])
        elif os.getenv("ENABLE_TEAMS"):
            teams_event(internetGatewayId, user, event['account'],
                        event['region'], event['source'])
        else:
            print("We will improve with other versions")
            
