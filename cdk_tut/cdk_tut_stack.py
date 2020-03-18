from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as api_gateway
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

        api_stage_options = api_gateway.StageOptions(stage_name="dev")
        api = api_gateway.LambdaRestApi(self, 'Endpoint', handler=lambda_greetings, deploy_options=api_stage_options)

        get_items_handler = _lambda.Function(
            self, 'GetItems',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='items.get',
            memory_size=128
        )

        post_items_handler = _lambda.Function(
            self, 'PostItems',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='items.post',
            memory_size=128
        )

        get_items_integration = api_gateway.LambdaIntegration(get_items_handler)
        post_items_integration = api_gateway.LambdaIntegration(post_items_handler)

        items = api.root.add_resource("items")
        items.add_method("GET", get_items_integration)
        items.add_method("POST", post_items_integration)

        get_item_handler = _lambda.Function(
            self, 'GetItem',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='item.get',
            memory_size=128
        )

        post_item_handler = _lambda.Function(
            self, 'PostItem',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='item.post',
            memory_size=128
        )

        get_item_integration = api_gateway.LambdaIntegration(get_item_handler)
        post_item_integration = api_gateway.LambdaIntegration(post_item_handler)

        item = items.add_resource("{item}")
        item.add_method("GET", get_item_integration)
        item.add_method("POST", post_item_integration)

