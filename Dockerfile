FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Seed database during build — ready on first request
RUN python build_seed.py

EXPOSE 8000

# Railway sets $PORT dynamically; fall back to 8000 for local / Render
CMD python -m uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}
