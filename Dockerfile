# Use an official Python runtime as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file to the container
COPY requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose a port (optional, adjust as needed)
EXPOSE 8000

# Set the command to run your application
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]