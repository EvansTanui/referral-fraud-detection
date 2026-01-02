# Referral Fraud Detection

A data engineering and analytics project designed to identify suspicious referral behavior using transaction, referral, and reward data.  
This project focuses on **interpretable, rule-based fraud signals**, reflecting how early-stage fraud detection systems are commonly implemented in production environments.

---

##  Project Objectives
- Detect fraudulent or abusive referral patterns in incentive-based systems
- Generate clear and explainable fraud signals for analyst review
- Demonstrate clean data engineering structure and reproducible analytics workflows
- Establish a foundation for future statistical or machine learning–based fraud detection

---

##  Project Structure
referral-fraud-detection/
├── data/
│ ├── raw/ # Source datasets (transactions, referrals, rewards)
│ └── output/ # Generated fraud signals and reports
├── profiling/
│ └── data_profiling.csv # Data quality checks and summary statistics
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

This behavior often indicates system abuse, test account misuse, or reward exploitation.

---

### 2. High-Volume Referrers
Identifies users generating an unusually high number of referrals compared to the overall population.

Such behavior may indicate:
- Referral farming
- Automated or scripted activity
- Coordinated fraud rings

---

### 3. Referrals Without Completed Transactions
Detects referrals that never result in a successful payment transaction.

This signal is useful for identifying:
- Incentive abuse
- Fake or low-quality accounts
- Abandoned referral attempts

---

##  Fraud KPIs

### Core Fraud Metrics
- Self-referral rate (0.2%)
- Percentage of referrals without completed transactions
- Average referrals per user
- Top 1% referrer contribution (15%)
- Fraud-flagged users as a percentage of total users

---

### Behavioral Metrics
- Referral velocity (referrals per day)
- Time between referral and first transaction
- Repeat referral patterns per user

---

### Business Impact Metrics
- Rewards issued to flagged users
- Estimated incentive leakage
- Conversion rate of clean vs flagged referrals

---

##  Outputs
- `fraud_signals.csv`: Aggregated fraud flags generated from rule-based detection
- `data_profiling.csv`: Dataset health indicators, null rates, and distributions

These outputs are designed to support:
- Fraud analyst investigations
- Dashboarding and reporting
- Escalation and review pipelines

---

##  How to Run

From the project root directory:

```bash
pip install -r requirements.txt
python src/profiling.py
python src/fraud_signals.py




