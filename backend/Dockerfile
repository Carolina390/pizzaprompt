# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /backend

# Copy the current directory contents into the container at /app
COPY . /backend

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8080

# Define the command to run your application
CMD ["python", "dominosapi.py"]