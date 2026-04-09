# Particle41 Take Home Assessment 

**Repository Overview**

In this repo, we have 3 sections

- `.github/workflows/ci.yaml`
- `app`
- `Kubernetes Deployment (Killercoda)`

## .github/workflows/ci.yaml

**Overview**

In this section we have setup and created a github action workflow or CI pipeline which automates manual sdlc process like checking out the source code, building the application, scanning the docker image built and pushing it to dockerhub registry.

Stages used in CI pipeline are below :

- `Checkout code` : checking out the source code in runner servers.
- `Install Trivy (Open Source Container Security Tool)` : Installing trivy on runner servers.
- `Build Application Docker Image` : Building or containerising the application using docker
- `Log in to Docker registry (Dockerhub)` : Login into Dockerhub
- `Scan container image (trivy)` : Scanning the build image for container vulnerability
- `Push Application Docker Image (Dockerhub)` : Uploading or pushing the image to dockerhub

[Image for Reference]

<img width="953" height="435" alt="pipeline" src="https://github.com/user-attachments/assets/a688bcbf-feaf-4b8d-83f1-90ccb14e33fe" />


## app

**Overview**

In this section we are creating a simpletimeservice microservice application which displays timestamp and ip address of visitor in json. For the assessment I have used python flask framework. 

Below are the steps performed for creating, containerising and deployment in K8s cluster.

- `webapp.py` : Main logic code written for simpletimeservice application using python (flask).
- `requirements.txt` : Its used to mention all the dependencies or libraries used for the python application.
- `Dockerfile` : Main file used to write the logic and instructions to containerise the application using docker clis.
- `deployment.yaml` : Deployment file for deploying the application as pods in k8s cluster where containers are behind the pods.
- `service.yaml` : Service file which helps the deployment/pods to be get exposed in outer world or can be accessible from endpoint.
- `README.md` : Readme file with proper steps to replicate and execute the same.

[Image for Reference]

<img width="959" height="112" alt="app" src="https://github.com/user-attachments/assets/9a52fa1f-9131-441e-93fa-9980d5e6e487" />


## Kubernetes Cluster (Killercoda) 

**Overview**

In this section we are using kubernets manifest files to deploy in kubernetes cluster.

Below are the steps performed for creating, containerising and deployment in K8s cluster.

- `deployment.yaml` : It manages a set of Pods to run an application workload.
- `service.yaml` : It provides a stable network endpoint (IP address and DNS name) to access your Pods.

[Image for Reference]

<img width="959" height="434" alt="killercoda-ui" src="https://github.com/user-attachments/assets/5bfc9c92-acfd-468c-a315-8342684a131a" />


<img width="959" height="187" alt="killercoda-svc" src="https://github.com/user-attachments/assets/756e7895-7a78-4c55-989f-6c61f9bd29a5" />


