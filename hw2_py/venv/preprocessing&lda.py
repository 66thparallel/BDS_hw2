
# coding: utf-8

# In[ ]:

"""
Authors Jane Liu and Meng Li
Classes:
"""


# article list:

arc11='/Users/limeng/Downloads/dataset_3/data/C1/article01.txt'
arc12='/Users/limeng/Downloads/dataset_3/data/C1/article02.txt'
arc13='/Users/limeng/Downloads/dataset_3/data/C1/article03.txt'
arc14='/Users/limeng/Downloads/dataset_3/data/C1/article04.txt'
arc15='/Users/limeng/Downloads/dataset_3/data/C1/article05.txt'
arc16='/Users/limeng/Downloads/dataset_3/data/C1/article06.txt'
arc17='/Users/limeng/Downloads/dataset_3/data/C1/article07.txt'
arc18='/Users/limeng/Downloads/dataset_3/data/C1/article08.txt'
arc21='/Users/limeng/Downloads/dataset_3/data/C4/article01.txt'
arc22='/Users/limeng/Downloads/dataset_3/data/C4/article02.txt'
arc23='/Users/limeng/Downloads/dataset_3/data/C4/article03.txt'
arc24='/Users/limeng/Downloads/dataset_3/data/C4/article04.txt'
arc25='/Users/limeng/Downloads/dataset_3/data/C4/article05.txt'
arc26='/Users/limeng/Downloads/dataset_3/data/C4/article06.txt'
arc27='/Users/limeng/Downloads/dataset_3/data/C4/article07.txt'
arc28='/Users/limeng/Downloads/dataset_3/data/C4/article08.txt'
arc31='/Users/limeng/Downloads/dataset_3/data/C7/article01.txt'
arc32='/Users/limeng/Downloads/dataset_3/data/C7/article02.txt'
arc33='/Users/limeng/Downloads/dataset_3/data/C7/article03.txt'
arc34='/Users/limeng/Downloads/dataset_3/data/C7/article04.txt'
arc35='/Users/limeng/Downloads/dataset_3/data/C7/article05.txt'
arc36='/Users/limeng/Downloads/dataset_3/data/C7/article06.txt'
arc37='/Users/limeng/Downloads/dataset_3/data/C7/article07.txt'
arc38='/Users/limeng/Downloads/dataset_3/data/C7/article08.txt'
arclist=[arc11,arc12,arc13,arc14,arc15,arc16,arc17,arc18,arc21,arc22,arc23,arc24,arc25,arc26,arc27,arc28,arc31,arc32,arc33,
         arc34,arc35,arc36,arc37,arc38]


# preprocessing:

def preprocessing(txt_name):
    import string
    import logging
    import unittest
    import nltk
    from nltk.stem import WordNetLemmatizer


    # Read stopwords
    with open('/Users/limeng/Downloads/stop_words.txt', 'r') as g:
        stopwords = g.read().splitlines()
    
    # Read file and store in a list
    texts=[]
    with open(txt_name, 'r') as f:
        sentence = f.readlines()
        # clean and tokenize document string
        for s in sentence:
            raw = s.lower()
            raw = raw.replace('\n',' ')
            tokens = raw.split()

            # remove stop words from tokens
            stopped_tokens = [i for i in tokens if not i in stopwords]
    
            # stem tokens
            stemmed_tokens = [WordNetLemmatizer().lemmatize(i) for i in stopped_tokens]
    
            # add tokens to list
            texts.append(stemmed_tokens)

    return (texts)



# NER(not work well):

'''def ner(arc):
    with open('/Users/limeng/Downloads/stop_words.txt', 'r') as g:
        stopwords = g.read().splitlines()
    
        
    with open(arc, 'r') as f:
        sentence = f.readlines()
        # clean and tokenize document string
        for s in sentence:
            raw = s.replace('\n',' ')
            tokens = raw.split()

            # remove stop words from tokens
            stopped_tokens = [i for i in tokens if not i in stopwords]
    
            # stem tokens
            stemmed_tokens = [WordNetLemmatizer().lemmatize(i) for i in stopped_tokens]
    
            # add tokens to list
            texts.append(stemmed_tokens)
    en={}
    import pprint
    for sentences in texts:
        for sentence in sentences:
            tokenized = nltk.word_tokenize(sentence)
            tagged = nltk.pos_tag(tokenized)
            chunked = nltk.ne_chunk(tagged)
            for tree in chunked:
                if hasattr(tree, 'label'):
                    ne = ' '.join(c[0] for c in tree.leaves())
                    en[ne] = [tree.label(), ' '.join(c[1] for c in tree.leaves())]
    pp = pprint.PrettyPrinter(indent=4)
    return (pp.pprint(en))'''


# LDA function:

def lda(arc):
    from gensim import corpora
    from gensim.models.ldamodel import LdaModel
    import pprint

    dictionary = corpora.Dictionary(arc)
    corpus = [dictionary.doc2bow(text) for text in arc]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=1, id2word = dictionary, passes=20)
    pp = pprint.PrettyPrinter()
    a=pp.pprint(ldamodel.print_topics(num_words=10)
    return a





