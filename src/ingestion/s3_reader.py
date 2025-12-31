import boto3
import logging
from typing import List

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client("s3")

class S3DocumentReader:
    def __init__(self, bucket_name: str, prefix: str = "raw-documents/"):
        self.bucket_name = bucket_name
        self.prefix = prefix

    def list_documents(self) -> List[str]:
        """List document keys under the given prefix."""
        response = s3.list_objects_v2(
            Bucket=self.bucket_name,
            Prefix=self.prefix
        )
        contents = response.get("Contents", [])
        return [obj["Key"] for obj in contents if not obj["Key"].endswith("/")]

    def read_document(self, key: str) -> str:
        """Read a document from S3 and return its content as text."""
        logger.info(f"Reading document from S3: {key}")
        obj = s3.get_object(Bucket=self.bucket_name, Key=key)
        return obj["Body"].read().decode("utf-8")
