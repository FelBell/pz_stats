# Frontend Service

This is the Angular-based frontend application for the Project Zomboid Statistics project. It provides a user interface to visualize player stats and game runs.

## Purpose

The frontend is an Angular application that fetches data from the backend API and displays it to the users. It is designed to be responsive and easy to navigate.

## Key Files

- **`package.json`**: Manages the project's dependencies and defines scripts for common tasks such as starting the development server, building for production, and running tests.
- **`nginx.conf`**: The configuration file for the Nginx web server used in production. It handles serving the static Angular files and contains a reverse proxy configuration to route `/api` requests to the backend service.
- **`Dockerfile`**: A multi-stage Dockerfile that:
  1.  Builds the Angular application in a Node.js environment.
  2.  Copies the resulting build artifacts into an Nginx-based image for efficient serving.
- **`proxy.conf.json`**: Used during local development with `ng serve`. It tells the Angular CLI development server to proxy requests starting with `/api` to the backend service (typically running on `http://backend:5000`).

## Running with Docker

The easiest way to run the frontend is as part of the entire project stack using Docker Compose.

From the root of the repository, run:

```bash
docker-compose up -d --build
```

This will build the frontend image and start it along with the other services (backend, database, etc.). By default, the frontend is accessible through the Traefik reverse proxy (usually on port 80/443, depending on your configuration).

## Local Development

If you want to run the frontend locally for development:

1.  Navigate to the `frontend/` directory:
    ```bash
    cd frontend
    ```
2.  Install dependencies:
    ```bash
    npm install
    ```
3.  Start the development server:
    ```bash
    npm start
    ```
    The application will be available at `http://localhost:4200`.

## Testing

To run the unit tests using Vitest:

```bash
npm test
```
