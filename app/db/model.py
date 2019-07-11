"""Connects to database and setups table."""
from peewee import (
    Model,
    AutoField,
    CharField,
    IntegerField,
    UUIDField,
    BooleanField,
    DateTimeField,
    DecimalField,
    PostgresqlDatabase
)
from .constants import DATABASE_NAME, PORT

db = PostgresqlDatabase(DATABASE_NAME, port=PORT)


class SimulatedImageClick(Model):
    """Represent a click on an image."""

    pk = AutoField(primary_key=True)
    click_set_id = CharField()
    user_id = IntegerField()
    logged_in = BooleanField()
    zooniverse_id = CharField()
    timestamp = DateTimeField()
    click_x = DecimalField(max_digits=15)
    click_y = DecimalField(max_digits=15)
    number_of_tracks = CharField()  # 2, 3, 4, 5-10 or 10+
    decay_type = CharField()
    mass = CharField()
    decay_length = CharField()
    projection = CharField()
    true_x1 = DecimalField(max_digits=15)
    true_y1 = DecimalField(max_digits=15)
    true_x2 = DecimalField(max_digits=15)
    true_y2 = DecimalField(max_digits=15)

    class Meta:
        """Provides peewee config."""

        database = db
        table_name = "TBL_SIMULATED_IMAGE_CLICK"


class SimulatedImageClickAll(Model):
    """Represent a click on an image."""

    pk = AutoField(primary_key=True)
    click_set_id = CharField()
    user_id = IntegerField()
    logged_in = BooleanField()
    zooniverse_id = CharField()
    timestamp = DateTimeField()
    click_x = DecimalField(max_digits=15)
    click_y = DecimalField(max_digits=15)
    number_of_tracks = CharField()  # 2, 3, 4, 5-10 or 10+
    decay_type = CharField()
    mass = CharField()
    decay_length = CharField()
    projection = CharField()
    true_x1 = DecimalField(max_digits=15)
    true_y1 = DecimalField(max_digits=15)
    true_x2 = DecimalField(max_digits=15)
    true_y2 = DecimalField(max_digits=15)

    class Meta:
        """Provides peewee config."""

        database = db
        table_name = "TBL_SIMULATED_IMAGE_CLICK_ALL"


class NonSimulatedImageClick(Model):
    """Represent a click on an image."""

    pk = AutoField(primary_key=True)
    click_set_id = CharField()
    user_id = IntegerField()
    logged_in = BooleanField()
    zooniverse_id = CharField()
    timestamp = DateTimeField()
    click_x = DecimalField(max_digits=15)
    click_y = DecimalField(max_digits=15)
    number_of_tracks = CharField()  # 2, 3, 4, 5-10 or 10+ or weird
    projection = CharField()

    class Meta:
        """Provides peewee config."""

        database = db
        table_name = "TBL_NON_SIMULATED_IMAGE_CLICK"


class AccuracyBenchmarkScore(Model):
    """Represent accuracy result of algorithm."""

    pk = AutoField(primary_key=True)
    run_id = UUIDField()
    zooniverse_id = CharField()
    projection = CharField()
    algorithm = CharField()
    number_of_clusters = IntegerField()
    expected_number_of_clusters = IntegerField()
    mean_distances_from_clusters = DecimalField()
    parameters = DecimalField(null=True)

    class Meta:
        """Provides peewee config."""

        database = db
        table_name = "TBL_ACCURACY_BENCHMARK"


class SpeedBenchmarkScore(Model):
    """Represent speed result of algorithm."""

    pk = AutoField(primary_key=True)
    run_id = UUIDField()
    algorithm = CharField()
    size = CharField()
    mean_time_taken = DecimalField(max_digits=20)

    class Meta:
        """Provides peewee config."""

        database = db
        table_name = "TBL_SPEED_BENCHMARK"


class SimulatedUserAccuracy(Model):
    """Record how accurate a simulated user is."""

    pk = AutoField(primary_key=True)
    mean_distance = DecimalField(max_digits=30)
    number_of_clicks = IntegerField()
    user_id = IntegerField(unique=True)

    class Meta:
        """Provides peewee config."""

        database = db
        table_name = "TBL_SIMULATED_USER_ACCURACY"


def create_tables():
    """Create database tables."""
    db.create_tables([
        SimulatedImageClick,
        NonSimulatedImageClick,
        AccuracyBenchmarkScore,
        SpeedBenchmarkScore,
        SimulatedUserAccuracy,
        SimulatedImageClickAll
    ])
