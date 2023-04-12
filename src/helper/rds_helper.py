from helper.aws_helper import ServiceBase
from schemas.tag import TagModel, TagList


class RDSHelper(ServiceBase):

    def __init__(self):
        super().__init__("rds")

    def list_tags(self, resource):
        response = self.client.list_tags_for_resource(ResourceName=resource)
        tag_list = response.get("TagList", [])
        tags = [TagModel(key=a["Key"], value=a["Value"]) for a in tag_list]
        return TagList(tags=tags)

    def add_tag(self, resource, tag_key, tag_value):
        self.client.add_tags_to_resource(ResourceName=resource,
                                         Tags=[{"Key": tag_key,
                                               "Value": tag_value}])
