arc11='src/C1/article01.txt'
arc12='src/C1/article02.txt'
arc13='src/C1/article03.txt'
arc14='src/C1/article04.txt'
arc15='src/C1/article05.txt'
arc16='src/C1/article06.txt'
arc17='src/C1/article07.txt'
arc18='src/C1/article08.txt'
arc21='src/C4/article01.txt'
arc22='src/C4/article02.txt'
arc23='src/C4/article03.txt'
arc24='src/C4/article04.txt'
arc25='src/C4/article05.txt'
arc26='src/C4/article06.txt'
arc27='src/C4/article07.txt'
arc28='src/C4/article08.txt'
arc31='src/C7/article01.txt'
arc32='src/C7/article02.txt'
arc33='src/C7/article03.txt'
arc34='src/C7/article04.txt'
arc35='src/C7/article05.txt'
arc36='src/C7/article06.txt'
arc37='src/C7/article07.txt'
arc38='src/C7/article08.txt'
arclist=[arc11,arc12,arc13,arc14,arc15,arc16,arc17,arc18,arc21,arc22,arc23,arc24,arc25,arc26,arc27,arc28,arc31,arc32,arc33,
         arc34,arc35,arc36,arc37,arc38]
import pandas as pd

class name:
    
    def __init__(self,obj,namespace):
        self._obj= obj
        self._namespace= namespace

        
    def namestr(self):  
        return [name for name in self._namespace if self._namespace[name] is self._obj] 
        
#term matrix        
class Matrix:
    def __init__(self,ftopics):
        self._ftopics = ftopics
        
    def matrix(self):
        dic_topic={}
        #need change
        for arc in arclist:
            louter_key=name(arc,globals())
            outer_key=louter_key.namestr()[0]
            
            
            with open(arc, 'r') as f:
                article = f.read().splitlines()
            LPrep = LDAPreprocessor(article)
            Ltexts = LPrep.LDApreprocess()
            for word in self._ftopics:
                if len(word)<16:
                    a=0
                    inner_key=word
                    for w in Ltexts:
                        if w == word:
                            a=a+1
                    dic_topic[outer_key]=dic_topic.get(outer_key,{})
                    dic_topic[outer_key][inner_key] = dic_topic[outer_key].get(inner_key,0)
                    dic_topic[outer_key][inner_key]=a
                else:
                    a=0
                    inner_key=word
                    wlist=word.split()
                    for w in range(len(Ltexts)):
                        if Ltexts[w]==wlist[0] and Ltexts[w+1]==wlist[1]:
                            a=a+1
                        
                    dic_topic[outer_key]=dic_topic.get(outer_key,{})
                    dic_topic[outer_key][inner_key] = dic_topic[outer_key].get(inner_key,0)
                    dic_topic[outer_key][inner_key]=a

        matrix=pd.DataFrame.from_dict(dic_topic, orient='index')
        return matrix
    
    
class name:
    
    def __init__(self,obj,namespace):
        self._obj= obj
        self._namespace= namespace

        
    def namestr(self):  
        return [name for name in self._namespace if self._namespace[name] is self._obj] 
        
#generate TF-IDF:        
class TF:
    def __init__(self,ftopics):
        self._ftopics = ftopics
        
    def TFmatrix(self):
        dic_topic={}
        for arc in arclist:
            louter_key=name(arc,globals())
            outer_key=louter_key.namestr()[0]

            with open(arc, 'r') as f:
                article = f.read().splitlines()
            LPrep = LDAPreprocessor(article)
            Ltexts = LPrep.LDApreprocess()
            for word in self._ftopics:
                if len(word)<16:
                    tf=0
                    a=0
                    inner_key=word
                    for w in Ltexts:
                        if w == word:
                            a=a+1                     
                            tf=a/len(Ltexts)     
                    dic_topic[outer_key]=dic_topic.get(outer_key,{})
                    dic_topic[outer_key][inner_key] = dic_topic[outer_key].get(inner_key,0)
                    dic_topic[outer_key][inner_key]=tf
                
                else:
                    a=0
                    tf=0
                    inner_key=word
                    wlist=word.split()
                    for w in range(len(Ltexts)):
                        if Ltexts[w]==wlist[0] and Ltexts[w+1]==wlist[1]:
                            a=a+1 
                            tf=a/len(Ltexts)
                    dic_topic[outer_key]=dic_topic.get(outer_key,{})
                    dic_topic[outer_key][inner_key] = dic_topic[outer_key].get(inner_key,0)
                    dic_topic[outer_key][inner_key]=tf

        matrix=pd.DataFrame.from_dict(dic_topic, orient='index')
        return dic_topic,matrix
    
class IDF:
    def __init__(self,ftopics):
        self._ftopics = ftopics
    def idf(self):
        import math
        dic_topic2={}
        for word in self._ftopics:  
            if len(word)<16:
                b=0
                idf=0
                for arc in arclist:
                    with open(arc, 'r') as f:
                        article = f.read().splitlines()
                    LPrep = LDAPreprocessor(article)
                    Ltexts = LPrep.LDApreprocess()
                    if word in Ltexts:
                        b=b+1
                idf=math.log10(float(len(arclist))/b)  
                dic_topic2[word]=idf
            else:
                b=1
                idf=0
                idf=math.log10(float(len(arclist))/b)  
                dic_topic2[word]=idf
        return dic_topic2
