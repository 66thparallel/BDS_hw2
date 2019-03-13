#!/usr/bin/python3.7

"""
Authors Jane Liu and Meng Li

Classes:

"""
import string
import logging
import unittest
import nltk
from nltk.stem import WordNetLemmatizer

def main():

    # Read file and store in a list
    with open('src/C1/article01.txt', 'r') as f:
        article = f.read().splitlines()

    with open('src/stopwords.txt', 'r') as g:
        stopwords = g.read().splitlines()

    # Contains text without stop words
    cleantext = []

    # Tokenize the text
    for item in article:
        data = item.split()
        for i in data:
            cleantext.append(i)

    # Remove stop words
    for word in list(cleantext):
        if word in stopwords:
            cleantext.remove(word)

    # Remove punctuation and empty strings
    cleantext = [''.join(c for c in s if c not in string.punctuation) for s in cleantext]
    cleantext = [s for s in cleantext if s]

    # Lemmatize the text (stemming gave weird results)
    lemma_text = []
    lemma = WordNetLemmatizer()

    for word in list(cleantext):
        new_word = lemma.lemmatize(word)
        lemma_text.append(new_word)

    # print(lemma_text)

main()

