from helper.aws_helper import ServiceBase
from schemas.tag import TagModel, TagList


class SqsHelper(ServiceBase):

    def __init__(self):
        super().__init__("sqs")

    def list_tags(self, resource):
        response = self.client.list_queue_tags(QueueUrl=resource)
        tag_list = response.get("Tags",[])
        tags = [TagModel(key=a, value=tag_list[a]) for a in tag_list]
        return TagList(tags=tags)

    def add_tag(self, resource, tag_key, tag_value):
        self.client.tag_queue(QueueUrl=resource,
                              Tags={tag_key: tag_value})
