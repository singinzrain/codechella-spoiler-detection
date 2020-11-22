from typing import List

from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin

from SentenceDistance import SentenceDistance
from entity_recognition import get_entities
from model.tweet import Tweet
from util.TweepyWrapper import TweepyWrapper
from tweepy import Status

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
sentence_distance = SentenceDistance()

@app.route('/')
@cross_origin()
def hello_world():
    return 'Hello, World!'


@app.route('/tweets')
@cross_origin()
def get_tweets():
    result = get_tweet_list()
    return jsonify(result)


def get_tweet_list():
    tweets: List[Status] = TweepyWrapper().get_trending_tweets_in_LA(limit=10)
    result = []
    for t in tweets:
        tweet = Tweet.parse_from_status(t)
        result.append(tweet.__dict__)
    return result


@app.route('/similarTweets/<tweet_id>')
@cross_origin()
def get_similar_tweets(tweet_id):
    print(tweet_id)
    print("==============================")
    tweets = []
    # get the tweet
    tweet = TweepyWrapper().get_tweet(tweet_id)
    original = Tweet.parse_from_status(tweet)

    # extract entities
    entities: List[str] = get_entities(original.text)

    retry_count = 0
    limit = 5
    while len(tweets) < limit and retry_count < 5:
        # find tweets with entities
        statuses = []
        for entity in entities:
            statuses.extend(TweepyWrapper().get_tweets_by_keyword(keyword=entity, limit=15))

        potential_tweets: List[Tweet] = [Tweet.parse_from_status(t) for t in statuses]

        # filter similarities
        #print(len(tweets), retry_count, "===========================================")
        for potential_tweet in potential_tweets:
            similarity = sentence_distance.similarity(original.text, potential_tweet.text)
            #print(similarity)
            # todo judge whether eligible
            tweets.append(potential_tweet.__dict__)
            if len(tweets) > limit:
              break

        # repeat if less than 15
        retry_count += 1

    return jsonify(tweets)
