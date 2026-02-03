# Frontend Service

This is the Angular frontend application for the Project Zomboid Stats project. It provides a user interface to view player statistics and game runs.

## Key Files

- **`Dockerfile`**: Defines the two-stage build process. It uses a Node.js image to build the Angular application and an Nginx image to serve the resulting static files.
- **`nginx.conf`**: The Nginx configuration used in the production Docker container. It handles routing for the Angular SPA (Single Page Application) and proxies requests starting with `/api/` to the backend service.
- **`proxy.conf.json`**: Configuration for the Angular development server (`ng serve`). It proxies API requests to the backend service during local development.
- **`package.json`**: Contains project dependencies and scripts for building, testing, and running the application.

## Running with Docker

The frontend is typically run as part of the project's Docker Compose stack.

### Build and Run

To build and start the entire stack, including the frontend:

```bash
docker-compose up -d --build
```

The frontend will be served on port 80 within its container, and Traefik will route external traffic to it based on the `DOMAIN` environment variable defined in your `.env` file.

## Local Development

To run the frontend locally for development:

1.  **Install dependencies**:
    ```bash
    cd frontend
    npm install
    ```

2.  **Start the development server**:
    ```bash
    npm start
    ```
    The application will be available at `http://localhost:4200`. It will proxy `/api` requests to `http://backend:5000` as defined in `proxy.conf.json`.

## Testing

Unit tests are managed with Vitest. To run the tests once:

```bash
npm test
```
