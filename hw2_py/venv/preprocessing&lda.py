
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

    def LDAtokenize(self):
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

    def LDApreprocess(self):

        # Tokenize the text file
        self._temptext = LDATokenizer(self._article)
        self._cleantext = self._temptext.LDAtokenize()

        # Remove stop words
        with open('src/stopwords.txt', 'r') as g:
            stopwords = g.read().splitlines()   
           
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



    # LDA function:
    
    def LDA(arc):

        dictionary = corpora.Dictionary(arc)
        
        corpus = [dictionary.doc2bow(text) for text in arc]
        
        ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=1, id2word = dictionary, passes=20)
        
        a=ldamodel.print_topics(num_words=20)
        
        (num,topic)=a[0]
    
    return topic

class LDAtopics:
    
    def LDAtopic():
    with open('Ltopics.txt', 'w') as f:
            for item in self._results.keys():
                f.write(str(item))
                f.write(' ')
                f.write(str(self._results[item]))
                f.write('\n')
                print(item, self._results[item])


