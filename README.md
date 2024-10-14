# TMS(Task Management System)

## Prerequisites

To run this project on your machine, ensure that you have the following installed:

    Docker
    Docker Compose
    Git (for cloning the repository)
 
## Installation

**Clone the repository**
````
git clone git@github.com:behmah/TMS.git
````
**Switch to the repo folder**
````
cd TMS
````
**Build the Docker images**
````
docker-compose build
````
**Start the services(Web application, Database & Nginx)**
````
docker-compose up
````
**Or start & scale the services with 3 web applications to see load balancer**
````
docker-compose up --scale web=3
````
**Access the TMS application in your browser**
````
http://localhost
````
**Hint: stop other server(Apache & ...) on your machine**
