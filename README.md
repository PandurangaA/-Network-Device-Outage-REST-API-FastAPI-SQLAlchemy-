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


Description : 
One of my key projects was designing and building a REST API for managing network devices and outages. The problem was that the team was handling device inventory and outage tracking manually in spreadsheets, which made it hard to track uptime, close outages, or run any analytics.
My task was to create a centralized API that could handle device details, log outages, and calculate uptime metrics automatically.
To implement this, I built a REST API using FastAPI and SQLAlchemy. I designed the database schema with tables for devices, outages, and metrics. The API allowed CRUD operations for devices, including geo-tagging with latitude and longitude. For outages, I built endpoints to log new incidents, close them, and automatically compute downtime. I also included health-check endpoints so that teams could quickly verify device status.
From a technical perspective, I used SQLAlchemy ORM to handle queries efficiently, and FastAPI for the API layer with proper validation and documentation through OpenAPI/Swagger. I tested the endpoints using Postman and implemented error handling for missing or invalid data.
The result was that the operations team had a single, reliable system to track devices and outages instead of scattered spreadsheets. It improved visibility into network performance, reduced manual errors, and saved significant time during outage reporting and audits.
Overall, the project gave me solid experience in building production-ready REST APIs with Python, FastAPI, and SQLAlchemy, and it also showed me how backend automation can make a direct impact on network operations
