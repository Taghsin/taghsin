from helper.aws_helper import ServiceBase
from schemas.tag import TagModel, TagList


class IamRoleHelper(ServiceBase):

    def __init__(self):
        super().__init__("iam")

    def list_tags(self, resource):
        response = self.client.list_role_tags(RoleName=resource)
        tag_list = response.get("Tags", [])
        tags = [TagModel(key=a["Key"], value=a["Value"]) for a in tag_list]
        return TagList(tags=tags)

    def add_tag(self, resource, tag_key, tag_value):
        self.client.tag_role(RoleName=resource,
                             Tags=[{"Key": tag_key,
                                    "Value": tag_value}])


class IamUserHelper(ServiceBase):

    def __init__(self):
        super().__init__("iam")

    def list_tags(self, resource):
        response = self.client.list_user_tags(UserName=resource)
        tag_list = response.get("Tags", [])
        tags = [TagModel(key=a["Key"], value=a["Value"]) for a in tag_list]
        return TagList(tags=tags)

    def add_tag(self, resource, tag_key, tag_value):
        self.client.tag_user(UserName=resource,
                             Tags=[{"Key": tag_key,
                                    "Value": tag_value}])


class IamPolicyHelper(ServiceBase):

    def __init__(self):
        super().__init__("iam")

    def list_tags(self, resource):
        response = self.client.list_policy_tags(PolicyArn=resource)
        tag_list = response.get("Tags", [])
        tags = [TagModel(key=a["Key"], value=a["Value"]) for a in tag_list]
        return TagList(tags=tags)

    def add_tag(self, resource, tag_key, tag_value):
        self.client.tag_policy(PolicyArn=resource,
                               Tags=[{"Key": tag_key,
                                      "Value": tag_value}])
