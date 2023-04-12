from handlers._handler_base import HandlerBase
from workers.ec2_client import Ami, Instance, Dhcp, EbsVolume, ElasticIp, Eni, RouteTable, NatGateway, SecurityGroup, SubnetGroup,  Vpc, VpcPeeringConnection, InternetGateway, NAcl, Snapshot


class Ec2Event(HandlerBase):
    events = {"CreateVolume": EbsVolume,
              "RunInstances": Instance,
              "CreateSecurityGroup": SecurityGroup,
              "CreateVpc": Vpc,
              "CreateVpcPeeringConnection": VpcPeeringConnection,
              "CreateSubnet": SubnetGroup,
              "CreateRouteTable": RouteTable,
              "CreateInternetGateway": InternetGateway,
              "CreateDhcpOptions": Dhcp,
              "CreateNatGateway": NatGateway,
              "AllocateAddress": ElasticIp,
              "CreateImage": Ami,
              "CreateNetworkAcl": NAcl,
              "CreateSnapshot":Snapshot,
              "CreateNetworkInterface": Eni
            }

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
