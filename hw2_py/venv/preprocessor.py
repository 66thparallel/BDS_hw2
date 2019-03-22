#!/usr/bin/env python3
"""
Authors Jane Liu and Meng Li

Classes:
    Tokenizer: Accepts a text file and outputs tokenized text.

"""

import string
import unittest
import re
from itertools import groupby

import spacy
from spacy import displacy
import en_core_web_sm

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams


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

        # Tokenize the text file
        self._temptext = Tokenizer(self._article)
        self._cleantext = self._temptext.tokenize()

        # Remove punctuation and empty strings
        self._cleantext = [''.join(c for c in s if c not in string.punctuation) for s in self._cleantext]
        self._cleantext = [s for s in self._cleantext if s]

        # Remove stop words
        self._temptext = RemoveStopWords(self._cleantext)
        self._cleantext = self._temptext.removestopwords()

        # Lemmatize the text
        lemma_text = []
        lemmatizer = WordNetLemmatizer()

        for word in list(self._cleantext):
            new_word = lemmatizer.lemmatize(word)
            lemma_text.append(new_word)

        preprocessed_text = lemma_text

        # Apply NER to determine proper nouns, like "Microsoft Corporation"
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(' '.join(preprocessed_text))  # spaCy requires input text to be in string form

        preprocessed_str = ""

        for token in doc:
            temp = str(token.text) + ' '
            preprocessed_str += temp

        # Find all NER names and put into a list
        ner_list = []

        for ent in doc.ents:
            ner_list.append(str(ent.text))

        # Find all compound NER names and put into a list
        compound_ner = []

        for item in ner_list:
            temp = item.split()
            if len(temp) > 1:
                compound_ner.append(item)

        # Remove NER compound words from preprocessed_str and add back into preprocessed_list
        for name in compound_ner:
            if name in preprocessed_str:
                preprocessed_str = preprocessed_str.replace(name, '')

        preprocessed_str += ' '.join(compound_ner)

        # Generate 2-grams and 3-grams and output to the console a list of the n-grams that occur two or more times
        # in the document. Shows n-grams and their frequency counts.
        preprocessed_str = preprocessed_str.lower()
        preprocessed_str = re.sub(r'[^a-zA-Z0-9\s]', ' ', preprocessed_str)
        tokens = [token for token in preprocessed_str.split(' ') if token != '']
        output2 = list(ngrams(tokens, 2))
        output3 = list(ngrams(tokens, 3))

        ngram_list = []

        for gram in output2:
            if output2.count(gram) > 1:
                temp2 = (gram, output2.count(gram))
                ngram_list.append(temp2)


        for gram in output3:
            if output3.count(gram) > 1:
                temp3 = (gram, output3.count(gram))
                ngram_list.append(temp3)

        ngram_list = list(set(ngram_list))

        print(ngram_list)


        return None
