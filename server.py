from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application
    page over the Flask channel.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector():
    """
    This function receives the text from the HTML interface and
    runs emotion detection over it using the emeotion_detector()
    function. The output returned shows the emotions, scores and the dominant emotion for the provided text.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")
    # Pass the text to the emeotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the emotion, score and dominant_emotion from the response
    anger = response.get("anger")
    disgust = response.get("disgust")
    fear = response.get("fear")
    joy = response.get("joy")
    sadness = response.get("sadness")
    dominant_emotion = response.get("label")

    return f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
