from helper.aws_helper import ServiceBase
from schemas.tag import TagModel, TagList


class ParameterHelper(ServiceBase):

    def __init__(self):
        super().__init__("ssm")

    def list_tags(self, resource):
        response = self.client.list_tags_for_resource(
            ResourceType="Parameter",
            ResourceId=resource)
        tag_list = response.get("TagList", [])
        tags = [TagModel(key=a["Key"], value=a["Value"]) for a in tag_list]
        return TagList(tags=tags)

    def add_tag(self, resource, tag_key, tag_value):
        self.client.add_tags_to_resource(ResourceType="Parameter",
                                         ResourceId=resource,
                                            Tags=[{"Key": tag_key,
                                                   "Value": tag_value}])

class MWHelper(ServiceBase):

    def __init__(self):
        super().__init__("ssm")

    def list_tags(self, resource):
        response = self.client.list_tags_for_resource(
            ResourceType="MaintenanceWindow",
            ResourceId=resource)
        tag_list = response.get("TagList", [])
        tags = [TagModel(key=a["Key"], value=a["Value"]) for a in tag_list]
        return TagList(tags=tags)

    def add_tag(self, resource, tag_key, tag_value):
        self.client.add_tags_to_resource(ResourceType="MaintenanceWindow",
                                         ResourceId=resource,
                                            Tags=[{"Key": tag_key,
                                                   "Value": tag_value}])
