# Use an existing Python image as the base image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the script and requirements.txt to the working directory
COPY . .

# Install the required libraries
RUN pip install -r requirements.txt

# Set the entry point of the container
ENTRYPOINT ["python", "script.py"]