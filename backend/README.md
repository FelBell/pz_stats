# Backend Service

The Backend Service is a Python Flask API that handles data persistence for the Project Zomboid Statistics application. It provides endpoints for managing player information, game runs, and associated statistics.

## Key Files

- `app.py`: The main entry point of the Flask application. It defines the API routes and handles request logic.
- `models.py`: Contains the SQLAlchemy database models:
    - `Player`: Represents a game player (tracked by SteamID or Username).
    - `Run`: Represents an individual game session or "run".
    - `Stats`: Stores specific statistics for a run (e.g., zombies killed, time survived).
- `requirements.txt`: Lists the Python dependencies required to run the service.
- `Dockerfile`: Contains the build instructions for creating the backend container image.

## Getting Started

### Prerequisites

- Python 3.11+
- (Optional) Docker

### Running Locally

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment (Optional):**
   By default, the application uses a local SQLite database (`pz_stats.db`). To use a different database, set the `DATABASE_URL` environment variable:
   ```bash
   export DATABASE_URL="postgresql://user:password@localhost:5432/dbname"
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```
   The API will be available at `http://localhost:5000`.

### Running with Docker

1. **Build the image:**
   ```bash
   docker build -t pz-backend .
   ```

2. **Run the container:**
   ```bash
   docker run -p 5000:5000 pz-backend
   ```

## API Endpoints Overview

All API endpoints return JSON.

### Players
- `GET /api/players`: Retrieve a list of all players.
- `POST /api/players`: Create or update a player.
    - Required body: `{"id": "player_id", "name": "player_name"}`

### Runs
- `GET /api/runs`: Retrieve a list of all game runs.
- `POST /api/runs`: Create a new game run.
    - Required body: `{"player_id": "player_id"}`
    - Optional body: `{"start_time": "ISO-8601 string", "end_time": "ISO-8601 string", "is_dead": boolean}`

### Stats
- `GET /api/stats`: Retrieve all recorded statistics.
- `POST /api/stats`: Create or update statistics for a specific run.
    - Required body: `{"run_id": 1}`
    - Optional body: `{"zombies_killed": 100, "time_survived": 1234.5}`

## Database Configuration

The service uses SQLAlchemy to interact with the database. It is designed to work with both SQLite (for development) and PostgreSQL (for production). When running in the full stack via `docker-compose`, it connects to the `db` service.

All timestamps are handled in UTC.
