from helper.aws_helper import ServiceBase
from schemas.tag import TagModel, TagList


class KinesisHelper(ServiceBase):

    def __init__(self):
        super().__init__("kinesis")

    def list_tags(self, resource):
        response = self.client.list_tags_for_stream(StreamName=resource)
        tag_list = response.get("Tags", [])
        tags = [TagModel(key=a["Key"], value=a["Value"]) for a in tag_list]
        return TagList(tags=tags)

    def add_tag(self, resource, tag_key, tag_value):
        self.client.add_tags_to_stream(StreamName=resource,
                                 Tags={tag_key: tag_value})
