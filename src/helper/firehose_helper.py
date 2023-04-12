from helper.aws_helper import ServiceBase
from schemas.tag import TagModel, TagList


class FirehoseHelper(ServiceBase):

    def __init__(self):
        super().__init__("firehose")

    def list_tags(self, resource):
        response = self.client.list_tags_for_delivery_stream(DeliveryStreamName=resource)
        tag_list = response.get("Tags", [])
        tags = [TagModel(key=a["Key"], value=a["Value"]) for a in tag_list]
        return TagList(tags=tags)

    def add_tag(self, resource, tag_key, tag_value):
        self.client.tag_delivery_stream(DeliveryStreamName=resource,
                                 Tags=[{"Key": tag_key,
                                    "Value": tag_value}])
