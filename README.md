# OpsBridge BE

![Python](https://img.shields.io/badge/Python-3.12-3776ab?logo=python)
![Flask](https://img.shields.io/badge/Flask-REST-000000?logo=flask)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-SQLAlchemy_Async-4169e1?logo=postgresql)

운영 변경 요청, 승인, 감사 로그 흐름을 제공하는 Flask REST API입니다.

## 기능

- `POST /api/auth/login`
- `POST /api/auth/refresh`
- `GET /api/dashboard`
- `PATCH /api/events/{event_id}/status`
- OpenAPI 명세 제공
- k6 smoke script 제공

## 아키텍처

- 구조: MVC
- Framework: Flask
- ORM: SQLAlchemy 2.0 Async Mode
- Database: PostgreSQL
- Runtime: Gunicorn / Waitress

## 실행

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Docker

```bash
docker compose up --build
```

## 환경 변수

```bash
DATABASE_URL=postgres://app:app@localhost:5432/app
```

## 설계 메모

운영 변경 요청과 감사 로그를 분리해 승인 상태 변경, rollback 판단, 변경 이력 추적을 REST API로 다룰 수 있게 구성했습니다.
