import boto3

from schemas.tag import TagModel, TagList


class AwsHelper:
    def __init__(self, service_name):
        self.client = boto3.client(service_name)


class ServiceBase(AwsHelper):
    def __init__(self, service_name):
        super().__init__(service_name=service_name)

    def list_tags(self, resource: str) -> TagList:
        print("implement list_tags method!")
        return TagList([])

    def add_tag(self, resource, tag_key, tag_value):
        print("implement add_tag method!")

    def check_tag_exists(self, tag_list: TagList, tag_key: str) -> bool:
        for tag in tag_list.tags:
            if tag.key == tag_key:
                return True
        return False

    def tagging(self, resource: str, tag: TagModel) -> bool:
        tag_list = self.list_tags(resource=resource)
        tag_exist = self.check_tag_exists(tag_list=tag_list, tag_key=tag.key)
        if not tag_exist:
            self.add_tag(resource=resource, tag_key=tag.key,
                         tag_value=tag.value)
            return True
        return False
