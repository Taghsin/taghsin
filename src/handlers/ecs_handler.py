from handlers._handler_base import HandlerBase
from workers.ecs_client import EcsCluster, EcsTaskDefinition, EcsClusterService

class EcsEvent(HandlerBase):
    events = {"CreateCluster": EcsCluster,
              "RegisterTaskDefinition": EcsTaskDefinition,
              "CreateService": EcsClusterService
            }

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
