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
from docmatrix import *


def main():

    corpus_topics = {}

    with open('src/data.txt', 'r') as g:
        file_list = g.read().split()

        for filename in file_list:

            with open(filename, 'r') as f:
                article = f.read().split()

            Prep = Preprocessor(article)

            topics = Prep.preprocess()

            corpus_topics.update(topics)

    Corpus = Topics(corpus_topics)

    Corpus.generatetopics()

    Docmatrix = DocTermMatrix(corpus_topics)

    doc_matrix = Docmatrix.generatematrix()


    return None


main()