# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5006

# Define environment variable for Flask run
ENV FLASK_APP=main.py
ENV PYTHONUNBUFFERED=1

# Run the application when the container launches
CMD ["python", "./main.py"]
