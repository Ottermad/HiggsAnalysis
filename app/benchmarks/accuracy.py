"""Benchmark clustering algorithms."""
from scipy.optimize import linear_sum_assignment
from .dbscan import dbscan_and_cluster_centres
from .meanshift import meanshift_and_cluster_centres
from .kmeans import kmeans_cluster_centres
from app.helper import get_coords_tuple, distance_calc
from app.db.models import (
    NonSimulatedImageClick,
    AccuracyBenchmarkScore
)

accuracy_data = [
    {
        "projection": "XY",
        "zoo_id": "AHH0000o3y",
        "manual_clusters": [
            (380, -480), (480, -540), (500, -430), (520, -380), (560, -400),
            (540, -530), (630, -530), (630, -480)
        ]
    },
    {
        "projection": "XYzoom",
        "zoo_id": "AHH0001ram",
        "manual_clusters": [
            (300, -410), (340, -590), (350, -710), (360, -880),
            (510, -520), (500, -310), (590, -490), (650, -480),
            (710, -510), (810, -610)
        ]
    },
    {
        "projection": "XY",
        "zoo_id": "AHH0000lr6",
        "manual_clusters": [
            (980, -420), (720, -590), (530, -650), (620, -610),
            (520, -510), (430, -500), (390, -410), (220, -600),
            (80, -320)
        ]
    },
    {
        "projection": "RZzoom",
        "zoo_id": "AHH0000myo",
        "manual_clusters": [
            (740, -420), (590, -580), (520, -550), (460, -590),
            (450, -540), (340, -510), (390, -590), (370, -630),
            (310, -600), (280, -590), (120, -660), (250, -650),
            (310, -600), (150, -450)
        ]
    },
]

epses = range(5, 50, 5)
bandwidths = range(10, 300, 5)


def accuracy_benchmark(run_id):
    """Benchmark Accuracy."""
    for image in accuracy_data:
        query = NonSimulatedImageClick.select().where(
            (NonSimulatedImageClick.zooniverse_id == image['zoo_id']) &
            (NonSimulatedImageClick.projection == image['projection'])
        )
        coords = get_coords_tuple(query)

        for eps in epses:
            dbscan_benchmark(run_id, image, coords, eps)

        for bandwidth in bandwidths:
            meanshift_benchmark(run_id, image, coords, bandwidth)

        kmeans_benchmark(run_id, image, coords)


def dbscan_benchmark(run_id, image, coords, eps):
    n_clusters, centres = dbscan_and_cluster_centres(eps, coords)
    mean_distance = centre_accuracy(
        centres, image['manual_clusters'])
    score = AccuracyBenchmarkScore(
        run_id=run_id,
        zooniverse_id=image['zoo_id'],
        projection=image['projection'],
        algorithm='DBSCAN',
        number_of_clusters=n_clusters,
        expected_number_of_clusters=len(image['manual_clusters']),
        mean_distances_from_clusters=mean_distance,
        parameters=eps
    )
    score.save()


def meanshift_benchmark(run_id, image, coords, bandwidth):
    n_clusters, centres = meanshift_and_cluster_centres(
        bandwidth, coords
    )
    mean_distance = centre_accuracy(
        centres.tolist(), image['manual_clusters']
    )
    score = AccuracyBenchmarkScore(
        run_id=run_id,
        zooniverse_id=image['zoo_id'],
        projection=image['projection'],
        algorithm='MeanShift',
        number_of_clusters=n_clusters,
        expected_number_of_clusters=len(image['manual_clusters']),
        mean_distances_from_clusters=mean_distance,
        parameters=bandwidth
    )
    score.save()


def kmeans_benchmark(run_id, image, coords):
    kmeans_centres = kmeans_cluster_centres(
        len(image['manual_clusters']), coords
    )
    mean_distance = centre_accuracy(
        kmeans_centres.tolist(), image['manual_clusters']
    )
    score = AccuracyBenchmarkScore(
        run_id=run_id,
        zooniverse_id=image['zoo_id'],
        projection=image['projection'],
        algorithm='KMeans',
        number_of_clusters=len(image['manual_clusters']),
        expected_number_of_clusters=len(image['manual_clusters']),
        mean_distances_from_clusters=mean_distance,
    )
    score.save()


def centre_accuracy(algorithm_centres, manual_centres):
    """Compare the accuracy of the cluster centres."""
    cost_matrix = []

    for coord_a in algorithm_centres:
        row = [distance_calc(coord_a, coord_b) for coord_b in manual_centres]
        cost_matrix.append(row)

    row_indexes, col_indexes = linear_sum_assignment(cost_matrix)

    total_distance = 0
    for i in range(0, len(row_indexes)):
        total_distance += cost_matrix[row_indexes[i]][col_indexes[i]]

    return total_distance / len(row_indexes)
