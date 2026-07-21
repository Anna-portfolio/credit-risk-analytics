import pandas as pd
from pathlib import Path


BASE_PATH = Path(__file__).resolve().parent.parent
RAW_PATH = BASE_PATH / "data" / "raw"


def load_customers():
    path = RAW_PATH / "customers.csv"

    df = pd.read_csv(path)

    return df


def load_invoices():
    path = RAW_PATH / "invoices.csv"

    df = pd.read_csv(path)

    return df


def load_repayments():
    path = RAW_PATH / "repayments.csv"

    df = pd.read_csv(path)

    return df


def load_all_data():

    customers = load_customers()
    invoices = load_invoices()
    repayments = load_repayments()

    return {
        "customers": customers,
        "invoices": invoices,
        "repayments": repayments
    }
