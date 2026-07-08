# OpsBridge BE

Flask RESTful backend for operations approval workflow.

## Architecture

- Backend shape: `MVC`
- Database: `PostgreSQL`
- ORM: `SQLAlchemy 2.0 Async Mode`
- Runtime: Python Flask with Gunicorn/Waitress, no Node.js backend
- API style: REST only. GraphQL was deliberately removed.

## demo-backend conversion

The source idea from `cyjoon68/demo-backend` is converted from NestJS/GraphQL style auth, user, phone verification, and token hardening into Flask REST endpoints:

- `POST /api/auth/login`
- `POST /api/auth/refresh`
- `GET /api/dashboard`
- `PATCH /api/events/{event_id}/status`

## Resume bullets

- Rebuilt demo-backend authentication semantics as Flask REST with JWT refresh flow.
- Implemented MVC backend using PostgreSQL and SQLAlchemy 2.0 Async Mode.
- Added OpenAPI, pytest contract tests, Docker Compose, and k6 p95 smoke threshold.
