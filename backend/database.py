import os

from pathlib import Path

from dotenv import load_dotenv

from sqlalchemy import create_engine

from sqlalchemy.engine import URL

from sqlalchemy.orm import DeclarativeBase


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


DB_SERVER = os.getenv("DB_SERVER")
DB_NAME = os.getenv("DB_NAME")
DB_DRIVER = os.getenv("DB_DRIVER")


if not DB_SERVER or not DB_NAME or not DB_DRIVER:
    raise RuntimeError("Database configuration is missing in .env")


DATABASE_URL = URL.create(

    "mssql+pyodbc",

    host=DB_SERVER,

    database=DB_NAME,

    query={

        "driver": DB_DRIVER,

        "trusted_connection": "yes"

    }

)


engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):

    pass