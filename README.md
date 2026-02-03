# PZ Stats

PZ Stats is a comprehensive statistics tracking system for Project Zomboid. It captures in-game events and provides a web-based dashboard for players to visualize their survival progress, zombie kills, and run history.

## Project Overview

The system captures data from the Project Zomboid server using a custom Lua mod and routes it through a series of microservices to a PostgreSQL database, ultimately displaying it on an Angular frontend.

## Microservices Architecture

The project is composed of several specialized components:

- **PZ Mod (Lua)**: A Project Zomboid mod that listens for game events (e.g., player deaths, stat updates) and prints JSON-formatted data to the server's console.
- **Log Forwarder (Python)**: A service that tails the Project Zomboid server logs, parses the JSON events, and sends them to the Backend API.
- **Backend (Flask)**: A Python-based REST API that handles incoming statistics, manages player and run records, and interfaces with the database.
- **Frontend (Angular)**: A modern web application providing a dashboard to view statistics and run histories.
- **Database (PostgreSQL)**: The central repository for all player, run, and statistic data.
- **Traefik**: A reverse proxy and load balancer that handles SSL termination (via Let's Encrypt) and routes traffic to the frontend and backend services.

## Setup Instructions

### Prerequisites
- Docker and Docker Compose installed on your system.
- A registered domain name pointing to your server's IP address (for SSL support).

### Environment Variables
1. Copy the `.env.example` file to create a `.env` file:
   ```bash
   cp .env.example .env
   ```
2. Configure the following variables in `.env`:
   - `DOMAIN`: Your domain (e.g., `stats.example.com`).
   - `ACME_EMAIL`: Your email for Let's Encrypt certificates.
   - `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`: Credentials for the PostgreSQL database.
   - `API_KEY`: A secret key for authenticating the Log Forwarder with the Backend.

### Running with Docker Compose
To build and start the entire stack:
```bash
docker-compose up -d --build
```
The frontend will be accessible at `https://${DOMAIN}` and the API at `https://${DOMAIN}/api`.

## Directory Structure

- `/backend`: Contains the Flask API, models, and Dockerfile.
- `/frontend`: Contains the Angular application. See the [frontend README](./frontend/README.md) for detailed frontend development instructions.
- `/mod`: Contains the Project Zomboid Lua mod files.
- `/postgres-init`: Directory for database initialization scripts.
- `/traefik`: Directory for Traefik-related configuration.

## Contributing & Testing

### Frontend
To run unit tests for the frontend application using Vitest:
```bash
cd frontend
npm install
npm test
```

### Backend
The backend uses Flask with SQLAlchemy. For local development, it defaults to a local SQLite database (`pz_stats.db`) if no `DATABASE_URL` is provided.

### Project Zomboid Mod
Lua scripts are located in `mod/media/lua/`. Contributions should follow the Project Zomboid modding conventions.
