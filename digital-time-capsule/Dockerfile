# Use official Python image
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential curl

# Install Node.js for building React
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy all source
COPY . .

# Build React frontend
WORKDIR /app/client
RUN npm install && npm run build

WORKDIR /app

ENV PORT=8080
EXPOSE 8080

CMD ["gunicorn", "-b", ":8080", "app:app"]
