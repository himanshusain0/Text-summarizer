# Base image
FROM python:3.10-slim

# System packages
RUN apt-get update -y && apt-get install -y awscli

# Working directory
WORKDIR /app

# Copy project
COPY . /app

# 🔥 IMPORTANT FIX
ENV PYTHONPATH="/app/src"

# Upgrade pip
RUN pip install --upgrade pip

# Install torch
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Fix transformers
RUN pip install --upgrade accelerate
RUN pip install --upgrade transformers

# Expose port
EXPOSE 8080

# Run FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]