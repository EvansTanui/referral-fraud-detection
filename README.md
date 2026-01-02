# Referral Fraud Detection

A data engineering and analytics project designed to identify suspicious referral behavior using transaction, referral, and reward data.  
The project demonstrates how rule-based fraud signals can be engineered, profiled, and operationalized for investigation workflows.

---

##  Project Objectives
- Detect fraudulent or abusive referral patterns
- Generate interpretable fraud signals for analysts
- Showcase clean data engineering structure and reproducible analytics
- Lay foundations for future ML-based fraud detection

---

##  Project Structure
referral-fraud-detection/
├── data/
│ ├── raw/ # Source datasets (transactions, referrals, rewards)
│ └── output/ # Generated fraud signals and reports
├── profiling/
│ └── data_profiling.csv # Data quality & summary statistics
├── src/
│ ├── profiling.py # Data profiling and validation logic
│ └── fraud_signals.py # Rule-based fraud detection signals
├── docs/
│ └── README.md # Extended documentation (optional)
├── requirements.txt
├── .gitignore
└── README.md

---

##  Fraud Detection Logic

### 1. Self-Referrals
Flags cases where a user refers themselves:
Often indicates system abuse or test account exploitation.

### 2. High-Volume Referrers
Identifies users with an unusually high number of referrals compared to the population.
This may indicate:
- Referral farming
- Automated scripts
- Coordinated fraud rings

### 3. Referrals Without Completed Transactions
Detects referrals that never result in a successful payment.
Useful for identifying:
- Incentive abuse
- Fake or abandoned accounts

---

##  Fraud KPIs

### Core Fraud Metrics
- Self-referral rate (%)
- Percentage of referrals without completed transactions
- Average referrals per user
- Top 1% referrer contribution (%)
- Fraud-flagged users as a percentage of total users

### Behavioral Metrics
- Referral velocity (referrals per day)
- Time between referral and first transaction
- Repeat referral patterns per user

### Business Impact Metrics
- Rewards issued to flagged users
- Estimated incentive leakage
- Conversion rate: clean vs flagged referrals

---

##  Outputs
- `fraud_signals.csv`: Aggregated fraud flags per user
- `data_profiling.csv`: Dataset health, null rates, and distributions

These outputs are designed for:
- Fraud analyst review
- Dashboarding
- Escalation pipelines

---

##  How to Run

From the project root:
python src/profiling.py
python src/fraud_signals.py



