# Use an official Python runtime as base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy current directory contents into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
