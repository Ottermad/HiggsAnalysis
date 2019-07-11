"""Run DBSCAN."""
import numpy as np
from sklearn.cluster import DBSCAN


def find_cluster_centres(cluster, coords):
    """Find cluster centres for DBSCAN clustering."""
    # #  Cluster numbering starts at 0 so add 1
    number_of_clusters = np.amax(cluster.labels_) + 1

    # For each cluster create an empty array to store points
    clusters = [[] for x in range(0, number_of_clusters)]
    for x in range(0, len(cluster.labels_)):
        point = cluster.labels_[x]
        clusters[point].append(coords[x])

    centres = []
    for cluster in clusters:
        x = sum([r[0] for r in cluster]) / len(cluster)
        y = sum([r[1] for r in cluster]) / len(cluster)
        centres.append((x, y))
    return centres


def dbscan_and_cluster_centres(eps, coords, min_samples=2):
    """Use DBSCAN to form clusters."""
    clustering = DBSCAN(eps=eps, min_samples=min_samples).fit(coords)
    labels = clustering.labels_

    # Number of clusters in labels, ignoring noise if present.
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    centres = find_cluster_centres(clustering, coords)
    return n_clusters, centres


def dbscan_clusters(eps, coords):
    """Use DBSCAN to form clusters."""
    clustering = DBSCAN(eps=eps, min_samples=2).fit(coords)
    labels = clustering.labels_

    # Number of clusters in labels, ignoring noise if present.
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    return n_clusters
