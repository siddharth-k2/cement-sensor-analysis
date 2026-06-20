import pandas as pd
import sqlite3

# ==========================
# EXTRACT
# ==========================

print("Reading sensor data...")

df = pd.read_csv("data/sensor_data.csv")

print(f"Original Records: {len(df)}")

# ==========================
# TRANSFORM
# ==========================

print("Cleaning data...")

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Handle missing values
numeric_columns = [
    "temperature",
    "pressure",
    "vibration",
    "power_consumption",
    "production_rate"
]

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].mean())

# Remove invalid values

df = df[df["temperature"] > 0]
df = df[df["pressure"] > 0]
df = df[df["vibration"] > 0]
df = df[df["power_consumption"] > 0]
df = df[df["production_rate"] > 0]

# Outlier Handling (IQR Method)

for col in numeric_columns:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df = df[
        (df[col] >= lower) &
        (df[col] <= upper)
    ]

print(f"Cleaned Records: {len(df)}")

# ==========================
# LOAD
# ==========================

print("Loading into SQLite Database...")

conn = sqlite3.connect(
    "database/plant_data.db"
)

df.to_sql(
    "sensor_data",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("ETL Pipeline Completed Successfully!")