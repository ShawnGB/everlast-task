.PHONY: install start db-up db-down run test

run: db-up start
	@echo "Setup and start complete."

db-up:
	@echo "Starting Docker containers..."
	docker-compose up -d --build db

db-down:
	@echo "Stopping Docker containers..."
	docker-compose down

install:
	@echo "No explicit install needed. `docker-compose up` will build the image and install dependencies."

start:
	@echo "Starting the FastAPI server..."
	docker-compose up --build --force-recreate backend

test:
	@echo "Running tests..."
	docker-compose run --rm backend pytest


# =====================
# Database (Alembic)
# =====================

# Neue Migration erstellen (Usage: make revision msg="add new field")
revision:
	docker-compose run --rm backend alembic revision --autogenerate -m "$(msg)"

# Auf neueste Migration upgraden
migrate:
	docker-compose run --rm backend alembic upgrade head

# Eine Migration zurückrollen
downgrade:
	docker-compose run --rm backend alembic downgrade -1

# Aktuellen Status anzeigen
db-status:
	docker-compose run --rm backend alembic current

# Alle Migrationen anzeigen
db-history:
	docker-compose run --rm backend alembic history
	

seed: migrate
	@echo "Seeding database..."
	docker-compose run --rm backend python seed.py
	
