from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import pylab as pl
class visiualization:
    def __init__(self,matrix):
        self._matrix = matrix
    
    def visual(self):
        pca = PCA(n_components=2).fit(self._matrix.iloc[:,:-1])
        pca_2d = pca.transform(self._matrix.iloc[:,:-1])

        for i in range(0, pca_2d.shape[0]):
            if self._matrix["cluster"][i] == 0:
                c1 = pl.scatter(pca_2d[i,0],pca_2d[i,1],c='r',marker='+')
            elif self._matrix["cluster"][i] == 1:
                c2 = pl.scatter(pca_2d[i,0],pca_2d[i,1],c='g',marker='o')
            elif self._matrix["cluster"][i] == 2: 
                c3 = pl.scatter(pca_2d[i,0],pca_2d[i,1],c='b',marker='*')
        pl.legend([c1, c2, c3], ['disease', 'bank','airline'])
        pl.title('matrix with 3 clusters and known outcomes')
        return pl.show()
