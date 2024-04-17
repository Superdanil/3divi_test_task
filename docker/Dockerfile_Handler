FROM python:3.12.2-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY reqs.txt ./

RUN useradd -U app && mkdir -p /app && chown -R app:app /app

RUN pip install --no-cache-dir -r reqs.txt

WORKDIR /app/

COPY --chown=app:app settings.py .

COPY ./handler/ ./handler/
COPY ./schemas/ ./schemas/

EXPOSE ${WRITER_SERVICE_PORT}
EXPOSE ${INPUT_SERVICE_PORT}

ENV PYTHONPATH "${PYTHONPATH}:/app"

CMD ["sh", "-c", "python3 handler/main.py"]
