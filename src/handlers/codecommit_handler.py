from handlers._handler_base import HandlerBase
from workers.codecommit_client import CodeCommitRepository


class CodecommitEvent(HandlerBase):
    events = {"CreateRepository": CodeCommitRepository}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
