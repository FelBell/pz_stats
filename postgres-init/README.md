# Database Initialization

Scripts placed in this directory are automatically executed by the PostgreSQL container when the database is first initialized.

## Usage

- Add `.sql` or `.sh` scripts here to define the initial schema or seed data.
- The scripts are mapped to `/docker-entrypoint-initdb.d` in the `db` container.
