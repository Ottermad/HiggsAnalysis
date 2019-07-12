import uuid
from app.benchmarks.accuracy import accuracy_benchmark
from app.db.models import AccuracyBenchmarkScore, data_set
run_id = uuid.uuid4()
accuracy_benchmark(run_id)
query = AccuracyBenchmarkScore.select().where(AccuracyBenchmarkScore.run_id == run_id).order_by(AccuracyBenchmarkScore.mean_distances_from_clusters)
data_set.freeze(query=query, format='csv', filename='results/accuracy_{}.csv'.format(run_id))
