"""Speed Benchmark."""
import time
import uuid
from .dbscan import dbscan_and_cluster_centres, dbscan_clusters
from .meanshift import meanshift_and_cluster_centres
from .kmeans import kmeans_cluster_centres
from functools import partial
from app.helper import get_coords_tuple
from app.db.models import (
    NonSimulatedImageClick,
    SpeedBenchmarkScore
)

image_sets = [
    {"label": "XL", "images": [("AHH0000lmp", "RZzoom")]},
    {"label": "L", "images": [("AHH0000pr0", "XY"), ("AHH0001ey6", "XYzoom")]},
    {"label": "M", "images": [("AHH00016le", "XYzoom"), ("AHH0001bh4", "XYzoom")]},
    {"label": "S", "images": [("AHH0000lr6", "XY"), ("AHH0000myo", "RZzoom")]},
]

algorithms = [
    {
        "name": "DBSCAN",
        "func": partial(dbscan_clusters, 20)
    },
    {
        "name": "DBSCAN + Cluster Centres",
        "func": partial(dbscan_and_cluster_centres, 20)
    },
    {
        "name": "MeanShift",
        "func": partial(meanshift_and_cluster_centres, 30)
    },
    {
        "name": "KMeans",
        "func": partial(kmeans_cluster_centres, 10)
    }
]


def speed_benchmark(run_id):
    """Speed Benchmark."""
    for image_set in image_sets:
        # Get coords
        total_coords = []
        for zooniverse_id, projection in image_set['images']:
            query = NonSimulatedImageClick.select().where(
                (NonSimulatedImageClick.zooniverse_id == zooniverse_id) &
                (NonSimulatedImageClick.projection == projection)
            )
            total_coords += get_coords_tuple(query)
        for algorithm in algorithms:
            start = time.time()
            for x in range(1, 100):
                algorithm['func'](total_coords)
            end = time.time()
            time_taken = (end - start) / 100
            s = SpeedBenchmarkScore(
                run_id=run_id,
                algorithm=algorithm['name'],
                size=image_set['label'],
                mean_time_taken=time_taken
            )
            s.save()
    print("Done with Run Id: {}".format(run_id))
