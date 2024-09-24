from typing import Optional

from agenteval.targets import BaseTarget
from agenteval.utils import create_boto3_client

_DEFAULT_MAX_RETRY = 10


class Boto3Target(BaseTarget):
    """A target that can be interfaced with via the `boto3` library.

    Attributes:
        boto3_client (BaseClient): A `boto3` client.
    """

    def __init__(
        self,
        boto3_service_name: str,
        aws_profile: Optional[str] = None,
        aws_region: Optional[str] = None,
        endpoint_url: Optional[str] = None,
        max_retry: int = _DEFAULT_MAX_RETRY,
    ):
        """
        Initialize the AWS target.

        Args:
            boto3_service_name (str): The `boto3` service name (e.g `"bedrock-agent-runtime"`).
            aws_profile (str, optional): The AWS profile name.
            aws_region (str, optional): The AWS region.
            endpoint_url (str, optional): The endpoint URL for the AWS service.
            max_retry (int, optional): The maximum number of retry attempts.
        """

        self.boto3_client = create_boto3_client(
            boto3_service_name=boto3_service_name,
            aws_profile=aws_profile,
            aws_region=aws_region,
            endpoint_url=endpoint_url,
            max_retry=max_retry,
        )
