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

    def generatematrix(self):

        top_count = []  # number times a topic appears in an article
        cols = 0  # number of columns in each row
        doc_matrix = []  # document term matrix with tf-idf
        total_terms = []  # number of words in each document
        num_of_articles = 0

        with open('src/data.txt', 'r') as g:
            file_list = g.read().split()

            for filename in file_list:
                num_of_articles += 1

                # Create a row in the matrix containing the number of times a topic appears in the document
                with open(filename, 'r') as f:
                    article = f.read().split()
                    top_count.append(len(article))

                    for key in self._topics:
                        top_count.append(article.count(key))

                    doc_matrix.append(top_count)

                    top_count = []

        # Remove first element in each row--contains total number of words in each document
        for row in doc_matrix:
            total_terms.append(row[0])
            del row[0]
            cols = len(row)

        # Calculate the TF
        for i in range(cols):
            for j in range(len(doc_matrix)):
                tf = float(doc_matrix[j][i] / total_terms[j])
                doc_matrix[j][i] = tf

        # Counts the number of documents where each topic t appears
        num_docs_with_topic = []
        for i in range(cols):
            count = 0
            for j in range(len(doc_matrix)):
                if doc_matrix[j][i] > 0:
                    count += 1
            num_docs_with_topic.append(count)

        for i in range(cols):
            for j in range(len(doc_matrix)):
                if num_docs_with_topic[j] > 0:
                    idf = math.log(num_of_articles / num_docs_with_topic[j])
                    doc_matrix[j][i] *= idf

        print(doc_matrix)

        return(doc_matrix)