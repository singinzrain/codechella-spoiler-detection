from typing import List

from flask import Flask
from flask import jsonify

from SentenceDistance import SentenceDistance
from entity_recognition import get_entities
from model.tweet import Tweet
from util.TweepyWrapper import TweepyWrapper
from tweepy import Status

app = Flask(__name__)
sentence_distance = SentenceDistance()

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/tweets')
def get_tweets():
    result = get_tweet_list()
    return jsonify(result)


def get_tweet_list():
    tweets: List[Status] = TweepyWrapper().get_trending_tweets_in_LA(limit=3)
    result = []
    for t in tweets:
        tweet = Tweet.parse_from_status(t)
        result.append(tweet.__dict__)
    return result


@app.route('/similarTweets/<tweet_id>')
def get_similar_tweets(tweet_id: str):
    tweets = []
    # get the tweet
    tweet = TweepyWrapper().get_tweet("1330311987075682304")
    original = Tweet.parse_from_status(tweet)

    # extract entities
    entities: List[str] = get_entities(original.text)

    retry_count = 0
    while len(tweets) < 15 and retry_count < 5:
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

        # repeat if less than 15
        retry_count += 1

    return jsonify(tweets)
