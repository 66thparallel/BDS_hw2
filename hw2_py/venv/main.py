#!/usr/bin/python3

"""
Authors Jane Liu and Meng Li

Classes:
    main: Loops over every command in input file and calls relevant functions

"""
import string
import logging
import unittest
import nltk
from nltk.stem import WordNetLemmatizer
from hw2_classes import *


def main():

    # Read file and store in a list
    with open('src/C1/article01.txt', 'r') as f:
        article = f.read().splitlines()

    with open('src/stopwords.txt', 'r') as g:
        stopwords = g.read().splitlines()

    # Tokenize the text file
    temptext = Tokenizer(article)
    cleantext = temptext.tokenize()

    # Remove stop words
    for word in list(cleantext):
        if word in stopwords:
            cleantext.remove(word)

    # Remove punctuation and empty strings
    cleantext = [''.join(c for c in s if c not in string.punctuation) for s in cleantext]
    cleantext = [s for s in cleantext if s]

    # Lemmatize the text (stemming gave weird results)
    lemma_text = []
    lemmatizer = WordNetLemmatizer()

    for word in list(cleantext):
        new_word = lemmatizer.lemmatize(word)
        lemma_text.append(new_word)

    # Check to see if text has been lemmatized
    print(lemma_text)

    # NER

    # Sliding windows



main()

