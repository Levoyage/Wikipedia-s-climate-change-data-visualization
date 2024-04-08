# Use the official Python 3.8 image as the base image
FROM python:3.8

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the application files from the host machine to the container's working directory
COPY . /app

# Install dependencies using pip
RUN pip install chardet requests Flask uwsgi pandas flask_cors pytz matplotlib

# Create a non-root user named "myappuser" with no password and no additional information
RUN adduser --disabled-password --gecos '' myappuser

# Switch to the non-root user "myappuser"
USER myappuser

# Command to run when the container starts:
# Start uWSGI with the main process manager, bind it to port 5000, use the specified module "backend:app",
# run with a single master process, and utilize 8 threads
CMD ["uwsgi", "--http", "0.0.0.0:5000", "--module", "backend:app", "--master", "--processes", "1", "--threads", "8"]
