import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgres://app:app@localhost:5432/app")
ORM = "SQLAlchemy 2.0 Async Mode"
DATABASE = "PostgreSQL"
REST_ONLY = True
