from handlers._handler_base import HandlerBase
from workers.kms_client import Kms

class KmsEvent(HandlerBase):
    events = {"CreateKey": Kms }

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
