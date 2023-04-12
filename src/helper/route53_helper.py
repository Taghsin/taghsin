from helper.aws_helper import ServiceBase
from schemas.tag import TagModel, TagList


class Route53HostZoneHelper(ServiceBase):

    def __init__(self):
        super().__init__("route53")

    def list_tags(self, resource):
        response = self.client.list_tags_for_resource(
            ResourceType='hostedzone', ResourceId=resource)
        tag_list = response.get("Tags", [])
        tags = [TagModel(key=a["Key"], value=a["Value"]) for a in tag_list]
        return TagList(tags=[])

    def add_tag(self, resource, tag_key, tag_value):
        self.client.change_tags_for_resource(ResourceType='hostedzone', ResourceId=resource,
                                             AddTags=[{'Key': tag_key, 'Value': tag_value},])


class Route53HealthCheckHelper(ServiceBase):

    def __init__(self):
        super().__init__("route53")

    def list_tags(self, resource):
        response = self.client.list_tags_for_resource(
            ResourceType='healthcheck', ResourceId=resource)
        tag_list = response.get("Tags", [])
        tags = [TagModel(key=a["Key"], value=a["Value"]) for a in tag_list]
        return TagList(tags=[])

    def add_tag(self, resource, tag_key, tag_value):
        self.client.change_tags_for_resource(ResourceType='healthcheck', ResourceId=resource,
                                             AddTags=[{'Key': tag_key, 'Value': tag_value},])
