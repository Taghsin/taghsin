from helper.aws_helper import ServiceBase
from schemas.tag import TagModel, TagList
from botocore.exceptions import ClientError


class S3Helper(ServiceBase):

    def __init__(self):
        super().__init__("s3")

    def list_tags(self, resource):
        try:
            response = self.client.get_bucket_tagging(Bucket=resource)
            tag_list = response.get("TagSet", [])
            tags = [TagModel(key=a["Key"], value=a["Value"]) for a in tag_list]
            return TagList(tags=tags)
        except ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchTagSet':
                return TagList(tags=[])
            else:
                raise e

    def add_tag(self, resource, tag_key, tag_value):
        self.client.put_bucket_tagging(Bucket=resource,
                                       Tagging={'TagSet': [{'Key': tag_key,
                                                            'Value': tag_value},]})
