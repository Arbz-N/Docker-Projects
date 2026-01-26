FROM python:3.11-slim

RUN addgroup -g 1001 -S d_group && adduser -S d_user -u 1001

LABEL maintainer="arbaznaeem555@gmail.com" \
    creation_date="2026-01-26"

WORKDIR /login

COPY --chown=d_group:d_group requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=d_group:d_group app.py .
RUN chmod -R 755 /login && chmod -R 755 /login/*

USER d_user

CMD ["gunicorn","-w","4","-b","0.0.0.0:8000","app:app"]
