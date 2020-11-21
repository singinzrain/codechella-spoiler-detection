from flask import Flask, request
from flask import jsonify

from model.tweet import Tweet
from util.search_tweet import search

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/tweets')
def get_tweets():
    result = search(["codechella"], 15)
    tweets = []
    for t in result['statuses']:
        tweet = Tweet()
        tweet.content = t['text']
        tweets.append(tweet.__dict__)

    return jsonify(tweets)
