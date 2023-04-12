from handlers._handler_base import HandlerBase
from workers.sns_client import SnsTopic


class SnsEvent(HandlerBase):
    events = {"CreateTopic": SnsTopic}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
