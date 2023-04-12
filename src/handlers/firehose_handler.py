from handlers._handler_base import HandlerBase
from workers.firehose_client import FirehoseDelivery

class FirehoseEvent(HandlerBase):
    events = {"CreateDeliveryStream": FirehoseDelivery}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
