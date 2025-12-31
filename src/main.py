import pandas as pd
import os

RAW_DIR = "data/raw"

def load_csv(name):
    path = os.path.join(RAW_DIR, name)
    df = pd.read_csv(path)
    df.columns = df.columns.str.lower().str.strip()
    return df

def clean(df):
    for col in df.columns:
        if "at" in col:  # timestamp columns
            df[col] = pd.to_datetime(df[col], errors="coerce")
        if df[col].dtype == "object":  # string columns
            df[col] = df[col].astype(str).str.strip()
    return df

if __name__ == "__main__":
    user_referrals = clean(load_csv("user_referrals.csv"))
    print("Loaded user_referrals:", len(user_referrals))
