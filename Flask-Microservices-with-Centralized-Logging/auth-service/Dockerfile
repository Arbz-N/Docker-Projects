FROM python:3.11-slim

# Create non-root user
RUN groupadd -g 1001 d_group \
    && useradd -u 1001 -g 1001 -s /bin/sh -m d_user


LABEL maintainer="arbaznaeem555@gmail.com" \
    creation_date="2026-01-26"

WORKDIR /login

# Install dependencies
COPY --chown=1001:1001 requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY --chown=1001:1001 app.py .
RUN chmod -R 755 /login && chmod -R 755 /login/*

# Switch to non-root user
USER d_user

# Run with Gunicorn
CMD ["gunicorn","-w","4","-b","0.0.0.0:8000","app:app"]
