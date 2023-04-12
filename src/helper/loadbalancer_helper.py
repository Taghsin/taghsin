from helper.aws_helper import ServiceBase
from schemas.tag import TagModel, TagList


class LoadbalancerHelper(ServiceBase):

    def __init__(self):
        super().__init__("elb")

    def list_tags(self, resource):
        response = self.client.describe_tags(LoadBalancerNames=[resource])
        print(response)
        if len(response['TagDescriptions']) >0 :
            try:
                tag_list = response.get("TagDescriptions", [])
                tags = [TagModel(key=tag["Key"], value=tag["Value"]) for tag in  tag_list[0]["Tags"]]
                return TagList(tags=tags)
            except AttributeError:
                pass
        else:
            tags = [TagModel(key="", value="")]
            return TagList(tags=tags)

    def add_tag(self, resource, tag_key, tag_value):
        self.client.add_tags(LoadBalancerNames=[resource],
                                         Tags=[{"Key": tag_key,
                                               "Value": tag_value}])
