import requests  
# Import the requests lib
import json  


def emotion_detector(text_to_analyse):  # using a string input return back the emotion response
    # URL to call
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    # Text dictionary to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } } 
    #header to send
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    
    # Send the API our payload
    response = requests.post(url, json = myobj, headers=header)  
    # parse JSON response
    formatted_response = json.loads(response.text)
    #pull out dictionary of emotions
    emotion_dict=formatted_response['emotionPredictions'][0]['emotion']
    #define a variable for each
    anger = emotion_dict['anger']
    disgust = emotion_dict['disgust']
    fear = emotion_dict['fear']
    joy = emotion_dict['joy']
    sadness = emotion_dict['sadness']
    #find the max score and the corresponding key
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    #ready formatted response
    formatted_response_dict={
        'anger': anger,
        'disgust':disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
    
    return formatted_response_dict