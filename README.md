# Media Content Management API

A high-performance RESTful API built with **FastAPI** to manage media content and streaming metadata. This project demonstrates a scalable backend architecture with modular routing and robust data validation.

## 🚀 Features
- **Modular Routing:** Organized using `APIRouter` for scalability.
- **Data Validation:** Powered by `Pydantic` schemas.
- **Security:** Implementation of Header-based API Key verification and Dependency Injection.
- **Auto Documentation:** Interactive API docs via Swagger UI and ReDoc.

## 📁 Project Structure
```text
├── main.py              # Application entry point
├── schemas.py           # Pydantic data models
├── dummy_db.py          # In-memory data store
├── dependencies.py      # Core logic for security/dependencies
└── routers/
    └── matches.py       # Endpoints for media/matches
