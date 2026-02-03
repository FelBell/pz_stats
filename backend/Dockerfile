FROM python:3.11-slim

WORKDIR /app

# Install system dependencies if needed (e.g., for psycopg2)
# Using psycopg2-binary, so we might not need gcc, but libpq-dev is often useful.
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
