# Terraform Configuration for EKS Cluster for Particle41 Assessment 

**Assessment Overview**

This Terraform configuration deploys an EKS cluster in AWS Cloud. The infrastructure includes a VPC with 2 public and 2 private subnets, and an EKS cluster deployed to that VPC. The EKS cluster has 2 nodes of type `t2.medium` in the private subnets.

## AWS Authentication
if you already have an aws profile with your AWS credentials, you can select it by configuring the same in providers.tf provider for aws variable.

## Terraform Commands

To initialise with terraform and install all plugins providers:

```sh
terraform init
```

To see what changes Terraform will apply for the infra:

```sh
terraform plan
```

To apply the changes in the aws account:

```sh
terraform apply
```

To destroy the resources:

```sh
terraform destroy
```