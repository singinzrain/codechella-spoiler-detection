from transformers import DistilBertModel, DistilBertTokenizer
from sklearn.neighbors import DistanceMetric

class SpoilerDetection:
  def __init__(self):
    self.tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    self.embedding = DistilBertModel.from_pretrained('distilbert-base-uncased')

  def similarity(summary, tweet):
    vectorized_tweet = self.tokenizer(tweet)
    semantic_matrix = self.embeddings(vectorized_tweet)
    print(semantic_matrix.shape)
    print("=============")

    # assume that summary can be broken down into paragraphs
    tweet_to_paragraph_distances = []
    for i in summary.split("\n"):
      tokenized = self.tokenizer(i)
      vectorized = self.embedding(tokenized)
      print(vectorized.shape)  


if __name__ == '__main__':
  a = SpoilerDetection()
  tweet = open('dummyTweet.txt', 'r').read()
  summary = ""
  for paragraph in open('dummySummary.txt', 'r'):
    summary += paragraph +"\n"
  a.similarity(summary[:-1], )