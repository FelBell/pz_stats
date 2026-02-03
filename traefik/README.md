# Traefik Configuration

This directory is a placeholder for Traefik-related configuration. Currently, most of the Traefik configuration is managed directly in the `docker-compose.yml` file via labels and command arguments.

## Responsibilities

- **Reverse Proxy:** Routes traffic to the `frontend` and `backend` services.
- **SSL Termination:** Automatically handles SSL certificates via Let's Encrypt.
- **HTTP to HTTPS Redirection:** Ensures all traffic is served over a secure connection.

## SSL Storage

SSL certificates are stored in `/acme.json` within the Traefik container.
