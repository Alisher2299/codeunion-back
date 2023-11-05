from types import MappingProxyType

DEFAULT_STORAGE: str = "django.core.files.storage.FileSystemStorage"

FILE_STORAGES: MappingProxyType = MappingProxyType(
    mapping={
        "LOCAL": DEFAULT_STORAGE,
        "AWS_S3": "storages.backends.s3boto3.S3Boto3Storage",
    }
)

DEFAULT_S3_OBJECT_PARAMETERS: MappingProxyType = MappingProxyType(
    mapping={
        "CacheControl": "max-age=86400",
    }
)
