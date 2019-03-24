from sklearn.metrics import classification_report, confusion_matrix
class evaluation:
    def __init__(self, matrix):
        self._matrix = matrix
    def eva(self):
        matrix["actual_cluster"]=[2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
        print(confusion_matrix(matrix["actual_cluster"],matrix['cluster']))
        print(classification_report(matrix["actual_cluster"],matrix['cluster']))
