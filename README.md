# Recruiting-Challenge: Lead-Mini-CRM

## Überblick

Kleine, fokussierte Full-Stack-App für Lead-Verwaltung.  
Ziel: stabiler Kern (CRUD, Suche/Filter, Validierung), sauberes Schema, reproduzierbarer Start per Docker.

- **Backend**: FastAPI + SQLAlchemy (async) + Pydantic + Alembic + PostgreSQL
- **Frontend**: React + TypeScript + Vite (+ TanStack Query, Zod)
- **Dev**: Docker Compose (Services & Bootstrap), Linting/Tests

## Features

**Leads**

- Liste + Suche/Filter (Name/Domain)
- Anlegen mit Zod-Validierung (Domain inkl. `acme.com` _oder_ `https://acme.com`)
- Status ändern (inline, farbcodiert)
- Bearbeiten/Löschen über Modals

**Contacts**

- Entität samt API (CRUD), Zod-Typen und React-Query-Hooks vorbereitet
- Server-Seed mit Beispielkontakten
- Hinweis: **Keine vollständige UI-Integration** im Frontend – aus Zeitgründen priorisiert (siehe Trade-offs)

## Tech-Stack

**Backend**

- Python 3.11+, FastAPI, SQLAlchemy 2.x (async), Pydantic
- PostgreSQL
- **Alembic** (DB-Migrationen)

**Frontend**

- React + TypeScript + Vite
- TanStack Query (Fetching/Caching)
- Zod (Runtime-Validierung)
- Axios

**Dev & Qualität**

- Docker Compose (Orchestrierung von DB/Backend/Frontend, Bootstrap von Migrationen & Seeds)
- Ruff/Black (Lint/Format Python)
- ESLint (TS/React)
- Pytest (API-Tests)

## Setup & Start

### 1) Projekt klonen

```bash
git clone https://github.com/ShawnGB/everlast-task.git
cd everlast-task
```

### 2) Environment

```bash
cp .env.example .env
```

Die Defaults passen für den Docker-Start (DB-URL etc.).

### 3) Alles per Docker starten

```bash
docker compose up --build
```

Automatisch:

- Datenbank wird hochgefahren
- **Alembic-Migrationen** laufen
- **Seed-Daten** werden idempotent eingespielt
- Backend startet auf **:8000**, Frontend auf **:5173**

Zugriff:

- API: [http://localhost:8000](http://localhost:8000)
- Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
- Frontend: [http://localhost:5173](http://localhost:5173)

> Optional lokal: `cd frontend && npm ci && npm run dev` (wenn man das Frontend außerhalb von Docker starten möchte).

## API-Kurzüberblick

**Leads**

- `GET /leads/` – Liste (Query: `q`, `status`, `limit`, `offset`)
- `POST /leads/` – anlegen
- `GET /leads/{id}` – Detail
- `PUT /leads/{id}` – aktualisieren
- `DELETE /leads/{id}` – löschen

**Contacts**

- `GET /contacts/` – Liste
- `POST /contacts/` – anlegen
- `PUT /contacts/{id}` – aktualisieren
- `DELETE /contacts/{id}` – löschen

Swagger zeigt alle Schemas & Parameter.

## Tests

API-Tests mit **pytest**/**httpx**, eigene Test-DB im Container.

```bash
make test
```

## Architektur & Notizen

- **Validierung**: Pydantic im Backend, Zod im Frontend. Felder werden am Client _und_ Server geprüft. Domain-Regex erlaubt Werte _mit_ und _ohne_ Protokoll.
- **State/Fetched Data**: TanStack Query (schreibt invalidieren automatisch nach Mutationen).
- **Migrationen/Seeds**: Alembic für Schema; Seeds sind idempotent.

**Trade-offs (Zeitbudget)**

- Kontakte sind fachlich & technisch vorbereitet (Datenmodell, Endpoints, Zod-Typen, Hooks).
  Die **UI-Integration** (Bearbeiten/Hinzufügen im Lead-Modal) ist bewusst nicht finalisiert, um den stabilen Lead-Kern fertigzustellen.

## Nächste Schritte (wenn mehr Zeit)

- UI-Integration der Kontakte im Lead-Edit-Flow (einschl. E-Mail-Handling)
- E2E-Tests/Vitest für das Frontend
- kleinere UX-Verbesserungen (Optimistic Updates, Toasts)
