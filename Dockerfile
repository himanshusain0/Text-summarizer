# Base image
FROM python:3.10-slim

# System packages
RUN apt-get update -y && apt-get install -y awscli

# Working directory
WORKDIR /app

# Copy project
COPY . /app

# Upgrade pip (IMPORTANT)
RUN pip install --upgrade pip

# Install torch separately (stable CPU version)
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

# Install remaining dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Fix transformers issues (optional but safe)
RUN pip install --upgrade accelerate
RUN pip install --upgrade transformers

# Expose port
EXPOSE 8080

# Run FastAPI app
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]