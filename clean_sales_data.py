import pandas as pd

df = pd.read_csv("before.csv")

df = df.drop_duplicates()

df["customer_name"] = df["customer_name"].fillna("Unknown")
df["amount"] = df["amount"].fillna(0)

def parse_date(value):
    if pd.isna(value):
        return None
    for fmt in ("%d-%m-%Y", "%Y/%m/%d", "%d-%m-%y"):
        try:
            return pd.to_datetime(value, format=fmt)
        except ValueError:
            continue
    return None

df["date"] = df["date"].apply(parse_date)

df = df.dropna(subset=["date"])

df["date"] = df["date"].dt.strftime("%Y-%m-%d")

df.to_csv("after.csv", index=False)

print("CSV cleaned successfully!")
