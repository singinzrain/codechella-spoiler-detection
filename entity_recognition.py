from typing import List

import spacy
nlp = spacy.load("en_core_web_sm")
# example text
# text = """First of all, my obvious answer is Grave of The Fireflies. The emotional labor--no thank you. Second of all, the less obvious answer is A Whisker Away, because it was so well-made and relatable in my opinion that I was crying throughout.
#         Third of all (yes), the least obvious answer is Perfect Blue. Even I couldn't believe that I was willing to watch Hereditary once....twice....but not Perfect Blue.
#         It was definitely ahead of its time though.Maybe it's just me, but animations hit me deeper in the feels."""
#
# text2 = '''I was still a little mind-boggled the first time I watched Inception, but I got the basic gist of what was going on and how it all worked;
# with Interstellar and Tenet, when I looked things up on Wikipedia, there were several moments of "Wait, that happened?" "They said that?"'''
# doc = nlp(text2)
# for ent in doc.ents:
#     print(ent.text, ent.label_)
#

def get_entities(text: str) -> List[str]:
    doc = nlp(text)
    result = [ent.text for ent in doc.ents]
    print(result)
    return result

# python -m spacy download en_core_web_sm
# import nltk
# import re
# import math
# import numpy as np
# from itertools import chain
# from collections import Counter
# import nltk
# from nltk.util import ngrams # This is the ngram magic.
# from textblob import TextBlob
# import xlrd
# import pandas as pd

# nltk.download('punkt')
# NGRAM = 2

# re_sent_ends_naive = re.compile(r'[.\n]')
# re_stripper_alpha = re.compile('[^a-zA-Z]+')
# re_stripper_naive = re.compile('[^a-zA-Z\.\n]')

# splitter_naive = lambda x: re_sent_ends_naive.split(re_stripper_naive.sub(' ', x))

# sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

# def get_tuples_nosentences(txt):
#     if not txt: return None
#     ng = ngrams(re_stripper_alpha.sub(' ', txt).split(), NGRAM)
#     return list(ng)

# def get_tuples_manual_sentences(txt):
#     if not txt: return None
#     sentences = (x.split() for x in splitter_naive(txt) if x)
#     ng = (ngrams(x, NGRAM) for x in sentences if len(x) >= NGRAM)
#     return list(chain(*ng))

# def get_tuples_nltk_punkt_sentences(txt):
#     if not txt: return None
#     sentences = (re_stripper_alpha.split(x) for x in sent_detector.tokenize(txt) if x)

#     ng = (ngrams(filter(None, x), NGRAM) for x in sentences if len(x) >= NGRAM)
#     return list(chain(*ng))

# def get_tuples_textblob_sentences(txt):
#     if not txt: return None
#     tb = TextBlob(txt)
#     ng = (ngrams(x.words, NGRAM) for x in tb.sentences if len(x.words) > NGRAM)
#     return [item for sublist in ng for item in sublist]

# def jaccard_distance(a, b):
#     a = set(a)
#     b = set(b)
#     return 1.0 * len(a&b)/len(a|b)

# def cosine_similarity_ngrams(a, b):
#     vec1 = Counter(a)
#     vec2 = Counter(b)
    
#     intersection = set(vec1.keys()) & set(vec2.keys())
#     numerator = sum([vec1[x] * vec2[x] for x in intersection])

#     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
#     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
#     denominator = math.sqrt(sum1) * math.sqrt(sum2)

#     if not denominator:
#         return 0.0
#     return float(numerator) / denominator

# #--------------------------
# a = get_tuples_nosentences("It was the best of times.")
# b = get_tuples_nosentences("It was the")
# print("Jaccard: {}   Cosine: {}".format(jaccard_distance(a,b), cosine_similarity_ngrams(a,b)))
# #--------------------------

# embeddings_index = dict()
# f = open('glove.6B.50d.txt')

# for line in f:
#     values = line.split()
#     word = values[0]
#     coefs = np.asarray(values[1:], dtype='float32')
#     embeddings_index[word] = coefs

# f.close()
# print('Loaded %s word vectors.' % len(embeddings_index))

# for q in questions["ques_text"]:
#   q_vec.append(avg_sentence_vector(q.split(), num_features=50))

# q = np.array(q_vec)

# for t in temp:
#   # print(t)
#   temp_vec.append(avg_sentence_vector(t.split(), num_features=50))

# t = np.array(temp_vec)

# score = cosine_similarity(q, t)
# print(score.shape)

# def avg_sentence_vector(words, num_features):
#   stop=set(stopwords.words('english'))
#   featureVec = np.zeros((num_features,), dtype="float32")
#   nwords = 0

#   for word in words:
#     if (word not in stop):
#       if word in embeddings_index:
#         nwords = nwords+1
#         featureVec = np.add(featureVec, embeddings_index[word])

#   if nwords>0:
#     featureVec = np.divide(featureVec, nwords)
#   return featureVec


# # load a spaCy model, depending on language, scale, etc.

# # add PyTextRank to the spaCy pipeline
# tr = pytextrank.TextRank()
# nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)

# doc = nlp(text)

# # examine the top-ranked phrases in the document
# for p in doc._.phrases:
#     print("{:.4f} {:5d}  {}".format(p.rank, p.count, p.text))
#     print(p.chunks)