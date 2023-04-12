from handlers._handler_base import HandlerBase
from workers.lambda_client import Lambda

class LambdaEvent(HandlerBase):
    events = {"CreateFunction20150331": Lambda}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
