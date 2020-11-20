import torch
from transformers import DistilBertModel, DistilBertTokenizer
from sklearn.neighbors import DistanceMetric

class SpoilerDetection:
  def __init__(self):
    self.tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    self.embedding = DistilBertModel.from_pretrained('distilbert-base-uncased')

  def pad(self, tensor, goal_length):
    curr_length = tensor.shape[1]
    pad_length = goal_length - curr_length
    goal_dim = (1, pad_length)
    zeros = torch.zeros(goal_dim).type(torch.int64)
    return torch.cat((tensor, zeros), dim=1)

  def vectorize(self, sentence, max_length=280):
    indexed_vector = self.tokenizer(sentence, return_tensors='pt')
    indexed_vector["input_ids"] = self.pad(indexed_vector.input_ids, max_length)
    indexed_vector["attention_mask"] = self.pad(indexed_vector.attention_mask, max_length)
    vectorized_sentence = self.embedding(**indexed_vector)[0]
    return vectorized_sentence
    
  def similarity(self, summary, tweet):
    vectorized_tweet = self.vectorize(tweet)

    # assume that summary can be broken down into paragraphs
    distances = []
    for i in summary.split("\n"):
      vectorized = self.vectorize(i)
      dist = ((vectorized_tweet-vectorized)**2).sum()
      distances.append(dist.item())
    print(distances)

if __name__ == '__main__':
  a = SpoilerDetection()
  tweet = open('dummyTweet.txt', 'r').read()
  summary = ""
  for paragraph in open('dummySummary.txt', 'r'):
    summary += paragraph
  a.similarity(summary, tweet)