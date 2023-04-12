from handlers._handler_base import HandlerBase
from workers.ecr_client import Ecr

class EcrEvent(HandlerBase):
    events = {"CreateRepository": Ecr}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
