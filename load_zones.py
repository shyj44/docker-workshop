import pandas as pd
from sqlalchemy import create_engine

# --- Database connection ---
engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/ny_taxi"
)

# --- Read taxi zone CSV ---
zones_file = "taxi_zone_lookup.csv"
zones_df = pd.read_csv(zones_file)

print(f"Loaded {len(zones_df)} rows from {zones_file}")
print(zones_df.head())

# --- Load into Postgres ---
zones_df.to_sql(
    "taxi_zones",
    engine,
    if_exists="replace",  # recreate table if exists
    index=False
)

print("Taxi zones loaded successfully!")