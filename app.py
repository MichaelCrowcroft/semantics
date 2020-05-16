from flask import Flask, jsonify
from resources.sentiment import Sentiment
from resources.readability import Readability

app = Flask(__name__)

app.add_url_rule('/sentiment', view_func=Sentiment.as_view('sentiment'))
app.add_url_rule('/readability', view_func=Readability.as_view('readability'))

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
