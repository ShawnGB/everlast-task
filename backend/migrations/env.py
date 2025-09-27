import sys
from pathlib import Path
import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy.ext.asyncio import AsyncEngine

# --- Pfad fixen, damit "src.*" funktioniert ---
BASE_DIR = Path(__file__).resolve().parents[1]  # /code im Container
sys.path.append(str(BASE_DIR))

# jetzt die richtigen Imports
from src.database.connection import Base, engine
from src.core.config import settings

# wichtig: alle Models importieren, damit sie bei Autogenerate erkannt werden
from src.leads import models as leads_models
from src.contact import models as contact_models

# Alembic Config
config = context.config

# Logging konfigurieren
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Das ist das Target für Autogenerate
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = settings.DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    """Synchroner Migration-Lauf."""
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations(connectable: AsyncEngine) -> None:
    """Asynchroner Migration-Lauf."""
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


def run_migrations_online() -> None:
    """Run migrations in 'online' mode (async)."""
    connectable: AsyncEngine = engine
    asyncio.run(run_async_migrations(connectable))


# Entry Point
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
