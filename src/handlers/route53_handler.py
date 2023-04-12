from handlers._handler_base import HandlerBase
from workers.route53_client import HostZone, HealthCheck


class Route53Event(HandlerBase):
    events = {"CreateHostedZone": HostZone,
              "CreateHealthCheck": HealthCheck}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
