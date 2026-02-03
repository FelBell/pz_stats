# Postgres Initialization Scripts

This directory contains scripts used to initialize the PostgreSQL database for the Project Zomboid Stats application.

## Purpose

The `postgres-init/` directory is mounted to `/docker-entrypoint-initdb.d` in the PostgreSQL container. When the container is first started and the data volume is empty, any `.sql`, `.sql.gz`, or `.sh` scripts found in this directory will be automatically executed to initialize the database.

This is useful for:
- Creating additional databases or users.
- Initializing the database schema (if not handled by the application).
- Seeding the database with initial data.
- Creating PostgreSQL extensions.

## Execution Order

Scripts are executed in alphabetical order. To ensure a predictable execution order, it is recommended to prefix filenames with numbers (e.g., `01-init.sql`, `02-seed.sql`).

## Current Scripts

- `.gitkeep`: Ensures the directory is tracked by Git even when empty. Currently, the application uses SQLAlchemy's `db.create_all()` in `backend/app.py` for schema initialization.
