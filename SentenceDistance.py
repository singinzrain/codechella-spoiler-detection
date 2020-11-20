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
    print(dist)
    return dist
    
if __name__ == '__main__':
  a = SentenceDistance()
  tweet = open('dummyTweet.txt', 'r').read()
  summary = ""
  for paragraph in open('dummySummary.txt', 'r'):
    summary += paragraph
  a.similarity(summary, tweet)