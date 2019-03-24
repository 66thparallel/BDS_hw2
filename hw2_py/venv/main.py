#!/usr/bin/python3
"""
Authors Jane Liu and Meng Li
Classes:
    Main: Calls relevant classes and class methods and outputs all results.

"""

import string
from preprocessor import *
from ngrams_docmatrix import *
from ldapreprocessor import *
from matrix import *
from visualization import *
from evaluation import *
from kmeans import *


def main():
    # preprocessing:
    Prep = Preprocessor()

    corpus_topics = Prep.preprocess()

    Corpus = Topics(corpus_topics)

    freq_topics = Corpus.generatetopics()

    Docmatrix = DocTermMatrix(freq_topics)

    doc_matrix = Docmatrix.generatematrix()

    # LDA:

    textlist = []
    with open('src/data.txt', 'r') as g:
        file_list = g.read().split()

        for filename in file_list:
            with open(filename, 'r') as f:
                larticle = f.read().split()

            LPrep = LDAPreprocessor(larticle)

            Ltexts = LPrep.LDApreprocess()

            textlist.append(Ltexts)

    Ltopics = LDA(textlist)

    ltopics = Ltopics.get_lda()

    ldatopic = LDAtopics(ltopics)

    ldatopic.Ltopics()

    # Comparing the LDA and NER/n-grams prerpocessing results we get the final list of topics:
    ftopics = ['bank', 'rate', 'mortgage', 'loan', 'civil aeronautics', 'airline', 'disease', 'takenaka', 'safety',
               'minister', 'suspect', 'mouth', 'yen', 'company', 'pilot', 'corporation', 'hoof', 'year', 'civil',
               'policy']

    # generate document matrix
    m = Matrix(ftopics)
    fmatrix = m.matrix()
    # tf-idf
    t = TF(ftopics)
    dic_topic, tfmatrix = t.TFmatrix()
    i = IDF(ftopics)
    dic_topic2 = i.idf()
    # generate tf-idf matrix
    for elem in dic_topic:
        for topic in dic_topic.get(elem):
            dic_topic[elem][topic] = dic_topic.get(elem).get(topic) * dic_topic2[topic]
    matrix2 = pd.DataFrame.from_dict(dic_topic, orient='index')
    # kmeans
    km = kmeans(3, matrix2)
    kmeansr = km.k_means()
    # visualization
    gra = visiualization(kmeansr)
    gra.visual()
    # evaluation
    ev = evaluation(kmeansr)
    ev.eva()
    return kmeansr


main()