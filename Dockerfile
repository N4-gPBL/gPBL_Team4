FROM python:3.8

# Set the working directory to /app

WORKDIR /app

# Copy the current directory contents into the container at /app

COPY . /app

# Install any needed packages specified in requirements.txt

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8000 available to the world outside this container

EXPOSE 1337


CMD ["python", "manage.py", "runserver", "0.0.0.0:1337"]