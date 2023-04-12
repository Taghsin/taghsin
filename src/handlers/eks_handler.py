from handlers._handler_base import HandlerBase
from workers.eks_client import Eks

class EksEvent(HandlerBase):
    events = {"CreateCluster": Eks}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
