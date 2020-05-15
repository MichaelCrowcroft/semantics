from flask import Flask
from flask_restful import Resource, Api, reqparse
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
api = Api(app)

vader_analyser = SentimentIntensityAnalyzer()
parser = reqparse.RequestParser()
parser.add_argument('text')

class Sentiment(Resource):
    def get(self):
        return "working, post your text to this resource."

    def post(self):
        args = parser.parse_args()
        text = args['text']
        sentiment = vader_analyser.polarity_scores(text)
        return sentiment

api.add_resource(Sentiment, '/sentiment')

if __name__ == '__main__':
    app.run(debug=True)

