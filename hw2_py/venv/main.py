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
from preprocessor import *


def main():

    with open('src/C1/article01.txt', 'r') as f:
        article = f.read().splitlines()

    Prep = Preprocessor(article)

    topics = Prep.preprocess()

    print(topics)


main()

