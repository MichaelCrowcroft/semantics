from flask.views import MethodView
from webargs import fields, validate
from webargs.flaskparser import use_args, parser, abort
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

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