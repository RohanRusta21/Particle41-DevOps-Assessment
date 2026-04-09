# Simple SimpleTimeService microsvc using python flask for Particle41 Assessment 

**Assessment Overview**

In this section we are creating a simpletimeservice microservice application which displays timestamp and ip address of visitor in json.

## Prerequisites
- `Python 3.11+`
- `pip`
- `flask`
- `Docker (Docker desktop)`

## Run the application (locally)

To execute the python application in terminal

```sh
pip3 install -r requirements.txt
python3 webapp.py
```

The server will start at http://0.0.0.0:8080

## Run the application (Docker)

Perform below steps after setup of deocker engine and daemon:

To build the application to make it dockerised

```sh
docker build -t username/docker-image-name:version .
```

To run the docker image as container to validate

```sh
docker run -it -p 8080:8080 --name my_container username/docker-image-name:version
```

## Run the application (Kubernetes Cluster)

As we have already containerised the application and setup Github Action Workflow (CI/CD pipeline) to automate building and pushing the image to dockerhub registry, so now we are just left to apply `deployment.yaml` and `service.yaml` files in the k8s cluster. The yaml files incorporates logics like `request & limits`, `health checks or probes`, etc.

Perform below steps after setup of deocker engine and daemon:

To apply the deployment (pods) file in kubernetes cluster

```sh
kubectl apply -f deployment.yaml
```

To apply the service (expose or access) file in kubernetes cluster

```sh
kubectl apply -f service.yaml
```



