# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY /project /app

RUN pip install Flask Flask-SQLAlchemy psycopg2-binary

EXPOSE 5000
CMD ["python", "app.py"]
