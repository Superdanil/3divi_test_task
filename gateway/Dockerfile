FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/

COPY reqs.txt ./

RUN useradd -U app && mkdir -p /app && chown -R app:app /app

RUN pip install --no-cache-dir -r reqs.txt

COPY --chown=app:app settings.py .
COPY ./gateway/ ./gateway/
COPY ./schemas/ ./schemas/

EXPOSE ${GATEWAY_PORT}

ENV PYTHONPATH "${PYTHONPATH}:/app"

CMD ["sh", "-c", "python3 gateway/main.py"]
