# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements first to leverage Docker build cache
COPY requirements.txt .

# Install the application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the frontend application code
COPY app.py .

# Expose Streamlit's default port
EXPOSE 8501

# Run the Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
