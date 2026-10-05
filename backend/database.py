from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase


DATABASE_URL = URL.create(
    "mssql+pyodbc",
    host=r"AK-47\SQLEXPRESS",
    database="MomatoDB",
    query={
        "driver": "ODBC Driver 17 for SQL Server",
        "trusted_connection": "yes"
    }
)


engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass