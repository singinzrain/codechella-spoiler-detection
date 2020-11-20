import torch
from transformers import DistilBertModel, DistilBertTokenizer
from sklearn.neighbors import DistanceMetric

class SentenceDistance:
  def __init__(self):
    pass

  def similarity(self, summary, tweet):
    return 0
    
if __name__ == '__main__':
  a = SentenceDistance()
  tweet = open('dummyTweet.txt', 'r').read()
  summary = ""
  for paragraph in open('dummySummary.txt', 'r'):
    summary += paragraph
  a.similarity(summary, tweet)