# homework1
# Docker Workshop - NYC Taxi Data

This repository contains my homework for the Data Engineering Zoomcamp Docker + SQL assignment.

## Scripts

- `load_data.py` — loads taxi trip data into Postgres
- `load_zones.py` — loads NYC taxi zones CSV
- `query_data.py` — runs SQL queries for short trips, longest trips, and top zones
- `requirements.txt` — Python dependencies

## Data

- `green_tripdata_2025-11.parquet` — NYC green taxi trips (not pushed due to size)
- `taxi_zone_lookup.csv` — taxi zone lookup CSV

## How to run

1. Start Postgres container
2. Run `python load_data.py`
3. Run `python query_data.py`