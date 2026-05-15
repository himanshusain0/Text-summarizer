# Base image
FROM python:3.10-slim

# System dependencies
RUN apt-get update -y && apt-get install -y \
    awscli \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

ENV PYTHONPATH="/app/src"

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install torch==2.2.2 --index-url https://download.pytorch.org/whl/cpu

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install -e .

ENV HF_HOME="/app/.hf_cache"

RUN python -c "from transformers import pipeline; pipeline('summarization', model='philschmid/bart-large-cnn-samsum')"

EXPOSE 8080

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]