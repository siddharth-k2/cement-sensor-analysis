import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "database/plant_data.db"
)

query = """
SELECT *
FROM sensor_data
LIMIT 10
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()