# -*- coding: utf-8 -*-
from resources import twitterCleanser as cleaner
from resources import analytics
from stemming.porter2 import stem
import scipy
import numpy
import sys
import operator
import lda

__author__ = 'gerson64'

restList = ["@burgerking", "@mcdonalds", "@pizzahut", "@tacobell", "@chipotletweets", "@qdobamexgrill",
            "@wendys", "@kfc", "@ChickfilA"]

for i in range(len(restList)):
    restList[i] = restList[i].lower()

#cleaner.dedupe_files("data/twitterstream.txt", "data/twitterstream_clean.txt")
#cleaner.dedupe_files("data/tweets1.txt", "data/firehose_clean.txt")

#cleaner.stem_files("data/twitterstream_clean.txt", "data/twitterstream_stemmed.txt")
#cleaner.stem_files("data/firehose_clean.txt", "data/firehose_stemmed.txt")

#foodFile = open("data/twitterstream_stemmed.txt", "r").read()
#firehoseFile = open("data/firehose_stemmed.txt", "r").read()

#tfidf_obj , twitter_stopwords = analytics.tfidf_stopwords( {'generic_tweets' :firehoseFile}  , {'food' : foodFile} )

#twitter_stopword_dict = dict()
#for i in twitter_stopwords.nonzero()[1]:
#    twitter_stopword_dict[tfidf_obj.get_feature_names()[i]] = twitter_stopwords[0, i]

import pickle
#with open('data/twitter_stopword_dict.dict', 'wb') as handle:
#  pickle.dump(twitter_stopword_dict, handle)

with open('data/twitter_stopword_dict.dict', 'rb') as handle:
  twitter_stopword_dict = pickle.loads(handle.read())


twitter_stopword_dict  = sorted(twitter_stopword_dict.items(), key=operator.itemgetter(1))

twitter_useword_dict_inv = reversed(twitter_stopword_dict[-500:])
#twitter_stopword_dict = twitter_stopword_dict[:500]

wordList = [x[0] for x in twitter_useword_dict_inv]
wordList = [elem for elem in wordList if len(elem) > 3 ]

#dat = cleaner.fileParse("data/twitterstream_clean.txt")

#parsedDat = cleaner.parseByList(dat, restList, wordList)

#with open('data/parsedDat.dict', 'wb') as handle:
#  pickle.dump(parsedDat, handle)
with open('data/parsedDat.dict', 'rb') as handle:
  parsedDat = pickle.loads(handle.read())

parsedDat = parsedDat.items()
key = [x[0] for x in parsedDat]
vals = [x[1] for x in parsedDat]

print filter(lambda x: len(x) , vals)

counters = []
for i in range(len(vals)):
  counters.append(analytics.wordcounter(vals[i]))

for i in range(len(restList)):
   restList[i] = stem(restList[i].strip()).lower().replace("@", "")
wordList = [elem for elem in wordList if elem not in restList]

outMatrix = []
outMatrix.append(['names'] + key)
for word in wordList:
    tmpList = [word]
    for wordCountObj in counters:
        tmpList = tmpList + [unicode(wordCountObj.get(word,0))]
    outMatrix.append(tmpList)

outMatrix = zip(*outMatrix)

import csv
with open("output.csv", "wb") as f:
    writer = csv.writer(f, delimiter=',')
    for outrow in outMatrix:
        writer.writerow([s.encode('ascii', 'ignore') for s in outrow])



