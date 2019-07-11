"""Responsible for importing csv data into database."""
import datetime
from app.db.models import (
    NonSimulatedImageClick,
    SimulatedImageClick,
    db
)


def import_simulated_data(path_to_csv, error_path):
    """Read each csv file and adds to database."""
    data_source = []
    not_importing = []
    with open(path_to_csv) as f:
        first_line = True
        for line in f.readlines():
            # Skip header
            if first_line:
                first_line = False
                continue

            split_row = line.strip("\n").split(",")

            split_row = [i.strip('"') for i in split_row]

            if split_row[5] == '' or split_row[6] == '':
                not_importing.append(line)
                continue

            split_row[1] = int(split_row[1])  # User id
            split_row[2] = bool(int(split_row[2]))  # logged in

            split_row[4] = datetime.datetime.strptime(  # timestamp
                split_row[4], "%Y-%m-%d %H:%M:%S %Z"
            )

            # Click X + Y
            split_row[5] = float(split_row[5])
            split_row[6] = float(split_row[6])

            # Excel has changed 5-10 to 05-Oct
            if split_row[7] == "05-Oct":
                split_row[7] = "5-10"

            # True Decays
            split_row[12] = float(split_row[12])
            split_row[13] = float(split_row[13])
            split_row[14] = float(split_row[14])
            split_row[15] = float(split_row[15])

            data_source.append(split_row)

        print("Not Importing")
        print(not_importing)
        with open(error_path, "w+") as error_file:
            error_file.writelines(not_importing)

        with db.atomic():
            model = SimulatedImageClick
            for idx in range(0, len(data_source), 1000):
                model.insert_many(
                    data_source[idx: idx + 1000],
                    fields=[
                        model.click_set_id,
                        model.user_id,
                        model.logged_in,
                        model.zooniverse_id,
                        model.timestamp,
                        model.click_x,
                        model.click_y,
                        model.number_of_tracks,
                        model.decay_type,
                        model.mass,
                        model.decay_length,
                        model.projection,
                        model.true_x1,
                        model.true_y1,
                        model.true_x2,
                        model.true_y2,
                    ]
                ).execute()


def import_non_simulated_data(path_to_csv, error_path):
    """Read each csv file and adds to database."""
    data_source = []
    not_importing = []
    with open(path_to_csv) as f:
        for line in f.readlines():
            split_row = line.strip("\n").split(",")

            split_row = [i.strip('"') for i in split_row]

            # Click X or Y are empty
            if split_row[5] == '' or split_row[6] == '':
                not_importing.append(line)
                continue

            split_row[1] = int(split_row[1])  # User id
            split_row[2] = bool(int(split_row[2]))  # logged in

            split_row[4] = datetime.datetime.strptime(  # timestamp
                split_row[4], "%d/%m/%Y %H:%M"
            )

            # Click X + Y
            split_row[5] = float(split_row[5])
            split_row[6] = float(split_row[6])

            # Remove 'True' Decays
            del split_row[12:]

            # Remove data, 0, 0
            del split_row[8:11]

            data_source.append(split_row)

    print("Not Importing")
    print(not_importing)
    with open(error_path, "w+") as error_file:
        error_file.writelines(not_importing)

    with db.atomic():
        for idx in range(0, len(data_source), 1000):
            NonSimulatedImageClick.insert_many(
                data_source[idx: idx + 1000],
                fields=[
                    NonSimulatedImageClick.click_set_id,
                    NonSimulatedImageClick.user_id,
                    NonSimulatedImageClick.logged_in,
                    NonSimulatedImageClick.zooniverse_id,
                    NonSimulatedImageClick.timestamp,
                    NonSimulatedImageClick.click_x,
                    NonSimulatedImageClick.click_y,
                    NonSimulatedImageClick.number_of_tracks,
                    NonSimulatedImageClick.projection,
                ]
            ).execute()
