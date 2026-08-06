import pandas as pd

data = pd.read_csv("sample_market_data.csv")

print("Market Data Validation Report\n")

seen = set()

for _, row in data.iterrows():

    symbol = row["Symbol"]
    price = row["Price"]
    timestamp = row["Timestamp"]

    if pd.isna(price):
        print(f"{symbol}: Missing price")

    elif price <= 0:
        print(f"{symbol}: Invalid price")

    if timestamp != "09:30":
        print(f"{symbol}: Stale market data")

    if symbol in seen:
        print(f"{symbol}: Duplicate market data")

    seen.add(symbol)
