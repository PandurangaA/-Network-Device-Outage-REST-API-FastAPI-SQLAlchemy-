# -Network-Device-Outage-REST-API-FastAPI-SQLAlchemy-
"I designed and built a REST API for device inventory, live health checks, and outage tracking with automated uptime metrics.”

network-device-outage-api/
│
├── main.py              # FastAPI entrypoint
├── models.py            # SQLAlchemy models
├── crud.py              # Database operations
├── schemas.py           # Pydantic schemas
├── routers/             # API routes
├── utils/               # Ping/SNMP health checks
├── requirements.txt
├── alembic/             # Migrations
└── devices.db           # SQLite DB (auto-created)

