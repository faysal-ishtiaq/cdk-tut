from aws_cdk import (
    core,
    aws_lambda as _lambda
)


class CdkTutStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        lambda_greetings = _lambda.Function(
            self, 'GreetingsHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='greetings.greet',
            memory_size=128
        )
