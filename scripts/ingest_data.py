import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# 1. Load raw data (replace with your actual CSV or API link)
csv_url = "https://example.com/musanze_potato_prices.csv"
df = pd.read_csv(csv_url)

# 2. Inspect the data
print("Preview of data:")
print(df.head())

# 3. Connect to PostgreSQL
# Adjust user, password, host, port, and database to your setup
engine = create_engine("postgresql+psycopg2://user:password@localhost:5432/potato_db")

# 4. Write data into staging table
df.to_sql("raw_potato_prices", engine, if_exists="replace", index=False)

print("Data successfully ingested into raw_potato_prices table!")
