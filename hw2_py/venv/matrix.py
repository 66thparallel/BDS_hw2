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
            
            #need change
            with open(arc, 'r') as f:
                article = f.read().splitlines()
            LPrep = LDAPreprocessor(article)
            Ltexts = LPrep.LDApreprocess()
            for word in self._ftopics:
                a=0
                inner_key=word
                for w in Ltexts:
                    if w == word:
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

        matrix=pd.DataFrame.from_dict(dic_topic, orient='index')
        return dic_topic,matrix
    
class IDF:
    def __init__(self,ftopics):
        self._ftopics = ftopics
    def idf(self):
        import math
        dic_topic2={}
        for word in self._ftopics:  
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
        return dic_topic2
