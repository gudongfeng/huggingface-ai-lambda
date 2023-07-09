import os
from pathlib import Path
from aws_cdk import (
    aws_lambda as lambda_,
    aws_efs as efs,
    aws_ec2 as ec2
)
from aws_cdk import App, Stack, Duration, RemovalPolicy, Tags

from constructs import Construct

class ServerlessHuggingFaceStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # %%
        # iterates through the Python files in the docker directory
        docker_folder = os.path.dirname(os.path.realpath(__file__)) + "/inference"
        pathlist = Path(docker_folder).rglob('*.py')
        for path in pathlist:
            base = os.path.basename(path)
            filename = os.path.splitext(base)[0]
            # Lambda Function from docker image
            lambda_.DockerImageFunction(
                self, filename,
                code=lambda_.DockerImageCode.from_image_asset(docker_folder,
                                                              cmd=[
                                                                  filename+".handler"]
                                                              ),
                memory_size=4096,
                timeout=Duration.seconds(600),
                architecture=lambda_.Architecture.ARM_64,
                environment={"TRANSFORMERS_CACHE": "/tmp/hf_models_cache"},
            )

app = App()

stack = ServerlessHuggingFaceStack(app, "ServerlessHuggingFaceStack")
Tags.of(stack).add("AwsSample", "ServerlessHuggingFace")

app.synth()