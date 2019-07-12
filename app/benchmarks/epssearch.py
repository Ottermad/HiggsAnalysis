"""Comparing and searching for optimium EPS value."""
import matplotlib.pyplot as plt
from app.db.models import NonSimulatedImageClick
from app.helper import get_coords_tuple
from .accuracy import centre_accuracy
from .dbscan import dbscan_and_cluster_centres

colors = ['ro', 'bo', 'co', 'mo', 'yo', 'wo']


def plot_mean_distance_from_centres(images, filename, epses):
    """Plot a graph of accuracy against EPS."""

    fig, ax = plt.subplots()

    for color, image in zip(colors, images):

        query = NonSimulatedImageClick.select().where(
            (NonSimulatedImageClick.zooniverse_id == image['zoo_id']) &
            (NonSimulatedImageClick.projection == image['projection'])
        )
        coords = get_coords_tuple(query)

        accuracies = []
        for eps in epses:
            a, n = find_accuracy(eps, coords, image['manual_clusters'])
            accuracies.append(a)

        ax.plot(
            epses,
            accuracies,
            color,
            label="{}_{}".format(image['zoo_id'], image['projection'])
        )

    ax.set_xlabel("EPS Values")
    ax.set_ylabel(
        "Mean Distance from Centres")

    ax.legend(loc='lower right', fontsize=10, bbox_to_anchor=(0.3, 0.8))
    fig.savefig(filename, dpi=400)


def plot_absolute_difference(images, filename, epses):
    """Plot Number of Clusters against EPS."""
    fig, ax = plt.subplots()

    for color, image in zip(colors, images):

        query = NonSimulatedImageClick.select().where(
            (NonSimulatedImageClick.zooniverse_id == image['zoo_id']) &
            (NonSimulatedImageClick.projection == image['projection'])
        )
        coords = get_coords_tuple(query)

        cluster_diffs = []
        for eps in epses:
            a, n = find_accuracy(eps, coords, image['manual_clusters'])
            diff = abs(len(image['manual_clusters']) - len(n))
            cluster_diffs.append(diff)

        ax.plot(
            epses,
            cluster_diffs,
            color,
            label="{}_{}".format(image['zoo_id'], image['projection'])
        )

    ax.set_xlabel("EPS Values")
    ax.set_ylabel(
        "Absolute Difference between Number of Clusters expected and produced")
    ax.legend(loc='lower right', fontsize=10, bbox_to_anchor=(0.3, 0.8))
    fig.savefig(filename, dpi=400)


def find_accuracy(eps, coords, manual_clusters):
    """Find the accuracy for an eps value."""
    n, centres = dbscan_and_cluster_centres(eps, coords, min_samples=2)
    return centre_accuracy(centres, manual_clusters), centres
