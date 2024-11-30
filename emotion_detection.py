import requests  
# Import the requests lib


def emotion_detector(text_to_analyse):  # using a string input return back the emotion response
    # URL to call
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    # Text dictionary to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } } 
    #header to send
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    
    # Send the API our payload
    response = requests.post(url, json = myobj, headers=header)  
    # Return the response as text
    return response.text  