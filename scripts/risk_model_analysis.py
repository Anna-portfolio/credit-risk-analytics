import sys
from pathlib import Path


# Add project root to Python path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))


from src.data_loader import load_all_data
from src.validation import validate_dataframe
from src.feature_engineering import (
    create_customer_features,
    create_risk_target
)
from src.model import train_model
from src.evaluation import evaluate_model


def main():

    print("Loading data...")

    data = load_all_data()


    # -------------------------
    # Validation
    # -------------------------

    print("\nRunning validation...")


    validate_dataframe(
        data["customers"],
        "customers",
        [
            "customer_id",
            "company_name"
        ]
    )


    validate_dataframe(
        data["invoices"],
        "invoices",
        [
            "invoice_id",
            "customer_id",
            "invoice_amount"
        ]
    )


    validate_dataframe(
        data["repayments"],
        "repayments",
        [
            "repayment_id",
            "invoice_id"
        ]
    )


    # -------------------------
    # Feature engineering
    # -------------------------

    print("\nCreating customer features...")


    features = create_customer_features(
        data["customers"],
        data["invoices"],
        data["repayments"]
    )


    # -------------------------
    # Risk target creation
    # -------------------------

    print("\nCreating risk classes...")


    features = create_risk_target(
        features
    )


    print("\nRisk class distribution:")

    print(
        features["risk_class"].value_counts()
    )


    # -------------------------
    # Model training
    # -------------------------

    print("\nTraining model...")


    model_dir = ROOT_DIR / "models"

    model_dir.mkdir(
        exist_ok=True
    )


    model_path = model_dir / "xgboost_model.pkl"


    model, X_test, y_test = train_model(
        features,
        model_path
    )


    print("\nModel trained successfully.")

    print(
        f"Model saved to: {model_path}"
    )


    # -------------------------
    # Model evaluation
    # -------------------------

    evaluate_model(
        model,
        X_test,
        y_test
    )


if __name__ == "__main__":
    main()
