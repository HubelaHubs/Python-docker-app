# Python Docker Application

This project is a simple Python application that demonstrates how to use Docker for deployment.

## Project Structure

```
python-docker-app
├── src
│   └── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Getting Started

To get started with this project, you need to have Docker installed on your machine. Follow the instructions below to build and run the Docker container.

## Prerequisites

- Docker installed on your machine.

## Building the Docker Image

Navigate to the project directory and run the following command to build the Docker image:

```
docker build -t python-docker-app .
```

## Running the Docker Container

After building the image, you can run the Docker container using the following command:

```
docker run python-docker-app
```

## Dependencies

The project dependencies are listed in the `requirements.txt` file. Make sure to install them if you are running the application outside of Docker.

## License

This project is licensed under the MIT License.