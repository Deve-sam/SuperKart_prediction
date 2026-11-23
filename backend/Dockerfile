# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements first to leverage Docker build cache
COPY requirements.txt .

# Install Gunicorn and project dependencies
RUN pip install --no-cache-dir gunicorn && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application code and serialized model files
COPY app.py .
COPY superkart_model.joblib ./backend_files/

# Expose the Flask API port
EXPOSE 7860

# Run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]
