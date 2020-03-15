#!/usr/bin/env python3

from aws_cdk import core

from cdk_tut.cdk_tut_stack import CdkTutStack


app = core.App()
CdkTutStack(app, "cdk-tut")

app.synth()
