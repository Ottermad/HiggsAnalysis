"""Import data into database."""
from app.dataimports import import_simulated_data
import_simulated_data("data/higgshunters_vertices_allsim.csv", "data/not_importing_simulated.csv")
