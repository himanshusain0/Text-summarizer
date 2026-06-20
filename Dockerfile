# Base image
FROM python:3.10-slim

# System dependencies
RUN apt-get update -y && apt-get install -y \
    awscli \
    build-essential \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

ENV PYTHONPATH="/app/src"
ENV HF_HOME="/app/.hf_cache"

RUN pip install --upgrade pip

# Step 1: torch pehle
RUN pip install torch==2.2.2 --index-url https://download.pytorch.org/whl/cpu

# Step 2: requirements install
RUN pip install --no-cache-dir -r requirements.txt

# Step 3: numpy lock karo - koi bhi upar na kar sake
RUN pip install "numpy==1.26.4" --force-reinstall

# Step 4: package install
RUN pip install -e .

# Step 5: numpy dobara lock karo (e. install ke baad)
RUN pip install "numpy==1.26.4" --force-reinstall

# Step 6: Model bake in
RUN python -c "from transformers import pipeline; pipeline('summarization', model='sshleifer/distilbart-cnn-12-6')"

EXPOSE 8080

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]