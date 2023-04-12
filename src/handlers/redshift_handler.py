from handlers._handler_base import HandlerBase
from workers.redshift_client import RedshiftCluster


class RedshiftEvent(HandlerBase):
    events = {"CreateCluster": RedshiftCluster}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
