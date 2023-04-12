from helper.aws_helper import ServiceBase
from schemas.tag import TagModel, TagList


class SecretsManagerHelper(ServiceBase):

    def __init__(self):
        super().__init__("secretsmanager")

    def list_tags(self, resource):
        response = self.client.describe_secret(SecretId=resource)
        tag_list = response.get("Tags", [])
        tags = [TagModel(key=a["Key"], value=a["Value"]) for a in tag_list]
        return TagList(tags=tags)

    def add_tag(self, resource, tag_key, tag_value):
        self.client.tag_resource(SecretId=resource,
                               Tags=[{"Key": tag_key,
                                      "Value": tag_value}])
