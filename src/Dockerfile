# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y build-essential libcairo2-dev pkg-config
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port
EXPOSE 8000