# The base image I used is an alpine version of python. Alpine has a small footprint and relatively few CVE-s.
# As this is a wery simple app and does not need a lot of dependencies I did not use a separate build stage.

FROM python:3.13-alpine

# Set the directory where the pid 1 process enters the container.
WORKDIR /app

# Install the needed dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the python app into the working directory.
COPY main.py .

# Set a user ID above 999 and preferably further to not collide with existing linux users.
# Collision would not inheritly be a problem, but as a best parctice is should not happen.
USER 10001

# Optional but good for documentation and can be used with "podman/docker -P" to auto allocate and expose a port.
EXPOSE 5000

# Set a CMD that starts the application.
CMD ["uvicorn", "main:my_app", "--host", "0.0.0.0", "--port", "5000"]