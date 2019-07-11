# Higgs Hunters Analysis

## Set up
* Make sure you have Python 3 installed (perhaps using a virtualenv)
* Make sure you have PostgreSQL installed and running on port ``5433``
* Create a database called ```higgs2_db``` 
* These parameters can be configured in `app/db/constants.py`
* Run `pip install -r requirements.txt`
* Import data by running `python3 import_simulated.py` and `python3 import_non_simulated.py`

## Data Imports
Some rows are not imported if their click_x or click_y entries are blank

## Benchmarks

### Speed Benchmarks

| Algorithm                | Size | Mean Time Taken |
|--------------------------|------|-----------------|
| DBSCAN                   | S    | 0.00108         |
| DBSCAN + Cluster Centres | S    | 0.0012          |
| DBSCAN                   | M    | 0.0013          |
| DBSCAN + Cluster Centres | M    | 0.00147         |
| DBSCAN                   | L    | 0.0024          |
| DBSCAN + Cluster Centres | L    | 0.00286         |
| DBSCAN                   | XL   | 0.00311         |
| DBSCAN + Cluster Centres | XL   | 0.00368         |
| KMeans                   | S    | 0.03236         |
| KMeans                   | M    | 0.03725         |
| KMeans                   | L    | 0.06914         |
| KMeans                   | XL   | 0.0806          |
| MeanShift                | S    | 0.13886         |
| MeanShift                | M    | 0.24238         |
| MeanShift                | L    | 0.51321         |
| MeanShift                | XL   | 0.80898         | 