from handlers._handler_base import HandlerBase
from workers.secretsmanager_client import SecretsManager


class SecretsmanagerEvent(HandlerBase):
    events = {"CreateSecret": SecretsManager}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
