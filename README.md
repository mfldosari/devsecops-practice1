# DevSecOps CI/CD Pipeline

This repository contains a secure CI/CD pipeline implementation for a Python application using GitHub Actions. The pipeline incorporates security scanning at multiple stages following DevSecOps best practices.

## Pipeline Overview

This automated workflow performs the following steps on every push to the `main` branch:

1. **Code Checkout**: Pulls the latest code from the repository
2. **Python Environment Setup**: Configures Python 3.11
3. **Dependency Installation**: Installs Python dependencies
4. **Security Scanning**:
   - **SAST**: Runs Bandit for static application security testing
5. **Docker Operations**:
   - Builds a Docker image
   - Scans the image with Trivy for vulnerabilities
6. **Container Registry**:
   - Logs into DockerHub
   - Pushes the secured image
7. **Deployment**:
   - Deploys to an Azure VM via SSH
   - Runs the containerized application
8. **Notifications**:
   - Sends success/failure alerts to Slack

## Security Components

### Static Application Security Testing (SAST)
- Uses **Bandit** to scan Python code for common security issues

### Container Security
- Uses **Trivy** to scan Docker images for vulnerabilities before deployment

### Secrets Management
- Uses GitHub Secrets to securely store:
  - DockerHub credentials
  - Azure VM access details
  - Slack webhook URL

## Deployment Architecture

1. Application is containerized using Docker
2. Deployed to an Azure Virtual Machine
3. Runs as a container exposed on port 80 (mapped to internal port 5000)

## Notification System

- Success/failure notifications sent to Slack channel
- Custom success message includes deployment confirmation

## Requirements

- Python 3.11
- Docker
- Trivy (integrated via GitHub Action)
- Access to:
  - DockerHub account
  - Azure VM with Docker installed
  - Slack webhook URL

## Setup Instructions

1. Store these secrets in your GitHub repository settings:
   - `DOCKER_USERNAME`
   - `DOCKER_PASSWORD`
   - `VM_IP` (Azure VM IP address)
   - `VM_USER` (Azure VM username)
   - `VM_PASS` (Azure VM password)
   - `SLACK_WEBHOOK_URL`

2. Ensure your Azure VM has:
   - Docker installed and configured
   - SSH access enabled
   - Proper firewall rules for port 80

3. Push to `main` branch to trigger the pipeline

## Customization

To adapt this pipeline for your project:

1. Update `python-version` if needed
2. Modify Docker build commands if using different image names
3. Adjust deployment scripts for your target environment
4. Update Slack notification messages
