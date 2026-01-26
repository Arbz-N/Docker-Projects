FROM python:3.11-slim

RUN addgroup -g 1001 d_group && adduser -u 1001 -G d_group -S d_user

LABEL maintainer="arbaznaeem555@gmail.com" \
    creation_date="2026-01-26"

WORKDIR /payment

COPY --chown=1001:1001 requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=1001:1001 app.py .
RUN chmod -R 755 /order && chmod -R 755 /payment/*

USER d_user

CMD ["gunicorn","-w","4","-b","0.0.0.0:8000","app:app"]
