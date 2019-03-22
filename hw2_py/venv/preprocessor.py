#!/usr/bin/env python3
"""
Authors Jane Liu and Meng Li

Classes:
    Tokenizer: Accepts a text file and outputs tokenized text.

"""

import string
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

class RemoveStopWords:

    def __init__(self, text):
        self._text = text
        self._stopwords = []

    def removestopwords(self):
        with open('src/stopwords.txt', 'r') as g:
            self._stopwords = g.read().splitlines()
        for word in self._stopwords:
            self._text = [value for value in self._text if value != word]
            self._text = [value for value in self._text if value != word.capitalize()]

        return self._text


class Preprocessor:

    def __init__(self, article):
        self._article = article
        self._cleantext = []
        self._temptext = []

    def preprocess(self):

        # tokenize the text file
        self._temptext = Tokenizer(self._article)
        self._cleantext = self._temptext.tokenize()

        # remove punctuation and empty strings
        self._cleantext = [''.join(c for c in s if c not in string.punctuation) for s in self._cleantext]
        self._cleantext = [s for s in self._cleantext if s]

        # remove stop words
        self._temptext = RemoveStopWords(self._cleantext)
        self._cleantext = self._temptext.removestopwords()

        # lemmatize the text
        lemma_text = []
        lemmatizer = WordNetLemmatizer()

        for word in list(self._cleantext):
            new_word = lemmatizer.lemmatize(word)
            lemma_text.append(new_word)

        preprocessed_text = lemma_text

        # apply NER to determine proper nouns, like "Microsoft Corporation"
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(' '.join(preprocessed_text))  # spaCy requires entire text to be in string form

        preprocessed_str = ""

        for token in doc:
            temp = str(token.text) + ' '
            preprocessed_str += temp

        # find all NER names and put into a list
        ner_list = []

        for ent in doc.ents:
            ner_list.append(str(ent.text))

        # find all compound NER names and put into a list
        compound_ner = []

        for item in ner_list:
            temp = item.split()
            if len(temp) > 1:
                compound_ner.append(item)

        # remove NER compound words from preprocessed_str
        for name in compound_ner:
            if name in preprocessed_str:
                preprocessed_str = preprocessed_str.replace(name, '')

        preprocessed_list = preprocessed_str.split()

        preprocessed_list += compound_ner

        print(preprocessed_list)

        return None



'''
        # Sliding windows


        # Determine the frequency distribution of topics
        #frequency = nltk.FreqDist(preprocessed_text)

        #for key, val in frequency.items():
            print(str(key) + ':' + str(val))
'''