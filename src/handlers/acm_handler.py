from handlers._handler_base import HandlerBase
from workers.acm_client import Certificate


class AcmEvent(HandlerBase):
    events = {"RequestCertificate": Certificate}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
