# Particle41 Take Home Assessment 

**Repository Overview**

In this repo, we have 3 sections

- `.github/workflows/ci.yaml`
- `app`
- `terraform`


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

## terraform

**Overview**

In this section we are using Terraform configuration to deploy an EKS cluster in AWS Cloud. The infrastructure includes a VPC with 2 public and 2 private subnets, and an EKS cluster deployed to that VPC.

Below are the steps performed for creating, containerising and deployment in K8s cluster.

- `backend.tf` : It configures the Terraform stores its state data which is placed at centralised location.
- `main.tf` : It configures the modules used for creating EKS its addons , vpc_cni_irsa and vpc components.
- `providers.tf` : It configures the providers used for accesssing aws and kubernetes.
- `README.md` : Readme file with proper steps to replicate and execute the same infra.
- `variables.tf` : It stores and handles all the variables used accross the terraform directory and aws resources.

