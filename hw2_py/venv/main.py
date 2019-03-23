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
from ldapreprocessor import *


def main():
    #preprocessing:
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
    
    #LDA:
    
    textlist=[]
    with open('src/data.txt', 'r') as g:
        file_list = g.read().split()

        for filename in file_list:

            with open(filename, 'r') as f:
                larticle = f.read().split()

            LPrep = LDAPreprocessor(larticle)

            Ltexts = LPrep.LDApreprocess()
            
            textlist.append(Ltexts)
            
    Ltopics=LDA(textlist)
    
    ltopics=Ltopics.lda()
    
    ldatopic=LDAtopics(ltopics)
    
    ldatopic.Ltopics()
    
    #After comparing the LDA result and Preprocessing result, we finally get the list of topics:
    ftopics=['bank', 'rate', 'mortgage', 'loan', 'civil aeronautics', 'airline', 'disease', 'takenaka', 'safety', 'minister', 'suspect', 'mouth', 'yen', 'company', 'pilot', 'corporation', 'hoof', 'year', 'civil', 'policy']
    #Generate document matrix
    m=Matrix(ftopics)
    fmatrix=m.matrix()
    #tf-idf
    t=TF(ftopics)
    dic_topic,tfmatrix=t.TFmatrix()
    i=IDF(ftopics)
    dic_topic2=i.idf()
    #generate tf-idf matrix
    for elem in dic_topic:
        for topic in dic_topic.get(elem):
            dic_topic[elem][topic]=dic_topic.get(elem).get(topic)*dic_topic2[topic]
    matrix2=pd.DataFrame.from_dict(dic_topic, orient='index')
            
    return matrix2


main()

