#!/usr/bin/env python3
import os

import aws_cdk as cdk

from my_pipeline.my_pipeline_stack import MyPipelineStack


app = cdk.App()
MyPipelineStack(app, "MyPipelineStack",
    env=cdk.Environment(account="434167029606", region="eu-east-1")
    )

app.synth()
