# -*- coding: utf-8 -*-
__author__ = 'gerson64'
import nltk
import string
import os
import lda
import scipy
import numpy
import itertools

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

#http://www.cs.duke.edu/courses/spring14/compsci290/assignments/lab02.html

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    return tokens


def tfidf_stopwords(base_docs , compare_docs):
    #this can take some time
    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    tfidf.fit_transform(base_docs.values())
    return (tfidf , tfidf.transform(compare_docs.values()) )



#http://stackoverflow.com/questions/15899861/efficient-term-document-matrix-with-nltk
def fn_tdm_df(docs, xColNames = None, **kwargs):
    ''' create a term document matrix as pandas DataFrame
    with **kwargs you can pass arguments of CountVectorizer
    if xColNames is given the dataframe gets columns Names'''

    #initialize the  vectorizer
    vectorizer = CountVectorizer(**kwargs)
    x1 = vectorizer.fit_transform(docs)
    #create dataFrame
    df = pd.DataFrame(x1.toarray().transpose(), index = vectorizer.get_feature_names())
    if xColNames is not None:
        df.columns = xColNames

    return df

def wordcounter(inlist):
    wordcount = {}
    for word in inlist:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return wordcount