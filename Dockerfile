# Use the official Python base image
FROM python:3.11.3

# Set environment variables
ENV APP_HOME /app
ENV PORT 5000

# Set the working directory in the container
WORKDIR $APP_HOME

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt
RUN pip install gunicorn

# Copy the application code to the working directory
COPY . .

# Expose port 5000 to the outside world
EXPOSE $PORT

# Define the startup command
CMD ["python", "app.py"]
