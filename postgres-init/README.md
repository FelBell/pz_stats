# PostgreSQL Initialization Scripts

This directory contains scripts that are automatically executed when the PostgreSQL container is first initialized.

## Purpose

Scripts placed in this directory are mapped to `/docker-entrypoint-initdb.d` in the `db` container. According to the official [PostgreSQL Docker image documentation](https://hub.docker.com/_/postgres), any `.sql`, `.sql.gz`, or `.sh` files found in that directory will be executed in alphabetical order to initialize the database.

This initialization only occurs if the PostgreSQL data directory (mapped to the `postgres_data` volume) is empty.

## Current Scripts

- `.gitkeep`: A placeholder file to ensure the directory is tracked by Git even when no initialization scripts are present.
