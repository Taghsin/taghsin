from handlers._handler_base import HandlerBase
from workers.eventbridge_client import EventBridgeRule

class EventBridgeEvent(HandlerBase):
    events = {"PutRule": EventBridgeRule}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
