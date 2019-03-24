#!/usr/bin/env python3
"""
Authors Jane Liu and Meng Li

Classes:
    Tokenizer: Accepts a list of words and outputs tokenized text.
    RemoveStopWords: Accepts a list of tokens and removes stop words
    Preprocessors: Calls Tokenizer, RemoveStopWords, and lemmatizes the text. Applies NER to find proper nounds and
        replaces individual tokens with proper nounds. Determines 2-grams and 3-grams. Generates topics sorted
        by frequency and outputs results to the console and topics.txt.

"""

import string
import unittest
import re
import operator
from itertools import groupby
from collections import Counter

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
        self._tokenized_text = []

    def tokenize(self):
        # Remove punctuation and empty strings
        self._tokenized_text = [''.join(c for c in s if c not in string.punctuation) for s in self._text]
        self._tokenized_text = [s for s in self._tokenized_text if s]

        return self._tokenized_text

class RemoveStopWords:

    def __init__(self, text):
        self._text = text
        self._stopwords = []

    def removestopwords(self):
        with open('src/stopwords.txt', 'r') as g:
            self._stopwords = g.read().splitlines()
        for word in self._stopwords:
            self._text = [value for value in self._text if value != word]

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

        # Remove tokens and replace them with NER compound words
        for name in compound_ner:
            if name in preprocessed_str:
                preprocessed_str = preprocessed_str.replace(name, '')

        # Generate 2-grams and 3-grams
        prep_str = preprocessed_str.lower()
        prep_str = re.sub(r'[^a-zA-Z0-9\s]', ' ', prep_str)
        tokens = [token for token in prep_str.split(' ') if token != '']
        output2 = list(ngrams(tokens, 2))
        output3 = list(ngrams(tokens, 3))

        ngram_list = []

        for gram in output2:
            if output2.count(gram) > 3:
                temp2 = (gram, output2.count(gram))
                ngram_list.append(temp2)

        for gram in output3:
            if output3.count(gram) > 3:
                temp3 = (gram, output3.count(gram))
                ngram_list.append(temp3)

        # Remove duplicates of n-gram tuples
        ngram_list = list(set(ngram_list))

        # Remove tokens and replace with n-grams
        ngram_dict = dict(ngram_list)
        ngram_words = []
        for item in ngram_dict.keys():
            word = ' '.join(item)
            count = ngram_dict[item]
            if word in preprocessed_str:
                preprocessed_str = preprocessed_str.replace(word, '')
                preprocessed_str = preprocessed_str.replace(word.capitalize(), '')
            while count > 0:
                ngram_words.append(word)
                count -= 1
        preprocessed_list = preprocessed_str.split() + compound_ner + ngram_words

        # Find the most frequently occuring individual words
        word_freq = Counter(preprocessed_list)
        common_words = word_freq.most_common(10)

        # Combine the most frequently occuring words with most common n-grams
        topics = dict(common_words)

        return topics

class Topics:

    def __init__(self, topics):
        self._topics = topics
        self._results = {}

    def generatetopics(self):
        # Add the count of topics that appear in more than one document
        for key, value in self._topics.items():
            if key in self._results:
                self._results[key] = self._results[key] + value
            else:
                self._results[key] = value

        # Get the most frequent topics
        topic_num = 50
        self._results = dict(sorted(self._topics.items(), key=operator.itemgetter(1), reverse=True)[:topic_num])

        with open('topics.txt', 'w') as f:
            for item in self._results.keys():
                f.write(str(item))
                f.write(' ')
                f.write(str(self._results[item]))
                f.write('\n')
                print(item, self._results[item])

        print('\n')

        return self._results
