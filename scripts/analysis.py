import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect Database
conn = sqlite3.connect("database/plant_data.db")

# Load Data
df = pd.read_sql(
    "SELECT * FROM sensor_data",
    conn
)

# ==========================
# KPI Metrics
# ==========================

avg_temp = df["temperature"].mean()
max_vibration = df["vibration"].max()
avg_power = df["power_consumption"].mean()
total_production = df["production_rate"].sum()

print("\n===== KPI SUMMARY =====")
print(f"Average Temperature : {avg_temp:.2f}")
print(f"Maximum Vibration   : {max_vibration:.2f}")
print(f"Average Power Usage : {avg_power:.2f}")
print(f"Total Production    : {total_production:.2f}")

# ==========================
# Equipment Performance
# ==========================

equipment_stats = df.groupby(
    "equipment_name"
).agg({
    "power_consumption": "mean",
    "production_rate": "mean"
})

print("\n===== EQUIPMENT STATS =====")
print(equipment_stats)

# ==========================
# Chart 1
# Temperature Trend
# ==========================

plt.figure(figsize=(10,5))
plt.plot(df["temperature"])
plt.title("Temperature Trend")
plt.xlabel("Reading Number")
plt.ylabel("Temperature")
plt.grid(True)
plt.tight_layout()
plt.savefig(
    "reports/temperature_trend.png"
)

# ==========================
# Chart 2
# Vibration Trend
# ==========================

plt.figure(figsize=(10,5))
plt.plot(df["vibration"])
plt.title("Vibration Trend")
plt.xlabel("Reading Number")
plt.ylabel("Vibration")
plt.grid(True)
plt.tight_layout()
plt.savefig(
    "reports/vibration_trend.png"
)

# ==========================
# Chart 3
# Power Consumption
# ==========================

power_data = df.groupby(
    "equipment_name"
)["power_consumption"].mean()

plt.figure(figsize=(8,5))
power_data.plot(kind="bar")
plt.title("Average Power Consumption")
plt.ylabel("kWh")
plt.tight_layout()
plt.savefig(
    "reports/power_consumption.png"
)

print("\nReports Generated Successfully!")

conn.close()