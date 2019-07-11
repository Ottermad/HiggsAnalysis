"""K Means Clustering."""
from sklearn.cluster import KMeans


def kmeans_cluster_centres(number_of_clusters, coords):
    """Get number of clusters."""
    clustering = KMeans(n_clusters=number_of_clusters).fit(coords)
    centres = clustering.cluster_centers_
    return centres
