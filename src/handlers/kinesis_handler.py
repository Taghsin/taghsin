from handlers._handler_base import HandlerBase
from workers.kinesis_client import KinesisStream

class KinesisEvent(HandlerBase):
    events = {"CreateStream": KinesisStream }

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
