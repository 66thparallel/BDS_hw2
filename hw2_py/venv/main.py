#!/usr/bin/env python3

"""
Authors Jane Liu and Meng Li

Classes:

"""

import logging
import unittest


def main():

    # Read file and store in a list
    with open('src/C1/article01.txt', 'r') as f:
        article = f.read().splitlines()

    with open('src/stopwords.txt', 'r') as g:
        stopwords = g.read().splitlines()

    # Contains text without stop words
    cleantxt = []

    for item in article:
        data = item.split()
        for i in data:
            cleantxt.append(i)

    for word in list(cleantxt):
        if word in stopwords:
            cleantxt.remove(word)

    # Test if all stop words have been removed.
    for j in cleantxt:
        print(j)

main()

