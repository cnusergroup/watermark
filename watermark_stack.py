from aws_cdk import (
    Stack,
    CfnOutput,
    RemovalPolicy,
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_s3_deployment as s3deploy,
)
from constructs import Construct


class WatermarkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(
            self, "SiteBucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        )

        distribution = cloudfront.Distribution(
            self, "SiteDistribution",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3BucketOrigin.with_origin_access_control(bucket),
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            ),
            default_root_object="index.html",
        )

        s3deploy.BucketDeployment(
            self, "DeploySite",
            sources=[s3deploy.Source.asset(".", exclude=["cdk.out", "*.py", "__pycache__", ".git", "node_modules", "cdk.json", "requirements.txt", "README.md", "deploy-info.txt", ".venv"])],
            destination_bucket=bucket,
            distribution=distribution,
        )

        CfnOutput(self, "CloudFrontURL", value=f"https://{distribution.distribution_domain_name}")
