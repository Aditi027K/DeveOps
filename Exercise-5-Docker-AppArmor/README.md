# Docker Security with AppArmor and Python

## Objective

The objective of this exercise is to understand how AppArmor can be used with Docker containers to provide an additional layer of security. The exercise also demonstrates how to apply and verify an AppArmor profile using the Docker SDK for Python.

## Technologies Used

- Docker Desktop
- Docker
- Python
- Flask
- Docker SDK for Python
- AppArmor
- WSL2

## Project Structure

```text
Exercise-5-Docker-AppArmor/
│
├── app.py
├── Dockerfile
├── apply_apparmor.py
├── test_restricted_actions.py
├── requirements.txt
└── README.md
Task 1: Flask Application
A simple Flask application was created in app.py.
The application runs on port 5000 and displays:
Hello, this is a secure Flask application running inside a Docker container!

Task 2: Dockerize the Application
A Dockerfile was created using the Python 3.8 slim image.
The Docker image was built using:
docker build -t flask-apparmor .

The container was successfully started and accessed through:
http://localhost:5000

Task 3: AppArmor Profile
An AppArmor profile named my-apparmor-profile was used with the Docker container.
The container was started using:
docker run -d --name apparmor-test --security-opt="apparmor=my-apparmor-profile" flask-apparmor

The applied security option was verified using:
docker inspect apparmor-test --format "{{json .HostConfig.SecurityOpt}}"

Output:
["apparmor=my-apparmor-profile"]

Task 4: Docker SDK for Python
The Docker SDK for Python was installed using:
pip install docker

The apply_apparmor.py script was used to:
1. Connect to Docker.
2. Build the Flask image.
3. Start a container with the AppArmor profile.
4. Inspect the container.
5. Verify the applied AppArmor profile.
6. Stop and remove the container.
The profile was successfully verified with:
AppArmor profile applied: ['apparmor=my-apparmor-profile']

Task 5: Test Restricted Actions
The test_restricted_actions.py script was created to test access to restricted resources.
The following actions were tested:
cat /etc/passwd

and:
/bin/bash

In the Docker Desktop + WSL2 environment used for this exercise, both commands were executable successfully.
This demonstrates that although the AppArmor profile was successfully attached to the container, the expected restrictions from the assignment were not enforced in this environment.
