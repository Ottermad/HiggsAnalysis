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