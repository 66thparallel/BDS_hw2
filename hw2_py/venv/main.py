#!/usr/bin/python3
"""
Authors Jane Liu and Meng Li

Classes:
    main: Loops over every command in input file and calls relevant functions

Notes (delete before submitting!!):
    Set up Preprocessor class. The Preprocessors.preprocess() function needs to remove stop words, tokenize,
    lemmatize, perform NER, and sliding window. Separate LDA class.

"""

import string
import logging
import unittest
from collections import Counter

import spacy
from spacy import displacy
import en_core_web_sm

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Preprocessing textual data
from preprocessor import *


def main():

    with open('src/C1/article01.txt', 'r') as f:
        article = f.read().splitlines()

    # Tokenize the text file
    temptext = Tokenizer(article)
    cleantext = temptext.tokenize()

    # Remove stop words
    for word in list(cleantext):
        if word in stopwords.words('english'):
            cleantext.remove(word)

    # Remove punctuation and empty strings
    cleantext = [''.join(c for c in s if c not in string.punctuation) for s in cleantext]
    cleantext = [s for s in cleantext if s]

    # Lemmatize the text
    lemma_text = []
    lemmatizer = WordNetLemmatizer()

    for word in list(cleantext):
        new_word = lemmatizer.lemmatize(word)
        lemma_text.append(new_word)

    preprocessed_text = lemma_text

    # Perform named-entity extraction
    #nlp = en_core_web_sm.load()
    #doc = nlp(' '.join(preprocessed_text))  # spaCy requires text to be in string form
    #print([(X.text, X.label_) for X in doc.ents])

    # Sliding windows


    # Determine the frequency distribution of topics
    frequency = nltk.FreqDist(preprocessed_text)

    for key, val in frequency.items():
        print(str(key) + ':' + str(val))


main()

