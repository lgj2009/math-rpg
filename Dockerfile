FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# DB is created + seeded on first startup, not during build

EXPOSE 8000

CMD python -m uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}
