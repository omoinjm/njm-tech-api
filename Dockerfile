# Use an official Python runtime as a parent image
FROM python:3.8 AS base

# Install Go
RUN apt-get update && \
    apt-get install -y golang && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install hakrawler
RUN go install github.com/hakluke/hakrawler@latest

# Install gau
RUN go install github.com/lc/gau/v2/cmd/gau@latest

# Set the working directory to /app
WORKDIR /app

# Copy the contents of the "src" directory into the container at /app
COPY ./ /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn
RUN pip install gunicorn

# Expose the port for the Flask application
EXPOSE $PORT

# Run the Python application using Gunicorn
CMD gunicorn -b :$PORT app:app

