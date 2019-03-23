import pandas as pd

class name:
    
    def __init__(self,obj,namespace):
        self._obj= obj
        self._namespace= namespace

        
    def namestr(self):  
        return [name for name in self._namespace if self._namespace[name] is self._obj] 
        
        
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
