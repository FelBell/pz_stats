# Traefik Configuration

This directory is a placeholder for Traefik-related configurations. Currently, the Traefik setup is primarily managed through the `docker-compose.yml` file to facilitate environment variable interpolation.

## Overview

Traefik is used as the edge router and reverse proxy for the application. Its main responsibilities include:
- **Routing**: Directing incoming traffic to the appropriate service (frontend or backend).
- **SSL Termination**: Automatically managing SSL certificates via Let's Encrypt (ACME).
- **HTTP to HTTPS Redirection**: Ensuring all traffic is served over a secure connection.

## Static Configuration

The static configuration is defined in the `command` section of the `traefik` service in `docker-compose.yml`. Key settings include:

- **Entrypoints**:
  - `web`: Port 80, with a permanent redirection to `websecure`.
  - `websecure`: Port 443, for secure HTTPS traffic.
- **Providers**:
  - `docker`: Automatically discovers services based on Docker labels.
- **Certificates Resolvers**:
  - `letsencrypt`: Uses the ACME HTTP challenge on the `web` entrypoint. ACME email is configured via the `ACME_EMAIL` environment variable.
- **API/Dashboard**: Enabled (insecure mode for internal access).

## Dynamic Configuration

Dynamic routing is handled through Docker labels on individual services:

### Frontend
- **Rule**: `Host("${DOMAIN}")`
- **Entrypoint**: `websecure`
- **TLS**: Enabled with `letsencrypt` resolver.
- **Priority**: 1 (Lower priority to allow more specific rules to take precedence).

### Backend
- **Rule**: `Host("${DOMAIN}") && PathPrefix("/api")`
- **Entrypoint**: `websecure`
- **TLS**: Enabled with `letsencrypt` resolver.
- **Priority**: 2 (Higher priority than the frontend to ensure `/api` requests are routed correctly).

## Environment Variables

The following environment variables must be defined in the `.env` file for Traefik to function correctly:

- `DOMAIN`: The domain name where the application is hosted.
- `ACME_EMAIL`: The email address used for Let's Encrypt certificate registration.

## ACME Storage

SSL certificates are stored in `/acme.json` within the Traefik container.
