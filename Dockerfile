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

# Set up environment variables
ENV PYTHON_ENV='PROD'
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV FLASK_DEBUG=0

# Add the Go bin directory to the PATH
ENV PATH=$PATH:/root/go/bin/

# Expose the port for the Flask application
EXPOSE 5000
EXPOSE 3000

# Run the Python application (assuming app.py is your entry point)
CMD ["python", "app.py"]

