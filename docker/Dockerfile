FROM python:3.12-slim-trixie

RUN apt-get update\
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/app.py .

RUN useradd --create-home --shell /bin/bash appuser

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]

