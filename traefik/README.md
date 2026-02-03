# Traefik Configuration

This directory is intended for Traefik-related files and documentation.

## Purpose

Traefik is used as the edge router and reverse proxy for the `pz_stats` stack. It provides:

- **Automatic SSL/TLS Termination**: Using Let's Encrypt (ACME) to provide HTTPS for all services.
- **Dynamic Routing**: Automatically discovering and routing traffic to Docker containers based on labels.
- **HTTP to HTTPS Redirection**: Automatically upgrading insecure HTTP requests to HTTPS.
- **API Dashboard**: A dashboard to monitor the status of routers, services, and entrypoints.

## Configuration

### Static Configuration

The static configuration is defined in the `command` section of the `traefik` service in the root `docker-compose.yml` file. This approach was chosen to allow environment variable interpolation (e.g., `${ACME_EMAIL}`) which is not natively supported in a standalone `traefik.yml` file without extra templating.

Key static settings include:
- Entrypoints for `web` (:80) and `websecure` (:443).
- ACME (Let's Encrypt) configuration using the `httpchallenge`.
- Docker provider activation.

### Dynamic Configuration

Dynamic configuration (routers, services, and TLS settings) is managed through **Docker labels** on the individual service definitions in `docker-compose.yml`.

- **Backend**: Routed via `Host(${DOMAIN})` and `PathPrefix("/api")`.
- **Frontend**: Routed via `Host(${DOMAIN})`.

### SSL Certificates

SSL certificates are automatically requested and renewed by Traefik. They are stored in `/acme.json` within the Traefik container.

> **Note**: To avoid environment variable limitations in static configuration files, the `acme.json` file is not mounted from the host.

## Environment Variables

The Traefik configuration relies on the following variables in the `.env` file:

- `DOMAIN`: The domain name where the application is hosted.
- `ACME_EMAIL`: The email address used for Let's Encrypt registration and notifications.

## Files

- `docker-compose.yml` (root): Contains the Traefik service definition and routing labels.
- `acme.json` (internal): Stores SSL certificates (located inside the container).
