from flask import Flask
from flask import jsonify
import TweepyWrapper

from model.tweet import Tweet

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/tweets')
def get_tweets():
    tweets = TweepyWrapper.get_trending_tweets_in_LA()
    return jsonify(tweets)

@app.route('/similarTweets')
def get_similar_tweets():

    return jsonify(tweets)


@app.route('/check')
def check_spoiler():
    return "1"


@app.route('/summary/<movie_name>')
def get_summary(movie_name):
    return ""
