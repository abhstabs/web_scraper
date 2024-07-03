# Use the official Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install fastapi uvicorn

# Copy the project files to the container
COPY . .

# Expose the port that FastAPI will run on
EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]