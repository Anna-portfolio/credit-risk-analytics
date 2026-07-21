from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


def evaluate_model(model, X_test, y_test):
    """
    Evaluate trained model on test data.
    """

    predictions = model.predict(X_test)

    print("\nModel Evaluation")
    print("-" * 40)

    print(
        f"Accuracy : {accuracy_score(y_test, predictions):.2f}"
    )

    print(
        f"Precision: {precision_score(y_test, predictions, zero_division=0):.2f}"
    )

    print(
        f"Recall   : {recall_score(y_test, predictions, zero_division=0):.2f}"
    )

    print(
        f"F1-score : {f1_score(y_test, predictions, zero_division=0):.2f}"
    )

    print("\nConfusion Matrix:")

    print(
        confusion_matrix(
            y_test,
            predictions
        )
    )

    print("\nClassification Report:")

    print(
        classification_report(
            y_test,
            predictions,
            zero_division=0
        )
    )
