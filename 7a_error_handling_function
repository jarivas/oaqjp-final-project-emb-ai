import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyse):
    req = { "raw_document": { "text": text_to_analyse } }
    result = None
    
    response = requests.post(URL, json=req, headers=HEADERS)

    if response.status_code == 200:
        result = process_emotions(response.text)
    elif response.status_code == 400:
        result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return result

def process_emotions(text):
    emotions = json.loads(text)
    result = emotions["emotionPredictions"][0]["emotion"]
    dominant_emotion = None
    max_value = float('-inf')

    for key, value in result.items():
        if value > max_value:
            max_value = value
            dominant_emotion = key
 
    result["dominant_emotion"] = dominant_emotion

    return result