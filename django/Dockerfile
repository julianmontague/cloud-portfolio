# syntax=docker/dockerfile:1

# Django 4.2.8 supports Python 3.12, the latest release
FROM docker.io/library/python:3.12-alpine
WORKDIR /app

# Support caching dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django code
COPY . .

# Run the Django server
# default localhost isn't accessible outside of local network
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
