# Referral Fraud Detection

A data engineering and analytics project to detect suspicious referral behavior
using transaction, referral, and reward datasets.

## Project Structure

referral-fraud-detection/
├── data/
│ ├── raw/ # Original datasets
│ └── output/ # Fraud detection outputs
├── profiling/
│ └── data_profiling.csv
├── src/
│ ├── profiling.py
│ └── fraud_signals.py
├── docs/
│ └── README.md
├── .gitignore
└── README.md

## Fraud Detection Logic

### 1. Self-Referrals
Detects cases where a user refers themselves
(referrer_id == referee_id).

### 2. High-Volume Referrers
Identifies users who create an unusually high number of referrals,
which may indicate referral farming or automation.

### 3. Referrals Without Completed Transactions
Flags referrals that never result in a completed payment transaction.

## How to Run

From the project root:

```bash
python src/profiling.py
python src/fraud_signals.py
