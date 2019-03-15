#!/usr/bin/env python3
"""
Authors Jane Liu and Meng Li

Classes:
    Tokenizer: Accepts a text file and outputs tokenized text.

"""

class Tokenizer:

    def __init__(self, article):
        self.article = article
        self.tokenized_doc = []

    def tokenize(self):
        for item in self.article:
            data = item.split()
            for i in data:
                self.tokenized_doc.append(i)

        return self.tokenized_doc
