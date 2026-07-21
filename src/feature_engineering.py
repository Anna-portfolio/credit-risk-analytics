import pandas as pd
import numpy as np
from datetime import datetime


def create_customer_features(
        customers,
        invoices,
        repayments
):

    # Create copies to avoid modifying original DataFrames
    customers = customers.copy()
    invoices = invoices.copy()
    repayments = repayments.copy()


    # -------------------------
    # Customer features
    # -------------------------

    customers["registration_date"] = pd.to_datetime(
        customers["registration_date"]
    )

    customers["company_age_years"] = (
        datetime.now() -
        customers["registration_date"]
    ).dt.days / 365


    customer_features = customers[
        [
            "customer_id",
            "industry",
            "segment",
            "annual_turnover",
            "company_age_years"
        ]
    ]


    # -------------------------
    # Invoice features
    # -------------------------

    invoice_features = (
        invoices
        .groupby("customer_id")
        .agg(
            invoice_count=("invoice_id", "count"),
            total_invoice_amount=("invoice_amount", "sum"),
            avg_invoice_amount=("invoice_amount", "mean"),
            overdue_invoice_ratio=(
                "payment_status",
                lambda x: (x == "Overdue").mean()
            )
        )
        .reset_index()
    )


    # -------------------------
    # Repayment features
    # -------------------------

    repayment_data = (
        repayments
        .merge(
            invoices[
                [
                    "invoice_id",
                    "customer_id",
                    "due_date"
                ]
            ],
            on="invoice_id",
            how="left"
        )
    )


    repayment_data["due_date"] = pd.to_datetime(
        repayment_data["due_date"]
    )

    repayment_data["repayment_date"] = pd.to_datetime(
        repayment_data["repayment_date"]
    )


    repayment_data["payment_delay_days"] = (
        repayment_data["repayment_date"]
        -
        repayment_data["due_date"]
    ).dt.days


    repayment_features = (
        repayment_data
        .groupby("customer_id")
        .agg(
            avg_payment_delay_days=(
                "payment_delay_days",
                "mean"
            ),

            max_payment_delay_days=(
                "payment_delay_days",
                "max"
            ),

            late_payment_ratio=(
                "payment_delay_days",
                lambda x: (x > 0).mean()
            )
        )
        .reset_index()
    )


    # -------------------------
    # Final dataset
    # -------------------------

    features = (
        customer_features
        .merge(
            invoice_features,
            on="customer_id",
            how="left"
        )
        .merge(
            repayment_features,
            on="customer_id",
            how="left"
        )
    )


    return features



def create_risk_target(features):

    features = features.copy()


    # -------------------------
    # Synthetic risk classification
    # based on payment behaviour
    # -------------------------

    conditions = [

        (
            (features["overdue_invoice_ratio"] >= 0.5)
            |
            (features["late_payment_ratio"] >= 0.5)
            |
            (features["avg_payment_delay_days"] > 30)
        ),

        (
            (features["overdue_invoice_ratio"] > 0)
            |
            (features["avg_payment_delay_days"] > 7)
        )
    ]


    choices = [
        "HIGH",
        "MEDIUM"
    ]


    features["risk_class"] = np.select(
        conditions,
        choices,
        default="LOW"
    )


    return features
