from helper.aws_helper import ServiceBase
from schemas.tag import TagModel, TagList


class RedshiftHelper(ServiceBase):

    def __init__(self):
        super().__init__("redshift")

    def list_tags(self, resource):
        response = self.client.describe_tags(ResourceName=resource)
        if len(response['TaggedResources']) >0 :
            try:
                tag_list = response.get("TaggedResources", [])
                tags = [TagModel(key=tag_list[0]["Tag"]["Key"], value=tag_list[0]["Tag"]["Value"]) for a in tag_list[0]["Tag"]]
                return TagList(tags=tags)
            except AttributeError:
                pass
        else:
            tags = [TagModel(key="", value="")]
            return TagList(tags=tags)
            

    def add_tag(self, resource, tag_key, tag_value):
        self.client.create_tags(ResourceName=resource,
                                Tags=[{"Key": tag_key,
                                       "Value": tag_value}])
