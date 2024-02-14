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

# Set up environment variables using build arguments
ARG PYTHON_ENV
ARG FLASK_APP
ARG FLASK_ENV
ARG FLASK_DEBUG

# Set up environment variables
ENV PYTHON_ENV=${PYTHON_ENV}  
ENV FLASK_APP=${FLASK_APP}
ENV FLASK_ENV=${FLASK_ENV}
ENV FLASK_DEBUG=${FLASK_DEBUG}

# Add the Go bin directory to the PATH
ENV PATH=$PATH:/root/go/bin/

# Expose the port for the Flask application
EXPOSE 5000
EXPOSE 3000

# Expose the port for the Flask application
EXPOSE $PORT

# Run the Python application using Gunicorn
# CMD gunicorn -b :$PORT app:app

# Run the Python application (assuming app.py is your entry point)
CMD ["python", "app.py"]

