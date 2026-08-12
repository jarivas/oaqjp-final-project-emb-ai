import requests

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyse):
	req = { "raw_document": { "text": text_to_analyse } }
	result = None
	
	response = requests.post(URL, json=req, headers=HEADERS)

	if response.status_code == 200:
		result = response.text
	
	return result