#!/usr/bin/env python3
"""
Authors Jane Liu and Meng Li

Classes: DocTermMatrix

"""

import re
import string
import math


class DocTermMatrix:

    def __init__(self, topics):
        self._topics = topics
        self._top_count = []  # number times a topic appears in an article
        self._cols = 0  # number of columns in each row
        self._doc_matrix = []  # document term matrix with tf-idf
        self._total_terms = []  # number of words in each document
        self._num_of_articles = 0

    def generatematrix(self):

        with open('src/data.txt', 'r') as g:
            file_list = g.read().split()

            for filename in file_list:
                self._num_of_articles += 1

                # Create a row in the matrix containing the number of times a topic appears in the document
                with open(filename, 'r') as f:
                    article = f.read().split()
                    self._top_count.append(len(article))

                    for key in self._topics:
                        self._top_count.append(article.count(key))

                    self._doc_matrix.append(self._top_count)

                    self._top_count = []

        # Remove first element in each row--contains total number of words in each document
        for row in self._doc_matrix:
            self._total_terms.append(row[0])
            del row[0]
            self._cols = len(row)

        # Calculate the TF
        for i in range(self._cols):
            for j in range(len(self._doc_matrix)):
                tf = float(self._doc_matrix[j][i] / self._total_terms[j])
                self._doc_matrix[j][i] = tf

        # Counts the number of documents where each topic t appears
        num_docs_with_topic = []
        for i in range(self._cols):
            count = 0
            for j in range(len(self._doc_matrix)):
                if self._doc_matrix[j][i] > 0:
                    count += 1
            num_docs_with_topic.append(count)

        for i in range(self._cols):
            for j in range(len(self._doc_matrix)):
                if num_docs_with_topic[i] > 0:
                    idf = math.log(self._num_of_articles / num_docs_with_topic[i])
                    self._doc_matrix[j][i] *= idf

        print(self._doc_matrix)

        return(self._doc_matrix)