# Use an official Python 3.12 slim image
FROM python:3.12-slim

# Set environment variables to prevent prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install necessary system dependencies
RUN apt-get update && \
    apt-get install -y \
        libpq-dev \
        gcc \
        build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Create a virtual environment and install dependencies
RUN python3 -m venv $VIRTUAL_ENV && \
    $VIRTUAL_ENV/bin/pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Collect static files (if applicable)
RUN $VIRTUAL_ENV/bin/python manage.py collectstatic --noinput || true

# Expose port 8000 to allow external access
EXPOSE 8000

# Run the application using Gunicorn from the virtual environment
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "task_management.wsgi:application"]
