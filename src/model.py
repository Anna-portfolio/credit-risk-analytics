import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier


def train_model(features, model_path):

    data = features.copy()


    # -------------------------
    # Encode target
    # -------------------------

    encoder = LabelEncoder()

    data["risk_class_encoded"] = encoder.fit_transform(
        data["risk_class"]
    )


    # -------------------------
    # Prepare features
    # -------------------------

    X = data.drop(
        columns=[
            "customer_id",
            "risk_class",
            "risk_class_encoded"
        ]
    )


    y = data["risk_class_encoded"]


    # Encode categorical columns

    X = pd.get_dummies(
        X,
        columns=[
            "industry",
            "segment"
        ]
    )


    # -------------------------
    # Train / test split
    # -------------------------

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )


    # -------------------------
    # XGBoost model
    # -------------------------

    model = XGBClassifier(
        random_state=42,
        n_estimators=100,
        max_depth=3,
        learning_rate=0.1,
        eval_metric="logloss"
    )


    model.fit(
        X_train,
        y_train
    )


    # -------------------------
    # Save model
    # -------------------------

    joblib.dump(
        {
            "model": model,
            "encoder": encoder,
            "features": X.columns.tolist()
        },
        model_path
    )


    return model, X_test, y_test
