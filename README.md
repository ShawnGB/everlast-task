````
# Recruiting-Challenge: Lead-Mini-CRM

## Überblick

Eine schlanke Fullstack-Anwendung bestehend aus:

- **Backend**: FastAPI + SQLAlchemy (async) + PostgreSQL
- **Frontend**: React + TypeScript (Platzhalter, folgt später)
- **Entwicklung**: Docker Compose für eine reproduzierbare Umgebung

## Tech-Stack

- **Backend**: Python 3.11+, FastAPI, SQLAlchemy 2.x, PostgreSQL
- **Dev-Tools**: Docker Compose, Ruff, Pytest

## Setup & Start

1. **Repository klonen**

   ```bash
   git clone https://github.com/ShawnGB/everlast-task.git
   cd everlast-task```

2. **Environment-Datei vorbereiten**

   ```bash
   cp .env.example .env
   ```

   Die Defaults in `.env.example` sind für Docker bereits passend gesetzt.

3. **Stack starten (Backend + Datenbank + Migrationen + Seeds)**

   ```bash
   docker compose up --build
   ```

   Dabei passiert automatisch:

   * Datenbank wird initialisiert
   * Alembic-Migrationen werden ausgeführt
   * Seed-Daten werden idempotent eingespielt
   * Backend startet auf Port 8000

   Zugriff im Browser:

   * API: [http://localhost:8000](http://localhost:8000)
   * Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

## Wichtige Entscheidungen

* **PostgreSQL** als Datenbank: unterstützt Constraints und sauberes Schema-Management
* **Docker Compose**: ein Kommando für Backend + DB, keine lokale Installation nötig

  * Ruff für Linting und Formatierung
  * Pytest für Tests

## Tests

Tests befinden sich im Verzeichnis `test/` und prüfen die API-Endpunkte (`contacts`, `leads`) mit **pytest** und **httpx**.
Eine separate Test-Datenbank wird im Container verwendet.

### Ausführen

```bash
make test
```

````
