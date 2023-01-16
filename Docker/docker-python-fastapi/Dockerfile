FROM python:3.8-slim

LABEL maintainer="shlee@catchsecu.com"

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

WORKDIR /app

COPY ./app .

RUN pip3 install --upgrade pip && pip3 install --no-cache-dir --upgrade -r ./requirements.txt

ENV GOOGLE_APPLICATION_CREDENTIALS /app/airy-runway-344101-9fb121fbeb28.json

EXPOSE 8000

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn -k uvicorn.workers.UvicornWorker  --bind :$PORT --workers 2 --threads 8 --timeout 0 main:app