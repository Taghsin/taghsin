from handlers._handler_base import HandlerBase
from workers.iam_client import IamPolicy, IamRole, IamUser

class IamEvent(HandlerBase):
    events = {"CreatePolicy": IamPolicy,
              "CreateRole": IamRole,
              "CreateUser": IamUser 
             }

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
