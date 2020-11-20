from flask import Flask
from flask import jsonify

from model.tweet import Tweet

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/tweets')
def get_tweets():
    # mock
    # should get from core
    tweet = Tweet()
    tweet.content = "test"
    tweets = [tweet.__dict__]

    return jsonify(tweets)


@app.route('/check')
def check_spoiler():
    return "1"


@app.route('/summary/<movie_name>')
def get_summary(movie_name):
    return ""
