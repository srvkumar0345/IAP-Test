# My K8s App

This project contains a simple Python Flask application that provides a `/version` endpoint, containerized with Docker, and deployed on a Kubernetes cluster. The project also includes a CI/CD pipeline configured using GitHub Actions.

## Project Structure
- `app/`: Contains the application code.
- `kubernetes/`: Kubernetes deployment and service manifests.
- `terraform/`: Infrastructure as Code using Terraform to provision Kubernetes.
- `.github/workflows/`: GitHub Actions CI/CD pipeline.
- `tests/`: Unit tests for the application.

## Setup Instructions

### Prerequisites
- Docker installed on your machine.
- Kubernetes cluster (EKS/GKE/AKS) or Minikube for local testing.
- kubectl configured to interact with your Kubernetes cluster.
- Terraform installed for infrastructure provisioning (optional).

### Building and Running Locally
1. Clone the repository.
2. Build the Docker image:
   ```bash
   docker build -t my-k8s-app .
   ```
3. Run the Docker container:
   ```bash
   docker run -p 5000:5000 my-k8s-app
   ```
4. Access the application at `http://localhost:5000/version`.

### Deploying to Kubernetes
1. Push the Docker image to a container registry (Docker Hub, ECR, etc.).
2. Apply the Kubernetes manifests:
   ```bash
   kubectl apply -f kubernetes/deployment.yaml
   kubectl apply -f kubernetes/service.yaml
   ```
3. Access the application using the external IP of the service.

### CI/CD Pipeline
- The GitHub Actions CI/CD pipeline automatically builds, tests, containerizes, and deploys the application to Kubernetes on each push to the `main` branch.

### Infrastructure Provisioning with Terraform (Bonus)
- Navigate to the `terraform/` directory and run:
  ```bash
  terraform init
  terraform apply
  ```
- This will provision an EKS cluster on AWS.

## Risks and Shortcomings
- Logginad and Monitoring setup needed.
- Test-case coverage should be increased.
- Container Vulnerability Scan should be done before deployment
