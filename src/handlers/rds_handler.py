from handlers._handler_base import HandlerBase
from workers.rds_client import RdsInstance, RdsParameterGroup, RdsDBSnapshot, RdsDBCLusterSnapshot,  RdsEventSubscription, RdsOptionGroup, RdsDbSubnetGroup


class RdsEvent(HandlerBase):
    events = {"CreateDBInstance": RdsInstance,
              "CreateDBParameterGroup": RdsParameterGroup,
              "CreateDBSnapshot": RdsDBSnapshot,
              "CreateDBClusterSnapshot":RdsDBCLusterSnapshot,
              "CreateEventSubscription": RdsEventSubscription,
              "CreateOptionGroup": RdsOptionGroup,
              "CreateDBSubnetGroup": RdsDbSubnetGroup}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
