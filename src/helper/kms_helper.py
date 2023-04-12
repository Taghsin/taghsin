from helper.aws_helper import ServiceBase
from schemas.tag import TagModel, TagList


class KmsHelper(ServiceBase):

    def __init__(self):
        super().__init__("kms")

    def list_tags(self, resource):
        response = self.client.list_resource_tags(
            KeyId=resource)
        tag_list =  response.get("Tags", [])
        tags = [TagModel(key=a["Key"], value=a["Value"]) for a in tag_list]
        return TagList(tags=tags)

    def add_tag(self, resource, tag_key, tag_value):
        self.client.tag_resource(KeyId=resource,
                                       Tags=[{"TagKey": tag_key,
                                       "TagValue": tag_value}])
                                       
