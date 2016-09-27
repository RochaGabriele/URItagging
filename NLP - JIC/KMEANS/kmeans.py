from sklearn import cluster

def kmeans_sklearn(k, data):
    """data is a matrix of features"""
    kmeans = cluster.KMeans(n_clusters=k)
    kmeans.fit(data)
    
    return kmeans

