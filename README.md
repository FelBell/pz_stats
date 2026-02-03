# PZ Stats

PZ Stats is a comprehensive statistics tracking system for Project Zomboid. It collects in-game data such as zombie kills and player deaths, stores them in a centralized database, and provides a web interface for visualization.

## Architecture

The project is built using a microservices architecture, orchestrated with Docker Compose:

- **Backend:** A [Flask](https://flask.palletsprojects.com/) API that manages player data, game runs, and statistics.
- **Frontend:** An [Angular](https://angular.io/) web application that displays the statistics.
- **Database:** [PostgreSQL](https://www.postgresql.org/) for persistent storage of game data.
- **Reverse Proxy:** [Traefik](https://traefik.io/) for routing and automatic SSL management via Let's Encrypt.
- **Game Mod:** A [Lua](https://www.lua.org/) mod for Project Zomboid that tracks events and logs them.

## Setup Instructions

### Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Configuration

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and configure the following variables:
   - `DOMAIN`: Your deployment domain (e.g., `stats.example.com`).
   - `ACME_EMAIL`: Email for Let's Encrypt certificates.
   - `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`: Database credentials.
   - `API_KEY`: Secret key for API authentication.

### Running the Project

To start the entire stack:

```bash
docker-compose up -d --build
```

The frontend will be accessible at `https://${DOMAIN}` and the API at `https://${DOMAIN}/api`.

## Directory Overview

- [**backend/**](./backend/README.md): Flask API source code.
- [**frontend/**](./frontend/README.md): Angular frontend source code.
- [**mod/**](./mod/README.md): Project Zomboid Lua mod.
- [**traefik/**](./traefik/README.md): Reverse proxy configuration details.
- [**postgres-init/**](./postgres-init/README.md): Database initialization scripts.

## Testing

### Frontend
To run frontend unit tests:
```bash
cd frontend
npm install
npm test
```

### Backend
Backend testing instructions will be added as test coverage is implemented.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a clear description of your changes.

Ensure that all frontend tests pass before submitting your PR.
