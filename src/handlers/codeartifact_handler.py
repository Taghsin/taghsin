from handlers._handler_base import HandlerBase
from workers.codeartifact_client import CodeArtifactRepository, CodeArtifactDomain


class CodeartifactEvent(HandlerBase):
    events = {"CreateRepository": CodeArtifactRepository,
              "CreateDomain": CodeArtifactDomain}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
