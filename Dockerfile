# Base image
FROM python:3.10-slim

# System dependencies
RUN apt-get update -y && apt-get install -y \
    awscli \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project
COPY . /app

# Fix PYTHONPATH
ENV PYTHONPATH="/app/src"

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies FIRST (faster builds)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install torch CPU version
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

# Install project
RUN pip install -e .

# Fix transformers issues
RUN pip install --upgrade accelerate transformers

# Expose port
EXPOSE 8080

# Run FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]