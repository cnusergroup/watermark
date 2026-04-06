#!/usr/bin/env python3
import aws_cdk as cdk
from watermark_stack import WatermarkStack

app = cdk.App()
WatermarkStack(app, "WatermarkStack")
app.synth()
