import json
from transformers import pipeline

# voiceToText = pipeline("automatic-speech-recognition")

voiceToText = pipeline("summarization", model="t5-small")

def handler(event, context):
    body = json.loads(event['body'])
    result = voiceToText(body['input'])
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(result[0])
    }
    return response
