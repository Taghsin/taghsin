from handlers._handler_base import HandlerBase
from workers.s3_client import S3Bucket


class S3Event(HandlerBase):
    events = {"CreateBucket": S3Bucket}

    def __init__(self, event, user):
        super().__init__(event=event, user=user)
