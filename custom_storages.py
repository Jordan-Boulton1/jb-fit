# Import the S3Boto3Storage class from Django storages package
from storages.backends.s3boto3 import S3Boto3Storage


# Define a custom storage class for handling static files
class StaticStorage(S3Boto3Storage):
    # Set the location within the S3 bucket for static files
    location = 'static'

    # Set the default access control list (ACL)
    # to make static files publicly readable
    default_acl = 'public-read'


# Define a custom storage class for handling media files
class MediaStorage(S3Boto3Storage):
    # Set the location within the S3 bucket for media files
    location = 'media'

    # Set the default access control list (ACL)
    # to make media files publicly readable
    default_acl = 'public-read'
