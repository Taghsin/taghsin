from handlers._handler_base import HandlerBase
from workers.efs_client import Efs

class EfsEvent(HandlerBase):
    events = {"CreateFileSystem": Efs}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
