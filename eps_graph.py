from app.benchmarks.epssearch import plot_mean_distance_from_centres, plot_absolute_difference
from app.benchmarks.accuracy import accuracy_data
plot_mean_distance_from_centres(accuracy_data, 'results/mean_distance_1.png', range(10, 150, 10))
plot_absolute_difference(accuracy_data, 'results/absolute_difference_1.png', range(10, 150, 10))
plot_mean_distance_from_centres(accuracy_data, 'results/mean_distance_2.png', range(10, 50, 1))
plot_absolute_difference(accuracy_data, 'results/absolute_difference_2.png', range(10, 40, 1))
