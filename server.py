from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)
  
    # Return a formatted string with the emotions and dominant emotion in requested format
    response_str = f"""For the given statement, the system response is
    'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']},
    'joy': {response['joy']}, 'sadness': {response['sadness']}.
    The dominant emotion is <strong>{response['dominant_emotion']}</strong>."""

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)