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
    } # this cannot be changed since we are loading a pre-trained model
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
    
def find_threshold(sentenceDistanceObj):
  import pandas as pd
  import csv
  from tqdm import tqdm
  paraphrases = pd.read_csv("InferSent/msr_paraphrase_train.txt", sep="\t", quoting=csv.QUOTE_NONE)
  paraphrases = paraphrases.query("Quality==1").sample(10)
  sentence_ones = paraphrases["#1 String"].tolist()
  sentence_twos = paraphrases["#2 String"].tolist()
  para_score = 0
  non_score = 0
  for index_i, i in enumerate(sentence_ones):
    print(index_i)
    for index_j, j in tqdm(enumerate(sentence_twos)):
      if index_i == index_j:
        para_score += sentenceDistanceObj.similarity(i, j)
      else:
        non_score += sentenceDistanceObj.similarity(i, j)
  para_score /= len(sentence_ones)
  non_score /= (len(sentence_ones)**2-len(sentence_ones))
  print("P: {} \t N: {}".format(para_score, non_score))

def custom_tests(a):
  ones = [
    'I was walking by the store and saw a lady with a broken nose', 
    'Coding sometimes can be very tedious and time consuming', 
    'Trump might be the worse president of all time.', 
  ]
  twos = [
    "Just outside of Vons, a girl was crying with a bloody nose.",
    "Sometimes, I find that programming is too laborious and I want to give it up",
    "Whoever becomes the president of the United States, he'll be better than Trump"
  ]
  for i, si in enumerate(ones):
    for j, sj in enumerate(twos):
      result = a.similarity(si, sj)
      if i==j:
        print("P: {}".format(result))
      else:
        print("N: {}".format(result))

if __name__ == '__main__':
  a = SentenceDistance()
  tweet = open('dummyTweet.txt', 'r').read()
  summary = ""
  for paragraph in open('dummySummary.txt', 'r'):
    summary += paragraph
  result = a.similarity(summary, tweet)
  print("Tweet to Summary: {}".format(result))
  print("==============================")
  custom_tests(a)
  print("==============================")
  find_threshold(a)