FROM python:3.10-slim

# Install system dependencies needed for wheels
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Upgrade build tools FIRST (this fixes setuptools.build_meta error)
RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt .

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Railway exposes PORT automatically
CMD gunicorn app:app --workers 1 --threads 1 --timeout 120 --bind 0.0.0.0:$PORT
