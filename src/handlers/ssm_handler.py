from handlers._handler_base import HandlerBase
from workers.ssm_client import ParameterStore, MaintenanceWindow


class SsmEvent(HandlerBase):
    events = {"PutParameter": ParameterStore,
              "CreateMaintenanceWindow": MaintenanceWindow}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
