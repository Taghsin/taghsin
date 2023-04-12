from helper.aws_helper import ServiceBase
from schemas.tag import TagModel, TagList


class EC2Helper(ServiceBase):

    def __init__(self):
        super().__init__("ec2")

    def list_tags(self, resource):
        response = self.client.describe_tags(Filters=[{"Name": "resource-id",
                                                       "Values": [resource]}])
        tag_list = response.get("Tags", [])
        tags = [TagModel(key=a["Key"], value=a["Value"]) for a in tag_list]
        return TagList(tags=tags)

    def add_tag(self, resource, tag_key, tag_value):
        self.client.create_tags(Resources=[resource],
                                Tags=[{"Key": tag_key,
                                       "Value": tag_value}])
