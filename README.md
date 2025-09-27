# Recruiting-Challenge: Lead-Mini-CRM

## Überblick

Eine schlanke Fullstack-Anwendung bestehend aus:

- **Backend**: FastAPI + SQLAlchemy (async) + PostgreSQL
- **Frontend**: React + TypeScript
- **Entwicklung**: Docker Compose für reproduzierbare Umgebung

## Tech-Stack

- **Backend**: Python 3.11+, FastAPI, SQLAlchemy 2.x, PostgreSQL
- **Dev-Tools**: Docker Compose, Ruff, Pytest

## Setup & Start

1. **Repository klonen**

   ```bash
   git clone https://github.com/ShawnGB/everlast-task.git
   cd everlast-task
   ```

2. **Environment Variablen vorbereiten**

   Eine `.env` Datei aus der Vorlage erzeugen:

   ```bash
   cp .env.example .env
   ```

   Die `.env.example` enthält bereits funktionierende Defaults für den Docker-Stack:

   ```
   DATABASE_URL=postgresql+asyncpg://user:password@db/everlast_db
   ```

3. **Backend starten**

   ```bash
   cd backend/
   docker compose up --build
   ```

   Danach ist FastAPI erreichbar unter:
   👉 `http://localhost:8000`
   👉 Swagger UI: `http://localhost:8000/docs`

## Wichtige Entscheidungen

- **PostgreSQL** als DB: ermöglicht echte Constraints wie `UNIQUE (contact_id) WHERE is_primary`.
- **Docker Compose**: ein Kommando für Backend + DB, keine lokale Installation nötig.
- **SQLAlchemy 2.0 API**: moderne Typhinweise (`Mapped`, `mapped_column`).
- **Lifespan Context**: statt `@app.on_event` für DB-Init – aktueller FastAPI-Standard.
- **Qualität**:
  - **Ruff** für Linting/Formatierung
  - **Pytest** für Tests

## Tests

Tests liegen im Verzeichnis `test/` und prüfen die API-Endpunkte (`contacts`, `leads`) mit **pytest** und **httpx**.  
Die Test-DB wird dabei automatisch im Container aufgesetzt.

### Ausführen

Mit `make` (empfohlen):

```bash
make test
```
