import pandas as pd
import sqlalchemy

# 1. Define data source (replace with real URL or local CSV path)
DATA_URL = "https://example.com/potato_prices.csv"  # placeholder

# 2. Load data into Pandas
def fetch_data():
    df = pd.read_csv(DATA_URL)
    return df

# 3. Clean data (basic example)
def clean_data(df):
    df = df.dropna()  # remove missing values
    df = df.drop_duplicates()  # remove duplicates
    df['date'] = pd.to_datetime(df['date'])  # ensure date format
    return df

# 4. Load into PostgreSQL
def load_to_postgres(df):
    # Update with your PostgreSQL credentials
    engine = sqlalchemy.create_engine(
        "postgresql://postgres:your_password@localhost:5432/potato_prices"
    )
    df.to_sql("raw_potato_prices", engine, if_exists="replace", index=False)
    print("Data successfully loaded into raw_potato_prices table.")

if __name__ == "__main__":
    data = fetch_data()
    data = clean_data(data)
    load_to_postgres(data)
