from helper.aws_helper import ServiceBase
from schemas.tag import TagModel, TagList


class ECRHelper(ServiceBase):

    def __init__(self):
        super().__init__("ecr")

    def list_tags(self, resource):
        response = self.client.list_tags_for_resource(resourceArn=resource)
        tag_list = response.get("tags", [])
        tags = [TagModel(key=a["Key"], value=a["Value"]) for a in tag_list]
        return TagList(tags=tags)

    def add_tag(self, resource, tag_key, tag_value):
        print(resource)
        self.client.tag_resource(resourceArn=resource,
                                 tags=[{"Key": tag_key,
                                       "Value": tag_value}])
