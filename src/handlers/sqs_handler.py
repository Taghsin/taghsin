from handlers._handler_base import HandlerBase
from workers.sqs_client import Sqs


class SqsEvent(HandlerBase):
    events = {"CreateQueue": Sqs}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
