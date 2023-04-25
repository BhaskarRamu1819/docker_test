# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster
ADD requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app
ADD flask_rest_apis .
ADD flask_rest_apis.py .
CMD ["python", "flask_rest_apis.py"]
