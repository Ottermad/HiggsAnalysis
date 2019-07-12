import uuid
from app.benchmarks.accuracy import accuracy_benchmark
from app.db.models import AccuracyBenchmarkScore, data_set
run_id = uuid.uuid4()
accuracy_benchmark(run_id)
query = data_set[AccuracyBenchmarkScore._meta.table_name].find(run_id=run_id)
data_set.freeze(query=query, format='csv', filename='results/accuracy_{}.csv'.format(run_id))
