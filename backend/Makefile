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
