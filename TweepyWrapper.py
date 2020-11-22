import tweepy

class TweepyWrapper:
  def __init__(self):
    consumer_key = "M0bhWx18SyJo5z7dwSeiepxlw"
    consumer_secret = "hXfmVLgarc64UlcRSnGncQgSVB1lBK0TJvI8fRABSGDZSoJxGV"
    access_token = "1289490941095473155-Ec4gSy89nzQxejSRooIiJdrJ1ko9zr"
    access_token_secret = "oj8cP7hFvMZiugcvQ8lx89qOIrN4tR0gpVQlQW8LE1Jjt"
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    self.api = tweepy.API(auth)

  def get_trending_tweets_in_LA(self, limit=15):
    # 15 tweets that talk about 15 trending topics in LA
    los_angeles_woeid = 2442047
    trends_obj = self.api.trends_place(los_angeles_woeid, exclude="hashtags")
    words = [x['query'] for x in trends_obj[0]['trends']][:limit]
    results = []
    for t in trends_obj[0]['trends'][:limit]:
      results.append(self.api.search(t['query'])[0]._json)
    return results
  
  def get_similar_tweets(self, tweet_id, limit=15):
    # get the tweet
    tweet_obj = self.api.statuses_lookup([tweet_id])[0]._json
    # extract entities
    # rakshithn's code

    # filter similarities
    # use Infersent
    
    # repeat if less than 15
    
