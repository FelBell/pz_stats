# Frontend Service

This is the Angular frontend for the Project Zomboid Statistics application. It provides a web interface for players to view their game statistics and leaderboard.

## Purpose
The frontend service serves as the user interface for the PZ Stats system. It communicates with the backend API to fetch and display player and run data.

## Key Files

- **`src/app/app.routes.ts`**: Defines the application routes and connects them to components (e.g., Dashboard, Statistics).
- **`src/app/services/stats.service.ts`**: An Angular service that uses `HttpClient` to communicate with the backend API endpoints (e.g., `/api/stats`).
- **`src/app/components/dashboard/dashboard.ts`**: The component for the dashboard view, displaying high-level statistics.
- **`proxy.conf.json`**: Configuration for the Angular development server to proxy API requests to the backend service (typically `http://backend:5000`) during development.

## Docker Usage

The frontend is containerized using a multi-stage Dockerfile. It builds the Angular application and then serves the static files using Nginx.

### Building and Running

To run the frontend as part of the entire stack, use:

```bash
docker-compose up -d --build
```

To build and run only the frontend service:

```bash
docker-compose up -d --build frontend
```

The frontend will be accessible at the domain specified in your `.env` file (via Traefik) or directly on port 80 of the container if running in a custom setup.

## Local Development

For local development without Docker:

1.  **Install dependencies**:
    ```bash
    npm install
    ```
2.  **Start the development server**:
    ```bash
    npm start
    ```
    This will use `proxy.conf.json` to route `/api` calls to `http://backend:5000`.

3.  **Open the application**:
    Navigate to `http://localhost:4200` in your browser.

## Testing

To run unit tests with Vitest:
```bash
npm test
```
