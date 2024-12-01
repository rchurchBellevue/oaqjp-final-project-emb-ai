'''Server.py will invoke flask, call the emotion detector function
    and return back a formatted response based upon the text entered.'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def sent_analyzer():
    '''Call the emotion_detector function to gauge the emotions in the entered text;
    if no text is entered a default response message is returned.'''

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        response_str="Invalid text! Please try again!."
    # Return a formatted string with the emotions and dominant emotion in requested format
    else:
        response_str = f"""For the given statement, the system response is
        'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']},
        'joy': {response['joy']}, 'sadness': {response['sadness']}.
        The dominant emotion is <strong>{response['dominant_emotion']}</strong>."""

    return response_str

@app.route("/")
def render_index_page():
    '''Render the index page form for data entry'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
