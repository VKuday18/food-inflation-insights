import sqlite3
import pandas as pd
import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # project root
csv_path = os.path.join(BASE_DIR, "data", "processed", "cpi_food_clean.csv")
db_path = os.path.join(BASE_DIR, "data", "food_inflation.db")

# Load the CSV
df = pd.read_csv(csv_path)

# Optional: make sure columns look right
# print(df.head())

# Connect to SQLite (it will create the file if it doesn't exist)
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Drop table if exists (for re-runs)
cur.execute("DROP TABLE IF EXISTS food_cpi;")

# Create table
cur.execute("""
    CREATE TABLE food_cpi (
        date TEXT,
        series_id TEXT,
        category TEXT,
        value REAL
    );
""")

# Write data from DataFrame into the table
df.to_sql("food_cpi", conn, if_exists="append", index=False)

# Check a few rows
for row in cur.execute("SELECT * FROM food_cpi LIMIT 5;"):
    print(row)

conn.commit()
conn.close()

print(f"Database created at: {db_path}")