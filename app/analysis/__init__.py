from app.db.models import SimulatedImageClick, SimulatedUserAccuracy
from app.helper import distance_calc
import matplotlib.pyplot as plt
from peewee import fn
from app.db.models import (
    SimulatedUserAccuracy
)


def calculate_simulated_distances():
    """Calculate mean distance scores for users."""
    # For each row in simulated data calculate distance
    user_distances = {}
    query = SimulatedImageClick.select()
    for row in query:
        if row.user_id not in user_distances.keys():
            user_distances[row.user_id] = []

        distance_from_decay_1 = distance_calc(
            (row.true_x1, row.true_y1), (row.click_x, row.click_y))
        distance_from_decay_2 = distance_calc(
            (row.true_x2, row.true_y2), (row.click_x, row.click_y))

        if distance_from_decay_2 < distance_from_decay_1:
            user_distances[row.user_id].append(distance_from_decay_2)
        else:
            user_distances[row.user_id].append(distance_from_decay_1)

    for user, distances in user_distances.items():
        mean_distance = sum(distances) / len(distances)
        r = SimulatedUserAccuracy(
            mean_distance=mean_distance,
            number_of_clicks=len(distances),
            user_id=user
        )
        r.save()
    print(len(user_distances.keys()))


def plot_mean_distance_against_cumulative_users(filename):
    """Plot the mean distance against the cumulative users."""
    query = SimulatedUserAccuracy.select().order_by(
        +SimulatedUserAccuracy.mean_distance)

    user_total = range(1, query.count() + 1)

    mean_distances = [r.mean_distance for r in query]

    plt.plot(
        user_total,
        mean_distances,
        'ro',
    )

    plt.xlabel('Cumulative Number of Users')
    plt.ylabel('Mean Distance')

    plt.savefig(filename, dpi=400)


def plot_number_of_clicks_against_cumulative_users(filename):
    """Plot the number of clicks against the cumulative users."""
    query = SimulatedUserAccuracy.select(
        SimulatedUserAccuracy.number_of_clicks,
        fn.COUNT(SimulatedUserAccuracy.number_of_clicks).alias('count')
    ).group_by(
        SimulatedUserAccuracy.number_of_clicks
    ).order_by(
        +SimulatedUserAccuracy.number_of_clicks
    )

    user_total = [0]
    number_of_clicks = [0]

    for row in query:
        user_total.append(user_total[-1] + row.count)
        number_of_clicks.append(row.number_of_clicks)

    plt.plot(
        user_total,
        number_of_clicks,
        'ro',
    )

    plt.xlabel('Cumulative Number of Users')
    plt.ylabel('Number of Clicks Made By A User')

    plt.ylim(0, 100)

    plt.savefig(filename, dpi=400)
