from handlers._handler_base import HandlerBase
from workers.dms_client import EndPoint, Certificate, Subnet, EventSubscription, ReplicationInstance


class DmsEvent(HandlerBase):
    events = {"CreateEndpoint": EndPoint,
              "ImportCertificate": Certificate,
              "CreateReplicationSubnetGroup": Subnet,
              "CreateEventSubscription": EventSubscription,
              "CreateReplicationInstance": ReplicationInstance}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
