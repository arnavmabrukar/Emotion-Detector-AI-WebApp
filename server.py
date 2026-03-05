from flask import flask, render_template. request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detection')

@app.route("/emtoionDetection")
def emo_detector():
    input_text = request.args.get("textToAnalyze")
    response = emotion_detector(input_text)

    return f"For the given statement, the system response is
    {response['anger']}, {response['disgust']}, {response['fear']},
    {response['joy']} and {response['sadness']}. 
    The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)