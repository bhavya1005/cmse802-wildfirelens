import pandas as pd
import sqlite3
import os


def load_and_clean_data(sqlite_path, output_path):
    # Connect to SQLite database
    conn = sqlite3.connect(sqlite_path)
    
    # Load the 'Fires' table
    df = pd.read_sql("SELECT * FROM Fires", conn)
    conn.close()

    # Select relevant columns
    keep_cols = [
        'FIRE_YEAR', 'DISCOVERY_DATE', 'STAT_CAUSE_DESCR',
        'FIRE_SIZE', 'FIRE_SIZE_CLASS', 'LATITUDE', 'LONGITUDE', 'STATE'
    ]
    df = df[keep_cols]

    # Convert Julian date to datetime
    df['DISCOVERY_DATE'] = pd.to_datetime(df['DISCOVERY_DATE'], origin='julian', unit='D')

    # Drop rows with missing lat/long or fire size
    df = df.dropna(subset=['LATITUDE', 'LONGITUDE', 'FIRE_SIZE'])

    # Save to CSV
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

    return df

if __name__ == "__main__":
    df = load_and_clean_data(
        "data/raw/FPA_FOD_20170508.sqlite",
        "data/processed/cleaned_fires.csv"
    )
    print(df.head())



