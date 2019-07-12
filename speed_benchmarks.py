import uuid
from app.benchmarks.speed import speed_benchmark
from app.db.models import SpeedBenchmarkScore, data_set
run_id = uuid.uuid4()
speed_benchmark(run_id)
query = SpeedBenchmarkScore.select().where(SpeedBenchmarkScore.run_id == run_id).order_by(SpeedBenchmarkScore.mean_time_taken)
data_set.freeze(query=query, format='csv', filename='results/speed_{}.csv'.format(run_id))

