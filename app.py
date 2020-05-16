from flask import Flask, jsonify
from flask.views import MethodView

from webargs import fields, validate
from webargs.flaskparser import use_args, parser, abort

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

vader_analyser = SentimentIntensityAnalyzer()

class Sentiment(MethodView):
    text_args = {"text": fields.Str(required=True)}

    def get(self):
        return "Working, post your text to this resource."

    @use_args(text_args)
    def post(self, args):
        text = args['text']
        sentiment = vader_analyser.polarity_scores(text)
        return sentiment

app.add_url_rule('/sentiment', view_func=Sentiment.as_view('sentiment'))

# Return validation errors as JSON
@app.errorhandler(422)
@app.errorhandler(400)
def handle_error(err):
    headers = err.data.get("headers", None)
    messages = err.data.get("messages", ["Invalid request."])
    if headers:
        return jsonify({"errors": messages}), err.code, headers
    else:
        return jsonify({"errors": messages}), err.code

if __name__ == '__main__':
    app.run(debug=True)
