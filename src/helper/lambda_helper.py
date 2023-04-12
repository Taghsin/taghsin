from helper.aws_helper import ServiceBase
from schemas.tag import TagModel, TagList


class LAMBDAHelper(ServiceBase):

    def __init__(self):
        super().__init__("lambda")

    def list_tags(self, resource):
        response = self.client.list_tags(Resource=resource)
        tag_list = response.get("Tags", {})
        tags = [TagModel(key=a, value=tag_list[a]) for a in tag_list.keys()]
        return TagList(tags=tags)

    def add_tag(self, resource, tag_key, tag_value):
        self.client.tag_resource(Resource=resource,
                                 Tags={tag_key: tag_value})
