from handlers._handler_base import HandlerBase
from workers.cw_client import CwAlarm


class CloudwatchEvent(HandlerBase):
    events = {"PutMetricAlarm": CwAlarm}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
