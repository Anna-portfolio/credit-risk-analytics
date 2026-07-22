"""
NOTE:
This project uses CSV files as the data source to keep the repository
self-contained and easy to run without access to a production database.

This module represents the production-ready database connection layer.
In a real-world environment, data would be loaded directly from SQL Server
via SQLAlchemy instead of pre-exported CSV files.
"""

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()


def get_connection():
    # Load database connection parameters from environment variables
    server = os.getenv("SQL_SERVER")
    database = os.getenv("DATABASE")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    # Update the ODBC driver name according to the local SQL Server installation
    connection_string = (
        f"mssql+pyodbc://{username}:{password}@{server}/{database}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )

    engine = create_engine(connection_string)

    return engine
