from datetime import datetime


def respond_success(body):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': body
    }


def greet(event, context):
    response = "Hi!!! Greetings from CDK. You have hit {} at {}".format(event.get('path'), datetime.now().isoformat())
    return respond_success(response)
