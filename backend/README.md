# Backend Service

This directory contains the backend service for the Project Zomboid Stats tracker.

## Purpose
The backend is a Python Flask API responsible for receiving, processing, and storing game statistics from Project Zomboid. It provides a RESTful interface for the log-forwarder to submit data and for the frontend to retrieve it.

## Key Files
- `app.py`: The main entry point for the Flask application. It defines the API routes and handles request logic.
- `models.py`: Defines the SQLAlchemy database models (`Player`, `Run`, `Stats`) and their relationships.
- `requirements.txt`: Lists the Python dependencies required to run the service.
- `Dockerfile`: Contains instructions for building the Docker container for the backend service.

## Configuration
The backend uses the following environment variables:
- `DATABASE_URL`: The connection string for the database. Defaults to `sqlite:///pz_stats.db` if not provided.
- `API_KEY`: (Optional) Used for authenticating requests from the log-forwarder.

## Getting Started

### Local Development
To run the backend locally without Docker:

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the application:**
    ```bash
    python app.py
    ```
    The API will be available at `http://localhost:5000`.

### Running with Docker
To build and run the backend as a Docker container:

1.  **Build the image:**
    ```bash
    docker build -t pz-backend .
    ```

2.  **Run the container:**
    ```bash
    docker run -p 5000:5000 pz-backend
    ```

Alternatively, you can use `docker-compose` from the root directory to start the entire stack.
