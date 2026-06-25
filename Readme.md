# Multi-Service DevOps Application using Docker Compose

## Purpose

This project demonstrates how to deploy a three-tier multi-container application using Docker Compose. It consists of an Nginx web server, a Flask backend application, and a MySQL database, each running in separate Docker containers. Nginx acts as a reverse proxy, forwarding client requests to the Flask application, which communicates with the MySQL database.

## Technologies Used

* Docker
* Docker Compose
* Nginx
* Python
* Flask
* MySQL

## Features

* Three-tier application architecture
* Multi-container deployment using Docker Compose
* Nginx reverse proxy configuration
* Flask backend application
* MySQL database integration
* Persistent database storage using Docker Volumes
* Internal container networking
* Simple deployment using a single Docker Compose command

## Project Structure

```text
multi-service-app/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── nginx/
│   └── default.conf
│
└── docker-compose.yml
```

## File Overview

### backend/app.py

Contains the Flask backend application and establishes a connection with the MySQL database.

### backend/requirements.txt

Lists the Python packages required by the Flask application.

### backend/Dockerfile

Builds the Docker image for the Flask backend by installing dependencies and running the application.

### nginx/default.conf

Configures Nginx as a reverse proxy to forward incoming client requests to the Flask application.

### docker-compose.yml

Defines and manages all three services (Nginx, Flask, and MySQL), configures networking, environment variables, and persistent storage using Docker Volumes.

## Architecture

```text
        User
          │
          ▼
   Nginx Container
          │
          ▼
   Flask Container
          │
          ▼
   MySQL Container
          │
          ▼
    Docker Volume
```

## How to Run

### Build and start all containers

```bash
docker-compose up -d
```

### Check running containers

```bash
docker ps
```

### Stop all containers

```bash
docker-compose down
```

## Expected Output

* Nginx receives client requests on port 8080.
* Requests are forwarded to the Flask backend.
* Flask communicates with the MySQL database.
* Database data is stored persistently using Docker Volumes.
* All services communicate through Docker's internal network.

## Learning Outcomes

* Understanding multi-container applications
* Building a three-tier architecture using Docker
* Configuring Nginx as a reverse proxy
* Connecting Flask with MySQL
* Managing multiple services using Docker Compose
* Implementing container networking
* Using Docker Volumes for persistent database storage
* Deploying production-style containerized applications
