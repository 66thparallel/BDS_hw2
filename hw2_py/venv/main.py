#!/usr/bin/env python3

"""
Authors Jane Liu and Meng Li

Classes:

"""

import string
import logging
import unittest


def main():

    # Read file and store in a list
    with open('src/C1/article01.txt', 'r') as f:
        article = f.read().splitlines()

    with open('src/stopwords.txt', 'r') as g:
        stopwords = g.read().splitlines()

    # Contains text without stop words
    cleantext = []

    for item in article:
        data = item.split()
        for i in data:
            cleantext.append(i)

    for word in list(cleantext):
        if word in stopwords:
            cleantext.remove(word)

    # Remove punctuation from words and remove empty strings
    cleantext = [''.join(c for c in s if c not in string.punctuation) for s in cleantext]
    cleantext = [s for s in cleantext if s]

    # Test if all stop words have been removed.
    print(cleantext)

main()

