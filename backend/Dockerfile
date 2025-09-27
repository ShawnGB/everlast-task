FROM python:3.11-slim

# Arbeitsverzeichnis
WORKDIR /code

RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    netcat-traditional \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Python Dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Source Code
COPY . /code/

# Entrypoint
ENTRYPOINT ["/code/entrypoint.sh"]
