from typing import List

import tweepy
from tweepy import SearchResults, Status


class TweepyWrapper:
  def __init__(self):
    consumer_key = "8gMDJrzwTbClwJ6PqimjBTpW2"
    consumer_secret = "7DwAuSCNF4kvd04xL8ku58SxYQaRzScm3V6o2SUmkTtopxgo9u"
    access_token = "1322291841081905152-MqZoBnCq1lq1amSvc3sNStSHwOmhD8"
    access_token_secret = "FJDNtfqXOdJGxs3LTyEBTEOOzQYQ0TDj7yJuM2kT8SCvk"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    self.api = tweepy.API(auth)

  def get_trending_tweets_in_LA(self, limit=15) -> List[Status]:
    # 15 tweets that talk about 15 trending topics in LA
    los_angeles_woeid = 2442047
    trends_obj = self.api.trends_place(los_angeles_woeid, exclude="hashtags")
    words = [x['query'] for x in trends_obj[0]['trends']][:limit]
    results = []
    for word in words:
      r: SearchResults = self.api.search(q=word, count=1)
      print(r.__dict__)
      if len(r) > 0:
        results.append(r[0])
    return results

  def get_tweets_by_keyword(self, keyword, limit=15) -> List[Status]:
    results = []
    r: SearchResults = self.api.search(q=keyword, count=limit)
    print(r.__dict__)
    if len(r) > 0:
      results.append(r[0])
    return results

  def get_tweet(self, tweet_id) -> Status:
    tweet = self.api.statuses_lookup([tweet_id])
    print(tweet[0])
    return tweet[0]

