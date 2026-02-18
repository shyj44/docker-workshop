import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm  # for progress bar

# --- STEP 1: Database connection ---
engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/ny_taxi"
)

# --- STEP 2: Read the green taxi trips data ---
taxi_file = "green_tripdata_2025-11.parquet"  # adjust path if needed
df = pd.read_parquet(taxi_file)

print(f"Loaded {len(df)} rows from {taxi_file}")

# Optional: inspect first few rows
print(df.head())

# --- STEP 3: Load into Postgres ---
# Use chunksize to avoid memory issues for very large files
tqdm.pandas(desc="Loading into Postgres")  # progress bar integration

df.to_sql(
    "green_taxi_trips",  # table name
    engine,
    if_exists="replace",  # 'replace' to recreate table, 'append' to add
    index=False,
    chunksize=5000,  # insert 5000 rows at a time
    method="multi",  # faster batch insert
)

print("Data loaded successfully into green_taxi_trips!")

