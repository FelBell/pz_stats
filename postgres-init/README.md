# Postgres Initialization Scripts

This directory is used for initializing the PostgreSQL database.

## Purpose

As defined in the `docker-compose.yml` file, this directory is mapped to `/docker-entrypoint-initdb.d` in the `db` service container. Any scripts placed here are executed when the database container is initialized for the first time.

## Scripts

Currently, this directory contains:

- `.gitkeep`: A placeholder file to ensure the directory is tracked by Git.
