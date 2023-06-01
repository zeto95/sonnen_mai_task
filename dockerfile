# Use an appropriate base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the Docker image
COPY . /app


# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Set the entry point command to execute your application
ENTRYPOINT ["python", "python_application.py"]