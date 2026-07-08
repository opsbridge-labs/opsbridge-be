# MVC Architecture

Controllers own Flask request/response boundaries, services hold business rules, and repositories isolate SQLAlchemy 2.0 async persistence.
Persistence uses PostgreSQL through SQLAlchemy 2.0 Async Mode with the asyncpg driver.
