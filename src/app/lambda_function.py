import json

def handler(event, context):
    print(event)
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "*/*"
        },
        "body": json.dumps(
            {
                "project": "python-app-pokemon-restapi",
                "version": "v2"
            }
        )
    }