#!/usr/bin/env python3
"""
Authors Jane Liu and Meng Li

Classes:
    Tokenizer: Accepts a text file and outputs tokenized text.

"""

import string
import logging
import unittest

import spacy
from spacy import displacy
import en_core_web_sm

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class Tokenizer:

    def __init__(self, text):
        self._text = text
        self._tokenized_doc = []

    def tokenize(self):
        for item in self._text:
            data = item.split()
            for i in data:
                self._tokenized_doc.append(i)

        return self._tokenized_doc


class Preprocessor:

    def __init__(self, article):
        self._article = article
        self._cleantext = []
        self._temptext = []

    def preprocess(self):

        # Tokenize the text file
        self._temptext = Tokenizer(self._article)
        self._cleantext = self._temptext.tokenize()

        # Remove stop words
        for word in list(self._cleantext):
            if word in stopwords.words('english'):
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

        preprocessed_text = lemma_text

        # Perform named-entity extraction - need to combine the names
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(' '.join(preprocessed_text))  # spaCy requires text to be in string form

        # print out named entities
        ner_list = []

        for ent in doc.ents:
            ner_list.append(ent.text)

        for name in ner_list:
            for word in name:
                pass


        return None

'''
        # Sliding windows


        # Determine the frequency distribution of topics
        #frequency = nltk.FreqDist(preprocessed_text)

        #for key, val in frequency.items():
            print(str(key) + ':' + str(val))
'''