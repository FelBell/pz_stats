# PZ Stats

## Project Overview

**PZ Stats** is a comprehensive statistics tracking system for [Project Zomboid](https://projectzomboid.com/). It allows server administrators and players to track game events such as zombie kills, survival time, and player runs in real-time. The system collects data directly from the game server and presents it through a modern web interface.

The project is designed with a microservices architecture to ensure scalability and ease of deployment.

## Architecture

The PZ Stats ecosystem consists of several interconnected components:

- **PZ Mod (Lua)**: A custom mod installed on the Project Zomboid server. It monitors game events (player kills, survival time, etc.) and logs them to the server console in a structured JSON format.
- **Log Forwarder (Python)**: A service that tails the Project Zomboid server logs, extracts the JSON statistics data, and transmits it to the Backend API.
- **Backend (Flask)**: A RESTful API built with Python and Flask. It handles data ingestion from the Log Forwarder, manages player and run records, and serves data to the frontend.
- **Frontend (Angular)**: A modern web dashboard built with Angular. It provides a user-friendly interface for players to view their statistics and history.
- **Database (PostgreSQL)**: A relational database that persists all player data, game runs, and statistics.
- **Traefik**: A reverse proxy and load balancer that manages incoming traffic, handles routing to the frontend and backend, and automatically manages SSL certificates via Let's Encrypt.

## Setup and Installation

### Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Configuration

1. **Environment Variables**: Copy the example environment file and update it with your credentials:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and set the following variables:
   - `DOMAIN`: Your server's domain name (e.g., `stats.example.com`).
   - `ACME_EMAIL`: Email address for Let's Encrypt SSL certificates.
   - `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`: Database credentials.
   - `API_KEY`: A secret key for authenticating the Log Forwarder with the Backend.

### Deployment

To start the entire stack (Database, Backend, Frontend, Traefik), run:

```bash
docker-compose up -d --build
```

The frontend will be accessible at `https://${DOMAIN}` and the backend API at `https://${DOMAIN}/api`.

## Project Structure

- `backend/`: Flask API source code and requirements.
- `frontend/`: Angular application source code. See [frontend/README.md](frontend/README.md) for detailed frontend documentation.
- `mod/`: Project Zomboid Lua mod files.
- `postgres-init/`: Initialization scripts for the PostgreSQL database.
- `traefik/`: Configuration and storage for the Traefik reverse proxy.
- `docker-compose.yml`: Docker orchestration file for the entire stack.

## Contributing and Testing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with descriptive commit messages.
4. Push your branch and open a pull request.

### Testing

#### Frontend
The frontend uses [Vitest](https://vitest.dev/) for unit testing. To run the tests, navigate to the `frontend/` directory and run:

```bash
cd frontend
npm install
npm test
```

#### Backend
The backend is a Flask application. Ensure you have the dependencies installed:

```bash
cd backend
pip install -r requirements.txt
# Add backend testing instructions here when available
```
