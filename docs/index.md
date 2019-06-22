# Index

- [Getting Started](#Getting-Started)
    - [Introduction](#Introduction)
    - [Dependencies](#Dependencies)
    - [Run locally](#Run-locally)
    - [Run remotely](#Run-remotely)
- [System Architecture]()
- [Services]()
    - [broker]()
    - [greenhouse]()
    - [humidity-rest]()
    - [moisture-mqtt]()
    - [moisture-rest]()
    - [user]()
    - [web]()

# Getting Started
## Introduction

This platform implements a greenhouse and plant monitoring service. The main focus was to provide __independent scalability for the different services__ in the platform to accommodate the needs of each greenhouse system. This allows a more efficient resource management and lower running costs. The platform can be reached through [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) and [MQTT](mqtt.org/) interfaces. The platform also provides a web application for data visualization and monitoring.

## Dependencies

To run the platform you will need [Docker](https://www.docker.com/) installed. Docker-compose comes bundled with Docker and is tool for defining and running multi-container Docker applications.

## Run locally

To run on your computer, clone the repository and run docker-compose has showed bellow:

```bash
    git clone https://github.com/dvcorreia/greenscale.git
```

```bash
    cd greenscale/services
    docker-compose up --build
```

To see if is up and running you can do `docker ps` and check if all the containers are running or for a fast test to `http://localhost` on your browser and see if the web application shows up.

## Run remotely

To run remotely you have to find a cloud hosting service that supports Docker applications. Follow the steps provided by your host service of choice.

# System architecture

Has said perviously, the system was design to be independently scalable. If you want to monitor more moisture sensors than humidity you can orchestrate more containers to do so.

## Micro-services networking

<img src='./assets/architecture-diagram.png' height='500px'/>

