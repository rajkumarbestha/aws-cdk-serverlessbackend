
from aws_cdk import (
    aws_s3 as s3,
    core
)

# Commented Lines are useful while S3 bucket hosting.
class CustomS3(s3.Bucket):

    def __init__(self, scope: core.Construct, id, bucket_name): #public_read_access, website_index_document, website_error_document):

        super().__init__(scope = scope, id = id, bucket_name=bucket_name, 
            removal_policy=core.RemovalPolicy.DESTROY, 
            block_public_access =s3.BlockPublicAccess(restrict_public_buckets=True))

            # access_control = s3.BucketAccessControl.PUBLIC_READ, 
            # public_read_access=public_read_access, 
            # #website_error_document=website_error_document, 
            # website_index_document=website_index_document)
    
    # self.grant_public_access()
    # self.add_cors_rule(allowed_methods=[s3.HttpMethods.GET], allowed_origins=['*'])
