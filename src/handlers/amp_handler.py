from handlers._handler_base import HandlerBase
from workers.amp_client import Amp


class AmpEvent(HandlerBase):
    events = {"CreateWorkspace": Amp}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
