import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=input_json, headers=header)
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        emotion_values = formatted_response['emotionPredictions'][0]['emotion']
        max_emotion = max(emotion_values, key=emotion_values.get)
    # If the response status code is 400, set label and score to None
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        emotion_values = None
        max_emotion = None
 
    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': max_emotion
            }

            
# emotion_detector("I love this new technology.")
# from emotion_detection import emotion_detector && emotion_detector("I love this new technology.")
