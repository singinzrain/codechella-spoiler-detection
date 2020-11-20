import torch
import nltk
from InferSent.model import InferSent
INFERSENT_VERSION = 2

class SentenceDistance:
  def __init__(self):
    nltk.download('punkt')
    W2V_PATH = 'InferSent/crawl-300d-2M.vec'
    MODEL_PATH = 'InferSent/infersent%s.pkl' % INFERSENT_VERSION
    params_model = {
      'bsize': 64,
      'word_emb_dim': 300,
      'enc_lstm_dim': 2048,
      'pool_type': 'max',
      'dpout_model': 0.0,
      'version': INFERSENT_VERSION
    }
    self.infersent = InferSent(params_model)
    self.infersent.load_state_dict(torch.load(MODEL_PATH))
    self.infersent.set_w2v_path(W2V_PATH)
    self.infersent.build_vocab_k_words(K=100000)


  def similarity(self, summary, tweet):
    sentences = [tweet, summary]
    self.infersent.update_vocab(sentences)
    vectorized_tweet, vectorized_summary = self.infersent.encode(sentences, tokenize=True)
    dist = ((vectorized_tweet-vectorized_summary)**2).sum()
    return dist
    
if __name__ == '__main__':
  a = SentenceDistance()
  tweet = open('dummyTweet.txt', 'r').read()
  summary = ""
  for paragraph in open('dummySummary.txt', 'r'):
    summary += paragraph
  result = a.similarity(summary, tweet)
  print("Tweet to Summary: {}".format(result))
  result = a.similarity(
    'I was walking by the store and saw a lady with a broken nose', 
    "Just outside of Vons, a girl was crying with a bloody nose."
  )
  print("Paraphrase: {}".format(result))
  
  result = a.similarity(
    'Coding sometimes can be very tedious and time consuming', 
    "Whoever becomes the president of the United States, he'll be better than Trump"
  )
  print("Not: {}".format(result))
  
  result = a.similarity(
    'Coding sometimes can be very tedious and time consuming', 
    "Sometimes, I find that programming is too laborious and I want to give it up"
  )
  print("Paraphrase: {}".format(result))
  
  result = a.similarity(
    'Trump might be the worse president of all time.', 
    "Whoever becomes the president of the United States, he'll be better than Trump"
  )
  print("Paraphrase: {}".format(result))
  
