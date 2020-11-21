from flask import Flask, request
from flask import jsonify

from model.tweet import Tweet

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/tweets')
def get_tweets():
    tweet = Tweet()
    tweet.content = "test"
    tweets = [tweet.__dict__]

    return jsonify(tweets)


@app.route('/check', methods=['POST'])
def check_spoiler():
    # list of tweets from request
    request_json = request.get_json()

    result = []
    for content in request_json['tweets']:
        tweet = Tweet()
        tweet.content = content

        # get movie title from IMDB api
        tweet.movie_title = "title"

        # get the Wikipedia plot summary
        tweet.plot = "plot"

        # get the compare result between plot summary and tweet content
        tweet.is_spoiler = 1

        result.append(tweet.__dict__)

    return jsonify(result)


@app.route('/summary/<movie_name>')
def get_summary(movie_name):
    # get the Wikipedia plot summary
    return ""
