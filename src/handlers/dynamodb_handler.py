from handlers._handler_base import HandlerBase
from workers.dynamodb_client import DynamoTable


class DynamodbEvent(HandlerBase):
    events = {"CreateTable": DynamoTable}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
