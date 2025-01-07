"""
Flask Application for Emotion Detection

This module provides a Flask-based web interface for detecting emotions 
in text. It includes routes for rendering the main page and handling 
emotion detection requests.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Render the main application page.
    
    Returns:
        str: Rendered HTML content for the main page.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def emo_detector():
    """
    Process text input from the client and detect emotions using 
    the emotion_detector function.

    Returns:
        str: A message with detected emotion scores and the dominant emotion.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # Validate input
    if not text_to_analyze:
        return "Invalid text! Please try again!"

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract emotion scores and the dominant emotion from the response
    anger = response.get("anger")
    disgust = response.get("disgust")
    fear = response.get("fear")
    joy = response.get("joy")
    sadness = response.get("sadness")
    dominant_emotion = response.get("dominant_emotion")

    # Handle invalid response
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Return the formatted response
    return (
        f"For the given statement, the system response is: "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
