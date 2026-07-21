import pandas as pd


def check_missing_values(df):
    """Return missing values for each column."""
    return df.isnull().sum()


def check_duplicates(df):
    """Return number of duplicated rows."""
    return df.duplicated().sum()


def check_required_columns(df, required_columns):
    """Check if all required columns exist."""
    return set(required_columns) - set(df.columns)


def validate_dataframe(df, name, required_columns):
    """Run basic validation checks."""

    print(f"\nValidation report: {name}")
    print("-" * 40)

    # Required columns
    missing_columns = check_required_columns(df, required_columns)

    if missing_columns:
        print(f"Missing columns: {missing_columns}")
    else:
        print("Required columns: OK")

    # Missing values
    missing = check_missing_values(df)

    if missing.sum() > 0:
        print("\nMissing values:")
        print(missing[missing > 0])
    else:
        print("Missing values: OK")

    # Duplicate rows
    duplicates = check_duplicates(df)

    if duplicates > 0:
        print(f"Duplicate rows: {duplicates}")
    else:
        print("Duplicate rows: OK")
