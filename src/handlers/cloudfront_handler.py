from handlers._handler_base import HandlerBase
from workers.cloudfront_client import Cloudfront


class CloudfrontEvent(HandlerBase):
    events = {"CreateDistribution": Cloudfront}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
