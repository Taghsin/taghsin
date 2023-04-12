from helper.aws_helper import ServiceBase
from schemas.tag import TagModel, TagList


class CloudFrontHelper(ServiceBase):

    def __init__(self):
        super().__init__("cloudfront")

    def list_tags(self, resource):
        response = self.client.list_tags_for_resource(
            Resource=resource)
        tag_list = response['Tags'].get('Items', [])
        tags = [TagModel(key=a["Key"], value=a["Value"]) for a in tag_list]
        return TagList(tags=tags)

    def add_tag(self, resource, tag_key, tag_value):
        self.client.tag_resource(Resource=resource,
                                            Tags={'Items': [{ 'Key': tag_key, 
                                                              'Value': tag_value},]})
