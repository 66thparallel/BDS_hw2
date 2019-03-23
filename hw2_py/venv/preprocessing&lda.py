
# coding: utf-8

# In[ ]:

"""
Authors Jane Liu and Meng Li
Classes:
"""


# preprocessing:
import string
import logging
import unittest
import gensim
from gensim import corpora
from gensim.models.ldamodel import LdaModel
import pprint

import nltk
from nltk.stem import WordNetLemmatizer


class LDATokenizer:

    def __init__(self, text):
        self._text = text
        self._tokenized_doc = []

    def tokenize(self):
        for item in self._text:
            data = item.split()
            for i in data:
                i=i.lower()
                self._tokenized_doc.append(i)

        return self._tokenized_doc


class LDAPreprocessor:

    def __init__(self, article):
        self._article = article
        self._cleantext = []
        self._temptext = []

    def preprocess(self):

        # Tokenize the text file
        self._temptext = LDATokenizer(self._article)
        self._cleantext = self._temptext.tokenize()

        # Remove stop words
        for word in list(self._cleantext):
            if word in stopwords:
                self._cleantext.remove(word)

        # Remove punctuation and empty strings
        self._cleantext = [''.join(c for c in s if c not in string.punctuation) for s in self._cleantext]
        self._cleantext = [s for s in self._cleantext if s]

        # Lemmatize the text
        lemma_text = []
        lemmatizer = WordNetLemmatizer()

        for word in list(self._cleantext):
            new_word = lemmatizer.lemmatize(word)
            lemma_text.append(new_word)
        return lemma_text



# LDA function:

def lda(arc):
         
    dictionary = corpora.Dictionary(arc)
    corpus = [dictionary.doc2bow(text) for text in arc]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=1, id2word = dictionary, passes=20)
    a=ldamodel.print_topics(num_words=20)
    (num,topic)=a[0]
    
    return topic





