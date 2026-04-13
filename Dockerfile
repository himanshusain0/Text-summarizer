# Base image
FROM python:3.8-slim-buster

# System packages
RUN apt-get update -y && apt-get install -y awscli

# Working directory
WORKDIR /app

# Copy project
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Fix transformers issues
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

# Port expose (FastAPI)
EXPOSE 8080

# Run app with uvicorn (IMPORTANT change)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]