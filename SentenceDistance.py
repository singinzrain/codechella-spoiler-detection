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

  def similarity(self, sentence_one, sentence_two):
    sentences = [sentence_one, sentence_two]
    self.infersent.update_vocab(sentences)
    vectorized_one, vectorized_two = self.infersent.encode(sentences, tokenize=True)
    dist = ((vectorized_one-vectorized_two)**2).sum()
    return dist
  
  def classify_spoiler(self, tweet, summary, threshold=5.0):
    for sentence in summary.split("."):
      score = self.similarity(tweet, sentence)
      print("{} : {}".format(score, sentence))
      print("===============")
      if score < threshold:
        return True
    return False
    
def find_threshold(model, sentences):
  from tqdm import tqdm
  sentence_ones, sentence_twos = sentences
  para_score = 0
  non_score = 0
  para_list = []
  non_list = []
  N = len(sentence_ones)
  print("Total Pairs to Iterate: {}".format(N))
  for index_i, i in tqdm(enumerate(sentence_ones)):
    for index_j, j in enumerate(sentence_twos):
      s = model.similarity(i, j)
      if index_i == index_j:
        para_score += s
        para_list.append(s)
      else:
        non_score += s
        non_list.append(s)
  para_score /= N
  non_score  /= N**2 - N

  print("P: {} - {}".format(para_score, para_list))
  print("N: {} - {}".format(non_score, non_list))
  
def mrpc_tests(model, sample_size=10):
  import pandas as pd
  import csv
  paraphrases = pd.read_csv("InferSent/msr_paraphrase_train.txt", sep="\t", quoting=csv.QUOTE_NONE)
  paraphrases = paraphrases.query("Quality==1").sample(sample_size)
  sentence_ones = paraphrases["#1 String"].tolist()
  sentence_twos = paraphrases["#2 String"].tolist()
  find_threshold(model, (sentence_ones, sentence_twos))

def custom_tests_one(model):
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
  find_threshold(model, (ones, twos))

def custom_tests_two(model):
  ones = [
    'Following Stark\'s funeral,',
    'Following Stark\'s funeral, Thor appoints Valkyrie as the new ruler of New Asgard and joins the Guardians',
    'Following Stark\'s funeral, Thor appoints Valkyrie as the new ruler of New Asgard and joins the Guardians', 
  ]
  twos = [
    "Dawg it’s still tough watching tony stark die",
    "the last time I cried this hard I watched Tony Stark die in endgame I literally feel like death #UnusAnnus",
    "literally my entire classroom the day after kt came out was TONY STARK DIES HEHEHEHE",
  ]
  find_threshold(model, (ones, twos))

if __name__ == '__main__':
  a = SentenceDistance()
  tweet = open('dummyTweet.txt', 'r').read()
  summary = ""
  for paragraph in open('dummySummary.txt', 'r'):
    summary += paragraph
  
  #result = a.classify_spoiler(tweet, summary, threshold=0.0)
  
  print("==============================")
  custom_tests_one(a)
  print("==============================")
  custom_tests_two(a)
  #print("==============================")
  #mrpc_tests(a)