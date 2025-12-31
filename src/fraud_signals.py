import pandas as pd
from pathlib import Path

# ----------------------------
# Paths
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"
OUTPUT_DIR = BASE_DIR / "data" / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

# ----------------------------
# Load data
# ----------------------------
user_referrals = pd.read_csv(DATA_DIR / "user_referrals.csv")
transactions = pd.read_csv(DATA_DIR / "paid_transactions.csv")

print("Data loaded successfully")

# ============================================================
# FRAUD RULE 1: Self-referrals
# ============================================================
self_referrals = user_referrals[
    user_referrals["referrer_id"] == user_referrals["referee_id"]
]

self_referrals.to_csv(
    OUTPUT_DIR / "fraud_self_referrals.csv",
    index=False
)

print(f"Self-referrals detected: {len(self_referrals)}")

# ============================================================
# FRAUD RULE 2: Suspicious high-volume referrers
# ============================================================
referral_counts = (
    user_referrals
    .groupby("referrer_id")
    .size()
    .reset_index(name="referral_count")
)

suspicious_referrers = referral_counts[
    referral_counts["referral_count"] > 3
]

suspicious_referrers.to_csv(
    OUTPUT_DIR / "fraud_high_volume_referrers.csv",
    index=False
)

print(f"Suspicious referrers detected: {len(suspicious_referrers)}")

# ============================================================
# FRAUD RULE 3: Referrals without completed transactions
# ============================================================
completed_transactions = transactions[
    transactions["transaction_status"] == "completed"
]["transaction_id"]

referrals_without_payment = user_referrals[
    ~user_referrals["transaction_id"].isin(completed_transactions)
]

referrals_without_payment.to_csv(
    OUTPUT_DIR / "fraud_referrals_without_payment.csv",
    index=False
)

print(f"Referrals without completed transactions: {len(referrals_without_payment)}")

print("Fraud signal generation completed successfully")
