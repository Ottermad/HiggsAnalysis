"""MeanShift Clustering."""
from sklearn.cluster import MeanShift


def meanshift_and_cluster_centres(bandwidth, coords):
    """Get number of clusters."""
    clustering = MeanShift(bandwidth=bandwidth).fit(coords)
    centres = clustering.cluster_centers_
    return len(centres), centres
