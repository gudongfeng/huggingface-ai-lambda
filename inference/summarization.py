from transformers import pipeline

# voiceToText = pipeline("automatic-speech-recognition")

voiceToText = pipeline("summarization", model="t5-small")

def handler(event, context):
    result = voiceToText(event['input'])
    response = {
        "statusCode": 200,
        "body": result
    }
    return response
