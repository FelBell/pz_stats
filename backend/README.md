# Backend API

This is the Flask-based backend for the PZ Stats project. It provides a RESTful API to manage and retrieve Project Zomboid player statistics.

## Tech Stack

- **Framework:** [Flask](https://flask.palletsprojects.com/)
- **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
- **Database:** PostgreSQL (via `psycopg2`)

## API Endpoints

- `GET /api/players`: List all players.
- `POST /api/players`: Create or update a player.
- `GET /api/runs`: List all game runs.
- `POST /api/runs`: Create a new game run.
- `GET /api/stats`: List all statistics.
- `POST /api/stats`: Update statistics for a specific run.

## Development

The backend uses environment variables for configuration, primarily `DATABASE_URL` and `API_KEY`. In development, it can fall back to a local SQLite database if `DATABASE_URL` is not provided.
