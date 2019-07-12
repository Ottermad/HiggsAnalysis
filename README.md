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
| DBSCAN                   | S    | 0.00122         |
| DBSCAN + Cluster Centres | S    | 0.00129         |
| DBSCAN                   | M    | 0.00130         |
| DBSCAN + Cluster Centres | M    | 0.00146         |
| DBSCAN                   | L    | 0.00235         |
| DBSCAN + Cluster Centres | L    | 0.00275         |
| DBSCAN                   | XL   | 0.00312         |
| DBSCAN + Cluster Centres | XL   | 0.00362         |
| KMeans                   | S    | 0.03630         |
| KMeans                   | M    | 0.04130         |
| KMeans                   | L    | 0.06523         |
| KMeans                   | XL   | 0.07688         |
| MeanShift                | S    | 0.18206         |
| MeanShift                | M    | 0.27798         |
| MeanShift                | L    | 0.49941         |
| MeanShift                | XL   | 0.77452         |

### Accuracy Benchmark
| zooniverse_id | projection | algorithm | number_of_clusters | expected_number_of_clusters | mean_distances_from_clusters | parameters |
|---------------|------------|-----------|--------------------|-----------------------------|------------------------------|------------|
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 10.89580                     | 155.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 10.89580                     | 165.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 10.89580                     | 160.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 10.89580                     | 145.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 10.89580                     | 150.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 10.89580                     | 140.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 39                 | 14                          | 11.65469                     | 10.00000   |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 11.85911                     | 175.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 11.85911                     | 185.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 11.85911                     | 180.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 11.85911                     | 170.00000  |
| AHH0000o3y    | XY         | MeanShift | 72                 | 8                           | 12.37632                     | 10.00000   |
| AHH0000myo    | RZzoom     | MeanShift | 33                 | 14                          | 12.53595                     | 15.00000   |
| AHH0000o3y    | XY         | MeanShift | 70                 | 8                           | 13.95188                     | 15.00000   |
| AHH0000myo    | RZzoom     | DBSCAN    | 12                 | 14                          | 14.22142                     | 30.00000   |
| AHH0000o3y    | XY         | DBSCAN    | 18                 | 8                           | 14.62970                     | 10.00000   |
| AHH0000myo    | RZzoom     | MeanShift | 26                 | 14                          | 14.77210                     | 20.00000   |
| AHH0000o3y    | XY         | MeanShift | 56                 | 8                           | 14.80047                     | 25.00000   |
| AHH0000o3y    | XY         | MeanShift | 62                 | 8                           | 14.86662                     | 20.00000   |
| AHH0000myo    | RZzoom     | DBSCAN    | 15                 | 14                          | 14.89996                     | 25.00000   |
| AHH0000myo    | RZzoom     | DBSCAN    | 12                 | 14                          | 14.97729                     | 35.00000   |
| AHH0000myo    | RZzoom     | MeanShift | 21                 | 14                          | 15.08397                     | 30.00000   |
| AHH0000myo    | RZzoom     | MeanShift | 22                 | 14                          | 15.26461                     | 25.00000   |
| AHH0000o3y    | XY         | DBSCAN    | 15                 | 8                           | 15.85503                     | 15.00000   |
| AHH0000o3y    | XY         | MeanShift | 54                 | 8                           | 16.07556                     | 30.00000   |
| AHH0000myo    | RZzoom     | DBSCAN    | 8                  | 14                          | 16.86491                     | 40.00000   |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 16.86910                     | 255.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 16.86910                     | 250.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 16.86910                     | 260.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 16.86910                     | 265.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 16.86910                     | 270.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 18                 | 14                          | 17.84154                     | 35.00000   |
| AHH0000myo    | RZzoom     | DBSCAN    | 7                  | 14                          | 18.09317                     | 45.00000   |
| AHH0000myo    | RZzoom     | MeanShift | 4                  | 14                          | 19.32052                     | 150.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 4                  | 14                          | 19.32052                     | 145.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 4                  | 14                          | 20.06602                     | 130.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 4                  | 14                          | 20.06602                     | 140.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 4                  | 14                          | 20.06602                     | 135.00000  |
| AHH0000o3y    | XY         | DBSCAN    | 11                 | 8                           | 20.25121                     | 20.00000   |
| AHH0000myo    | RZzoom     | MeanShift | 3                  | 14                          | 20.49840                     | 155.00000  |
| AHH0000o3y    | XY         | DBSCAN    | 14                 | 8                           | 20.75946                     | 25.00000   |
| AHH0000o3y    | XY         | DBSCAN    | 15                 | 8                           | 20.75946                     | 30.00000   |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 20.86685                     | 240.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 20.86685                     | 245.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 20.86685                     | 200.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 20.86685                     | 190.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 20.86685                     | 215.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 20.86685                     | 210.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 20.86685                     | 220.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 20.86685                     | 225.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 20.86685                     | 230.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 20.86685                     | 235.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 20.86685                     | 205.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 20.86685                     | 195.00000  |
| AHH0000lr6    | XY         | MeanShift | 5                  | 9                           | 21.21219                     | 110.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 4                  | 14                          | 21.26842                     | 95.00000   |
| AHH0000myo    | RZzoom     | MeanShift | 4                  | 14                          | 21.26842                     | 90.00000   |
| AHH0000myo    | RZzoom     | MeanShift | 4                  | 14                          | 21.48976                     | 105.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 4                  | 14                          | 21.48976                     | 100.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 3                  | 14                          | 21.51419                     | 165.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 3                  | 14                          | 21.51419                     | 160.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 7                  | 14                          | 21.56911                     | 60.00000   |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 21.57118                     | 275.00000  |
| AHH0000lr6    | XY         | MeanShift | 3                  | 9                           | 21.57118                     | 280.00000  |
| AHH0000lr6    | XY         | MeanShift | 21                 | 9                           | 21.59531                     | 10.00000   |
| AHH0000lr6    | XY         | MeanShift | 19                 | 9                           | 21.96207                     | 15.00000   |
| AHH0000myo    | RZzoom     | MeanShift | 4                  | 14                          | 22.04504                     | 110.00000  |
| AHH0000lr6    | XY         | MeanShift | 5                  | 9                           | 22.14524                     | 105.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 7                  | 14                          | 22.21408                     | 65.00000   |
| AHH0000myo    | RZzoom     | MeanShift | 4                  | 14                          | 22.23033                     | 85.00000   |
| AHH0000o3y    | XY         | MeanShift | 42                 | 8                           | 22.24938                     | 40.00000   |
| AHH0000myo    | RZzoom     | MeanShift | 4                  | 14                          | 22.25293                     | 120.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 4                  | 14                          | 22.25293                     | 125.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 4                  | 14                          | 22.25293                     | 115.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 5                  | 14                          | 22.31445                     | 80.00000   |
| AHH0000lr6    | XY         | MeanShift | 17                 | 9                           | 22.32099                     | 20.00000   |
| AHH0000lr6    | XY         | MeanShift | 15                 | 9                           | 22.32099                     | 25.00000   |
| AHH0000myo    | RZzoom     | MeanShift | 5                  | 14                          | 22.32877                     | 70.00000   |
| AHH0000o3y    | XY         | MeanShift | 47                 | 8                           | 22.33271                     | 35.00000   |
| AHH0000myo    | RZzoom     | DBSCAN    | 16                 | 14                          | 22.45296                     | 20.00000   |
| AHH0000myo    | RZzoom     | MeanShift | 5                  | 14                          | 22.76456                     | 75.00000   |
| AHH0000myo    | RZzoom     | MeanShift | 2                  | 14                          | 22.97964                     | 175.00000  |
| AHH0000lr6    | XY         | MeanShift | 4                  | 9                           | 23.06363                     | 125.00000  |
| AHH0000lr6    | XY         | MeanShift | 4                  | 9                           | 23.06363                     | 130.00000  |
| AHH0000lr6    | XY         | MeanShift | 4                  | 9                           | 24.05102                     | 120.00000  |
| AHH0000o3y    | XY         | DBSCAN    | 13                 | 8                           | 24.36262                     | 5.00000    |
| AHH0000lr6    | XY         | MeanShift | 4                  | 9                           | 24.36878                     | 115.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 2                  | 14                          | 24.68274                     | 170.00000  |
| AHH0000lr6    | XY         | MeanShift | 6                  | 9                           | 24.81181                     | 100.00000  |
| AHH0000lr6    | XY         | MeanShift | 4                  | 9                           | 24.91470                     | 135.00000  |
| AHH0000myo    | RZzoom     | DBSCAN    | 16                 | 14                          | 24.99338                     | 15.00000   |
| AHH0000lr6    | XY         | MeanShift | 7                  | 9                           | 25.87574                     | 75.00000   |
| AHH0000lr6    | XY         | MeanShift | 14                 | 9                           | 26.00191                     | 30.00000   |
| AHH0000myo    | RZzoom     | MeanShift | 8                  | 14                          | 26.06765                     | 55.00000   |
| AHH0000o3y    | XY         | MeanShift | 40                 | 8                           | 26.22042                     | 45.00000   |
| AHH0000o3y    | XY         | MeanShift | 39                 | 8                           | 26.27374                     | 50.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 1                  | 10                          | 26.87147                     | 280.00000  |
| AHH0000myo    | RZzoom     | DBSCAN    | 9                  | 14                          | 26.92486                     | 5.00000    |
| AHH0000myo    | RZzoom     | KMeans    | 14                 | 14                          | 27.20728                     |            |
| AHH0000lr6    | XY         | MeanShift | 6                  | 9                           | 28.68725                     | 90.00000   |
| AHH0000lr6    | XY         | DBSCAN    | 11                 | 9                           | 28.85869                     | 25.00000   |
| AHH0000lr6    | XY         | DBSCAN    | 11                 | 9                           | 28.93827                     | 20.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 1                  | 10                          | 29.02185                     | 285.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 1                  | 10                          | 29.02185                     | 295.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 1                  | 10                          | 29.02185                     | 290.00000  |
| AHH0000lr6    | XY         | MeanShift | 6                  | 9                           | 29.21010                     | 85.00000   |
| AHH0000lr6    | XY         | MeanShift | 6                  | 9                           | 29.21010                     | 80.00000   |
| AHH0000lr6    | XY         | MeanShift | 12                 | 9                           | 29.31582                     | 35.00000   |
| AHH0000myo    | RZzoom     | MeanShift | 16                 | 14                          | 29.55514                     | 40.00000   |
| AHH0000lr6    | XY         | MeanShift | 6                  | 9                           | 29.79119                     | 95.00000   |
| AHH0000lr6    | XY         | MeanShift | 12                 | 9                           | 29.80303                     | 40.00000   |
| AHH0000myo    | RZzoom     | MeanShift | 12                 | 14                          | 29.92794                     | 50.00000   |
| AHH0000lr6    | XY         | MeanShift | 2                  | 9                           | 29.99955                     | 290.00000  |
| AHH0000lr6    | XY         | MeanShift | 2                  | 9                           | 29.99955                     | 295.00000  |
| AHH0000lr6    | XY         | MeanShift | 2                  | 9                           | 29.99955                     | 285.00000  |
| AHH0000lr6    | XY         | DBSCAN    | 10                 | 9                           | 30.02240                     | 30.00000   |
| AHH0000lr6    | XY         | DBSCAN    | 12                 | 9                           | 30.77612                     | 15.00000   |
| AHH0000lr6    | XY         | DBSCAN    | 12                 | 9                           | 30.77612                     | 10.00000   |
| AHH0000lr6    | XY         | MeanShift | 11                 | 9                           | 30.80828                     | 45.00000   |
| AHH0000lr6    | XY         | MeanShift | 11                 | 9                           | 30.88216                     | 50.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 1                  | 10                          | 31.24022                     | 260.00000  |
| AHH0000lr6    | XY         | DBSCAN    | 10                 | 9                           | 31.48734                     | 45.00000   |
| AHH0000o3y    | XY         | DBSCAN    | 17                 | 8                           | 31.62182                     | 35.00000   |
| AHH0000myo    | RZzoom     | DBSCAN    | 15                 | 14                          | 31.77450                     | 10.00000   |
| AHH0000lr6    | XY         | DBSCAN    | 10                 | 9                           | 32.40622                     | 35.00000   |
| AHH0000lr6    | XY         | DBSCAN    | 10                 | 9                           | 32.40622                     | 40.00000   |
| AHH0000lr6    | XY         | MeanShift | 10                 | 9                           | 33.79612                     | 65.00000   |
| AHH0000lr6    | XY         | MeanShift | 10                 | 9                           | 33.87870                     | 60.00000   |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 33.89852                     | 180.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 33.89852                     | 185.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 1                  | 10                          | 34.17251                     | 235.00000  |
| AHH0000lr6    | XY         | MeanShift | 10                 | 9                           | 34.23796                     | 55.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 1                  | 10                          | 34.59134                     | 265.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 1                  | 10                          | 34.59134                     | 275.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 1                  | 10                          | 34.96942                     | 250.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 1                  | 10                          | 34.96942                     | 255.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 1                  | 10                          | 34.96942                     | 245.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 36.35393                     | 230.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 36.35393                     | 210.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 36.35393                     | 235.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 36.35393                     | 240.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 36.35393                     | 220.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 36.35393                     | 250.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 36.35393                     | 255.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 36.35393                     | 260.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 36.35393                     | 225.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 36.35393                     | 215.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 36.35393                     | 245.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 1                  | 10                          | 36.76955                     | 270.00000  |
| AHH0000lr6    | XY         | MeanShift | 9                  | 9                           | 36.85364                     | 70.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 1                  | 10                          | 37.05193                     | 240.00000  |
| AHH0000o3y    | XY         | MeanShift | 38                 | 8                           | 37.84086                     | 55.00000   |
| AHH0000lr6    | XY         | DBSCAN    | 13                 | 9                           | 38.91199                     | 5.00000    |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 40.01561                     | 190.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 40.01561                     | 205.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 40.01561                     | 200.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 40.01561                     | 195.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 2                  | 10                          | 41.41046                     | 210.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 1                  | 10                          | 42.49414                     | 215.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 2                  | 10                          | 45.03827                     | 200.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 2                  | 10                          | 45.03827                     | 205.00000  |
| AHH0000lr6    | XY         | KMeans    | 9                  | 9                           | 45.10610                     |            |
| AHH0001ram    | XYzoom     | MeanShift | 54                 | 10                          | 46.34069                     | 10.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 43                 | 10                          | 46.92355                     | 20.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 46                 | 10                          | 46.92355                     | 15.00000   |
| AHH0000myo    | RZzoom     | MeanShift | 14                 | 14                          | 48.02656                     | 45.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 41                 | 10                          | 48.23969                     | 25.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 38                 | 10                          | 48.67544                     | 30.00000   |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 50.24637                     | 295.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 50.24637                     | 265.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 50.24637                     | 270.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 50.24637                     | 275.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 50.24637                     | 280.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 50.24637                     | 285.00000  |
| AHH0000myo    | RZzoom     | MeanShift | 1                  | 14                          | 50.24637                     | 290.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 29                 | 10                          | 51.74938                     | 40.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 29                 | 10                          | 52.36172                     | 35.00000   |
| AHH0000o3y    | XY         | DBSCAN    | 18                 | 8                           | 54.57398                     | 40.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 28                 | 10                          | 54.87007                     | 45.00000   |
| AHH0000o3y    | XY         | DBSCAN    | 18                 | 8                           | 54.96353                     | 45.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 24                 | 10                          | 56.79548                     | 50.00000   |
| AHH0001ram    | XYzoom     | DBSCAN    | 29                 | 10                          | 59.45946                     | 20.00000   |
| AHH0001ram    | XYzoom     | DBSCAN    | 28                 | 10                          | 59.45946                     | 15.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 21                 | 10                          | 59.63718                     | 55.00000   |
| AHH0001ram    | XYzoom     | DBSCAN    | 24                 | 10                          | 59.93285                     | 30.00000   |
| AHH0001ram    | XYzoom     | DBSCAN    | 28                 | 10                          | 60.74549                     | 25.00000   |
| AHH0000o3y    | XY         | MeanShift | 35                 | 8                           | 60.82278                     | 60.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 2                  | 10                          | 65.24371                     | 225.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 2                  | 10                          | 65.24371                     | 230.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 2                  | 10                          | 66.54999                     | 220.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 4                  | 10                          | 68.31872                     | 155.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 4                  | 10                          | 70.84354                     | 150.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 18                 | 10                          | 71.52872                     | 60.00000   |
| AHH0001ram    | XYzoom     | DBSCAN    | 25                 | 10                          | 71.62107                     | 10.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 16                 | 10                          | 73.67815                     | 70.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 17                 | 10                          | 73.75843                     | 65.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 2                  | 10                          | 74.92984                     | 195.00000  |
| AHH0001ram    | XYzoom     | DBSCAN    | 21                 | 10                          | 76.96053                     | 35.00000   |
| AHH0000o3y    | XY         | MeanShift | 30                 | 8                           | 78.13348                     | 70.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 15                 | 10                          | 78.15777                     | 75.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 3                  | 10                          | 79.77805                     | 160.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 3                  | 10                          | 79.77805                     | 165.00000  |
| AHH0000o3y    | XY         | MeanShift | 31                 | 8                           | 79.94488                     | 65.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 13                 | 10                          | 82.45387                     | 80.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 3                  | 10                          | 83.73958                     | 185.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 3                  | 10                          | 83.78691                     | 180.00000  |
| AHH0001ram    | XYzoom     | DBSCAN    | 19                 | 10                          | 84.26471                     | 40.00000   |
| AHH0001ram    | XYzoom     | DBSCAN    | 18                 | 10                          | 84.35761                     | 45.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 3                  | 10                          | 85.13017                     | 175.00000  |
| AHH0000o3y    | XY         | MeanShift | 28                 | 8                           | 86.76542                     | 75.00000   |
| AHH0000o3y    | XY         | MeanShift | 27                 | 8                           | 89.02147                     | 80.00000   |
| AHH0001ram    | XYzoom     | DBSCAN    | 18                 | 10                          | 90.40007                     | 5.00000    |
| AHH0001ram    | XYzoom     | MeanShift | 13                 | 10                          | 98.79041                     | 85.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 4                  | 10                          | 102.63206                    | 170.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 11                 | 10                          | 103.00569                    | 90.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 3                  | 10                          | 103.44076                    | 190.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 11                 | 10                          | 109.69155                    | 100.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 6                  | 10                          | 112.64984                    | 145.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 7                  | 10                          | 112.77150                    | 130.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 7                  | 10                          | 113.20866                    | 135.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 7                  | 10                          | 116.31118                    | 125.00000  |
| AHH0000o3y    | XY         | MeanShift | 23                 | 8                           | 117.49492                    | 95.00000   |
| AHH0000o3y    | XY         | MeanShift | 26                 | 8                           | 117.49492                    | 90.00000   |
| AHH0000o3y    | XY         | MeanShift | 26                 | 8                           | 117.73480                    | 85.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 7                  | 10                          | 117.81531                    | 120.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 8                  | 10                          | 118.77801                    | 110.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 6                  | 10                          | 119.66989                    | 140.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 7                  | 10                          | 121.06393                    | 115.00000  |
| AHH0001ram    | XYzoom     | MeanShift | 10                 | 10                          | 121.18902                    | 95.00000   |
| AHH0001ram    | XYzoom     | MeanShift | 8                  | 10                          | 122.84545                    | 105.00000  |
| AHH0001ram    | XYzoom     | KMeans    | 10                 | 10                          | 125.12108                    |            |
| AHH0000o3y    | XY         | MeanShift | 21                 | 8                           | 140.46335                    | 100.00000  |
| AHH0000o3y    | XY         | MeanShift | 21                 | 8                           | 163.56612                    | 105.00000  |
| AHH0000o3y    | XY         | MeanShift | 19                 | 8                           | 206.02051                    | 110.00000  |
| AHH0000o3y    | XY         | MeanShift | 17                 | 8                           | 248.45204                    | 120.00000  |
| AHH0000o3y    | XY         | MeanShift | 18                 | 8                           | 248.45204                    | 130.00000  |
| AHH0000o3y    | XY         | MeanShift | 17                 | 8                           | 248.45204                    | 125.00000  |
| AHH0000o3y    | XY         | MeanShift | 15                 | 8                           | 249.02411                    | 140.00000  |
| AHH0000o3y    | XY         | MeanShift | 16                 | 8                           | 249.02411                    | 135.00000  |
| AHH0000o3y    | XY         | MeanShift | 18                 | 8                           | 250.24979                    | 115.00000  |
| AHH0000o3y    | XY         | MeanShift | 4                  | 8                           | 273.13057                    | 295.00000  |
| AHH0000o3y    | XY         | MeanShift | 15                 | 8                           | 275.74172                    | 150.00000  |
| AHH0000o3y    | XY         | MeanShift | 15                 | 8                           | 275.74172                    | 145.00000  |
| AHH0000o3y    | XY         | MeanShift | 13                 | 8                           | 276.17342                    | 155.00000  |
| AHH0000o3y    | XY         | MeanShift | 13                 | 8                           | 278.27340                    | 160.00000  |
| AHH0000o3y    | XY         | MeanShift | 13                 | 8                           | 278.54165                    | 165.00000  |
| AHH0000o3y    | XY         | MeanShift | 5                  | 8                           | 292.49190                    | 290.00000  |
| AHH0000o3y    | XY         | KMeans    | 8                  | 8                           | 299.14530                    |            |
| AHH0000o3y    | XY         | MeanShift | 6                  | 8                           | 299.76846                    | 275.00000  |
| AHH0000o3y    | XY         | MeanShift | 6                  | 8                           | 299.90033                    | 280.00000  |
| AHH0000o3y    | XY         | MeanShift | 6                  | 8                           | 301.34993                    | 240.00000  |
| AHH0000o3y    | XY         | MeanShift | 6                  | 8                           | 303.63952                    | 270.00000  |
| AHH0000o3y    | XY         | MeanShift | 12                 | 8                           | 304.95585                    | 175.00000  |
| AHH0000o3y    | XY         | MeanShift | 12                 | 8                           | 304.95585                    | 180.00000  |
| AHH0000o3y    | XY         | MeanShift | 11                 | 8                           | 306.54116                    | 185.00000  |
| AHH0000o3y    | XY         | MeanShift | 13                 | 8                           | 306.79171                    | 170.00000  |
| AHH0000o3y    | XY         | MeanShift | 6                  | 8                           | 307.69298                    | 265.00000  |
| AHH0000o3y    | XY         | MeanShift | 10                 | 8                           | 308.12546                    | 190.00000  |
| AHH0000o3y    | XY         | MeanShift | 6                  | 8                           | 309.84500                    | 260.00000  |
| AHH0000o3y    | XY         | MeanShift | 6                  | 8                           | 311.81719                    | 285.00000  |
| AHH0000o3y    | XY         | MeanShift | 7                  | 8                           | 321.82100                    | 255.00000  |
| AHH0000o3y    | XY         | MeanShift | 7                  | 8                           | 322.30429                    | 245.00000  |
| AHH0000o3y    | XY         | MeanShift | 7                  | 8                           | 323.12594                    | 235.00000  |
| AHH0000o3y    | XY         | MeanShift | 8                  | 8                           | 324.09336                    | 230.00000  |
| AHH0000o3y    | XY         | MeanShift | 9                  | 8                           | 330.02543                    | 220.00000  |
| AHH0000o3y    | XY         | MeanShift | 8                  | 8                           | 330.19857                    | 225.00000  |
| AHH0000o3y    | XY         | MeanShift | 8                  | 8                           | 335.99575                    | 250.00000  |
| AHH0000o3y    | XY         | MeanShift | 8                  | 8                           | 339.93190                    | 215.00000  |
| AHH0000o3y    | XY         | MeanShift | 8                  | 8                           | 343.01008                    | 210.00000  |
| AHH0000o3y    | XY         | MeanShift | 9                  | 8                           | 345.48001                    | 205.00000  |
| AHH0000o3y    | XY         | MeanShift | 9                  | 8                           | 346.74688                    | 200.00000  |
| AHH0000o3y    | XY         | MeanShift | 8                  | 8                           | 354.72775                    | 195.00000  |

### Summary
Mean Shift and DBSCAN produce similar results but DBSCAN is noticeably faster.

## Finding an EPS value