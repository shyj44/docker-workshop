import pandas as pd
from sqlalchemy import create_engine

# 1️⃣ Connect to your Postgres database
engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/ny_taxi"
)

# 2️⃣ Question 3: Count short trips (<= 1 mile in Nov 2025)
query_short_trips = """
SELECT COUNT(*) AS short_trips
FROM green_taxi_trips
WHERE lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime < '2025-12-01'
  AND trip_distance <= 1
"""
short_trips = pd.read_sql(query_short_trips, engine)
print("Q3 - Short trips (<=1 mile):")
print(short_trips, "\n")


# 3️⃣ Question 4: Pick-up day with longest trip (exclude trips >=100 miles)
query_longest_trip_day = """
SELECT DATE(lpep_pickup_datetime) AS pickup_day,
       MAX(trip_distance) AS longest_trip
FROM green_taxi_trips
WHERE lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime < '2025-12-01'
  AND trip_distance < 100
GROUP BY pickup_day
ORDER BY longest_trip DESC
LIMIT 1
"""
longest_trip_day = pd.read_sql(query_longest_trip_day, engine)
print("Q4 - Pick-up day with longest trip (under 100 miles):")
print(longest_trip_day, "\n")


# 4️⃣ Question 5: Biggest pickup zone by total_amount on Nov 18, 2025
query_biggest_zone = """
SELECT "PULocationID", SUM(fare_amount) AS total_amount
FROM green_taxi_trips
WHERE lpep_pickup_datetime >= '2025-11-18'
  AND lpep_pickup_datetime < '2025-11-19'
GROUP BY "PULocationID"
ORDER BY total_amount DESC
LIMIT 1
"""
biggest_zone = pd.read_sql(query_biggest_zone, engine)
print("Q5 - Pickup zone with largest total_amount on 2025-11-18:")
print(biggest_zone, "\n")


# 5️⃣ Question 6: Largest tip for pickups in East Harlem North in Nov 2025
# You need to replace 'X' with the PULocationID of East Harlem North from your zone CSV
EAST_HARLEM_NORTH_ID = X  # <- Replace this with correct ID

query_largest_tip = f"""
SELECT "DOLocationID", MAX(tip_amount) AS largest_tip
FROM green_taxi_trips
WHERE lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime < '2025-12-01'
  AND "PULocationID" = "{EAST_HARLEM_NORTH_ID}"
GROUP BY "DOLocationID"
ORDER BY largest_tip DESC
LIMIT 1
"""
largest_tip = pd.read_sql(query_largest_tip, engine)
print("Q6 - Drop-off zone with largest tip from East Harlem North in Nov 2025:")
print(largest_tip)