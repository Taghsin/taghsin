from handlers._handler_base import HandlerBase
from workers.grafana_client import Grafana

class GrafanaEvent(HandlerBase):
    events = {"CreateWorkspace": Grafana}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
