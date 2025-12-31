import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw")
OUTPUT_PATH = Path("profiling")
OUTPUT_PATH.mkdir(exist_ok=True)

FILES = {
    "user_referrals": "user_referrals.csv",
    "user_referral_logs": "user_referral_logs.csv",
    "user_logs": "user_logs.csv",
    "user_referral_statuses": "user_referral_statuses.csv",
    "referral_rewards": "referral_rewards.csv",
    "paid_transactions": "paid_transactions.csv",
    "lead_logs": "lead_logs.csv",
}

profiling_results = []

for table_name, file_name in FILES.items():
    file_path = RAW_DATA_PATH / file_name
    df = pd.read_csv(file_path)

    for col in df.columns:
        profiling_results.append({
            "table_name": table_name,
            "column_name": col,
            "data_type": str(df[col].dtype),
            "null_count": int(df[col].isna().sum()),
            "distinct_count": int(df[col].nunique(dropna=True))
        })

profiling_df = pd.DataFrame(profiling_results)

profiling_df.to_csv(
    OUTPUT_PATH / "data_profiling.csv",
    index=False
)

print("Data profiling completed: profiling/data_profiling.csv")
