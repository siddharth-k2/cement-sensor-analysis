import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)

equipment = [
    "Kiln",
    "Crusher",
    "Raw Mill",
    "Cement Mill",
    "Packing Plant"
]

records = []

start_date = datetime(2026, 1, 1)

for i in range(1000):

    timestamp = start_date + timedelta(hours=i)

    machine = random.choice(equipment)

    temperature = round(np.random.normal(850, 40), 2)
    pressure = round(np.random.normal(12, 1.5), 2)
    vibration = round(np.random.normal(2.5, 0.5), 2)
    power = round(np.random.normal(150, 20), 2)
    production = round(np.random.normal(120, 15), 2)

    status = random.choice([
        "Running",
        "Idle",
        "Maintenance"
    ])

    records.append([
        timestamp,
        machine,
        temperature,
        pressure,
        vibration,
        power,
        production,
        status
    ])

df = pd.DataFrame(
    records,
    columns=[
        "timestamp",
        "equipment_name",
        "temperature",
        "pressure",
        "vibration",
        "power_consumption",
        "production_rate",
        "status"
    ]
)

# Introduce missing values
for col in [
    "temperature",
    "pressure",
    "vibration"
]:
    df.loc[
        df.sample(frac=0.02).index,
        col
    ] = np.nan

df.to_csv(
    "data/sensor_data.csv",
    index=False
)

print("Dataset Generated Successfully")