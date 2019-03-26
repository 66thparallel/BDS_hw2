from sklearn.metrics import classification_report, confusion_matrix
class evaluation:
    def __init__(self, matrix):
        self._matrix = matrix
    def eva(self):
        self._matrix["actual_cluster"]=[2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
        print(confusion_matrix(self._matrix["actual_cluster"],self._matrix['cluster']))
        print(classification_report(self._matrix["actual_cluster"],self._matrix['cluster']))
