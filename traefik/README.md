# Traefik Configuration

This directory is a placeholder for Traefik-related configuration. Currently, the Traefik configuration is primarily managed through the `docker-compose.yml` file to support environment variable interpolation.

## Purpose

Traefik serves as the edge router and reverse proxy for the application. Its main responsibilities include:
- **Routing**: Forwarding incoming HTTP/HTTPS requests to the appropriate backend or frontend services based on Host rules and Path prefixes.
- **SSL Termination**: Automatically managing and renewing SSL certificates using Let's Encrypt (ACME).
- **HTTP Redirection**: Automatically redirecting all port 80 (HTTP) traffic to port 443 (HTTPS).

## Configuration

The configuration is split into two parts:

### 1. Static Configuration
The static configuration (entrypoints, providers, certificate resolvers) is defined in the `command` section of the `traefik` service in `docker-compose.yml`.

Key features configured:
- **Entrypoints**: `web` (port 80) and `websecure` (port 443).
- **ACME (Let's Encrypt)**: Uses the `httpchallenge` on the `web` entrypoint.
- **Dashboard**: Enabled and available (insecure mode for internal access).

### 2. Dynamic Configuration
The dynamic configuration (routers and services) is defined using Docker labels on each service (e.g., `backend`, `frontend`) within `docker-compose.yml`.

## Environment Variables

The following environment variables are required for Traefik to function correctly:
- `DOMAIN`: The domain name where the application is hosted (e.g., `example.com`).
- `ACME_EMAIL`: The email address used for Let's Encrypt certificate registration and notifications.

## Certificate Storage

SSL certificates are stored in `/acme.json` within the Traefik container.
