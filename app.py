#!/usr/bin/env python3
from aws_cdk import (
    core as cdk
)

from cdk_appsync.cdk_appsync_stack import CdkAppSyncStack


app = cdk.App()
CdkAppSyncStack(app, "CdkAppSyncStack")

app.synth()
