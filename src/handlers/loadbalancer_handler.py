from handlers._handler_base import HandlerBase
from workers.loadbalancer_client import Loadbalancer


class LoadbalancerEvent(HandlerBase):
    events = {"CreateLoadBalancer": Loadbalancer}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
