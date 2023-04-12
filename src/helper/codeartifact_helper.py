from helper.aws_helper import ServiceBase
from schemas.tag import TagModel, TagList


class CodeArtifactHelper(ServiceBase):

    def __init__(self):
        super().__init__("codeartifact")

    def list_tags(self, resource):
        response = self.client.list_tags_for_resource(resourceArn=resource)
        tag_list = response.get("tags", [])
        tags = [TagModel(key=a["key"], value=a["value"]) for a in tag_list]
        return TagList(tags=tags)

    def add_tag(self, resource, tag_key, tag_value):
        self.client.tag_resource(resourceArn=resource,
                                 tags=[{"key": tag_key,
                                        "value": tag_value}])
