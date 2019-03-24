from sklearn.cluster import KMeans
class kmeans:
    def __init__(self,num_clusters,matrix):
        self._matrix = matrix
        self._num_clusters=num_clusters
 
    def k_means(self):
        km = KMeans(n_clusters=self._num_clusters,
                max_iter=10000,random_state=3425)
        km.fit(self._matrix)
        clusters = km.labels_
        self._matrix['cluster']=clusters
        return self._matrix
   

