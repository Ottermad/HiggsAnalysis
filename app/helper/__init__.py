"""Application wide helpers."""
import math


def get_coords_tuple(query):
    """Get coords tuple."""
    results_x =[float(r.click_x) for r in query]
    results_y = [-float(r.click_y) for r in query]

    coords = [(r[0], r[1]) for r in zip(results_x, results_y)]
    return coords


def distance_calc(coords_1, coords_2):
    """Calculate Euclidean Distance."""
    return math.sqrt(
        (coords_1[0] - coords_2[0])**2 +
        (coords_1[1] - coords_2[1])**2
    )
