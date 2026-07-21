# Credit Risk Analytics Pipeline
created by @Anna-portfolio

## Business problem

This project demonstrates an end-to-end analytics pipeline for preparing credit risk data in a factoring environment.

The objective is to simulate a realistic portfolio of customers, invoices and repayments, perform data quality validation, engineer predictive features and train a machine learning model for customer risk classification.

> **Note:**  
> This repository uses a small synthetic dataset (3 files * 100 records each) created for demonstration purposes. The generated risk labels are based on engineered payment behaviour features and are intended to illustrate the complete machine learning pipeline rather than provide production-grade predictive performance.

---

## Tech Stack

- Python (pandas, NumPy, scikit-learn)
- SQL (Microsoft SQL Server)
- XGBoost
- SQLAlchemy
- pyodbc

---

## Project workflow

```text
SQL extraction
      ↓
CSV export
      ↓
Data loading
      ↓
Validation
      ↓
Feature engineering
      ↓
Risk target creation
      ↓
Model training (XGBoost)
      ↓
Model evaluation
      ↓
Model serialization (.pkl)
```

---

## Repository structure

```text
credit-risk-analytics/

├── data/
│   └── raw/
│       ├── customers.csv   
│       ├── invoices.csv    
│       └── repayments.csv  
│
├── sql/
│   ├── 01_extract_customers.sql    
│   ├── 02_extract_invoices.sql
│   ├── 03_extract_repayments.sql
│   └── 04_quality_checks.sql
│
├── src/
│   ├── connection.py
│   ├── data_loader.py
│   ├── validation.py
│   ├── feature_engineering.py
│   ├── model.py
│   └── evaluation.py
│
├── notebooks/
│   └── risk_model_analysis.py
│
├── models/
│   └── xgboost_model.pkl
│
├── requirements.txt
│
└── README.md
```

---

## Engineered features

The pipeline creates customer-level features such as:

- company age
- invoice count
- total invoice amount
- average invoice amount
- overdue invoice ratio
- average payment delay
- maximum payment delay
- late payment ratio

These features are used to build a synthetic customer risk classification target for demonstration purposes.

---

## Model

The project trains an **XGBoost Classifier** using engineered customer-level features.

The trained model is serialized and saved as:

```text
models/xgboost_model.pkl
```

---

## Model evaluation

The trained model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report

---

## Running the project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the pipeline:

```bash
python notebooks/risk_model_analysis.py
```