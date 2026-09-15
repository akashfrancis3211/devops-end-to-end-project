# DevOps Task API

End-to-end DevOps / DevSecOps portfolio project for a containerized Flask REST API with automated CI/CD using Jenkins, Docker, Trivy, Docker Hub, Kubernetes, and Helm.

---

## 📌 Project Overview

**DevOps Task API** is a practical DevOps project built around a lightweight Flask REST API.

The project demonstrates a complete application delivery workflow:

**GitHub → Jenkins → Test → Docker Build → Trivy Scan → Docker Hub → Helm → Kubernetes**

The current implementation runs in a local lab environment using Jenkins on Windows and a Kind Kubernetes cluster.

This project focuses on demonstrating practical DevOps and DevSecOps concepts rather than presenting a production cloud deployment.

---

## 🏗️ Architecture

```text
                    Developer
                        │
                        ▼
                   ┌─────────┐
                   │ GitHub  │
                   └────┬────┘
                        │
                        ▼
                 ┌─────────────┐
                 │   Jenkins   │
                 │   CI / CD   │
                 └──────┬──────┘
                        │
          ┌─────────────┼─────────────┐
          │             │             │
          ▼             ▼             ▼
      Validate        Pytest      Docker Build
                                      │
                                      ▼
                                Trivy Security
                                    Scan
                                      │
                                      ▼
                                Docker Hub
                                      │
                                      ▼
                                Helm Deploy
                                      │
                                      ▼
                              ┌──────────────┐
                              │ Kubernetes   │
                              │    Kind      │
                              └──────┬───────┘
                                     │
                                     ▼
                              DevOps Task API
```

---

## 🎯 Project Objectives

* Build and containerize a Flask REST API
* Create automated CI/CD using Jenkins
* Run application validation and automated tests
* Build Docker images automatically
* Scan container images for security vulnerabilities using Trivy
* Push validated images to Docker Hub
* Deploy the application to Kubernetes using Helm
* Perform rollout verification after deployment
* Practice real-world DevOps troubleshooting
* Maintain a professional GitHub portfolio project

---

## 🛠️ Tech Stack

| Technology  | Purpose                       |
| ----------- | ----------------------------- |
| Python      | Application development       |
| Flask       | REST API framework            |
| Pytest      | Automated testing             |
| Docker      | Application containerization  |
| Jenkins     | CI/CD automation              |
| Trivy       | Container security scanning   |
| Docker Hub  | Container image registry      |
| Kubernetes  | Container orchestration       |
| Kind        | Local Kubernetes cluster      |
| Helm        | Kubernetes package management |
| Git         | Version control               |
| GitHub      | Source code hosting           |
| Linux / WSL | Development environment       |

---

## 🔄 CI/CD Pipeline

The Jenkins pipeline performs the following stages:

1. **Diagnose**

   * Verifies Python, Docker, Trivy, kubectl and Helm availability.
   * Confirms Kubernetes connectivity.

2. **Validate**

   * Checks the Python environment.
   * Performs Python syntax validation.

3. **Test**

   * Installs development dependencies.
   * Executes the automated Pytest suite.

4. **Docker Build**

   * Builds a versioned Docker image using the Jenkins build number.

5. **Docker Verify**

   * Verifies the generated Docker image.

6. **Trivy Security Scan**

   * Scans the Docker image for HIGH and CRITICAL vulnerabilities.
   * Generates a JSON security report.
   * Archives the report as a Jenkins build artifact.
   * Fails the pipeline when applicable HIGH/CRITICAL vulnerabilities are detected.

7. **Docker Push**

   * Authenticates securely with Docker Hub using Jenkins credentials.
   * Pushes the versioned image to the container registry.

8. **Kubernetes Connectivity**

   * Verifies kubectl access to the Kind cluster.
   * Verifies Helm connectivity.

9. **Helm Deploy**

   * Installs or upgrades the Helm release.
   * Deploys the new image version.
   * Waits for the Kubernetes Deployment rollout to complete.

10. **Deployment Verification**

    * Confirms that the Kubernetes rollout succeeds.
    * Displays the deployed application pods.

---

## 🔐 DevSecOps — Trivy

Security scanning is integrated directly into the CI/CD pipeline.

The pipeline performs two scans:

### Report generation

The first scan generates a JSON report and allows the pipeline to continue so that the result can be archived.

### Security gate

The second scan uses the exit code as a pipeline quality gate.

If applicable HIGH or CRITICAL vulnerabilities are detected, Jenkins fails the build.

This demonstrates the concept of **shift-left security**, where container security is checked before deployment.

---

## 🐳 Docker

The application is packaged as a Docker image using:

```text
python:3.12-slim-trixie
```

The Docker image includes:

* Flask application
* Python dependencies
* Non-root application user
* Port `5000`

The container runs the Flask application on:

```text
0.0.0.0:5000
```

The Dockerfile also updates the base operating-system packages to reduce known OS-level vulnerabilities.

---

## 🧪 Testing

The project uses **Pytest** for automated application testing.

Current test coverage includes:

* Health endpoint
* GET `/tasks`
* POST `/tasks`
* Missing title validation
* Empty title validation
* Invalid title type validation
* Whitespace normalization

Example test result:

```text
7 passed
```

---

## 🌐 Application API

### Health Check

```http
GET /health
```

Example response:

```json
{
  "status": "healthy"
}
```

### Get Tasks

```http
GET /tasks
```

Returns the current task list.

### Create Task

```http
POST /tasks
Content-Type: application/json
```

Example request:

```json
{
  "title": "Learn Jenkins"
}
```

Example response:

```json
{
  "id": 3,
  "title": "Learn Jenkins",
  "completed": false
}
```

---

## ☸️ Kubernetes

The application can be deployed to Kubernetes using standard Kubernetes manifests and Helm.

The Kubernetes deployment includes:

* Deployment
* Service
* Multiple application replicas
* Container image versioning
* Kubernetes rollout verification

The local environment uses **Kind** to provide a Kubernetes cluster without requiring a paid cloud Kubernetes service.

---

## ⎈ Helm

The project contains a Helm chart under:

```text
helm/devops-task-api/
```

The chart manages:

* Deployment
* Service
* Replica count
* Container image repository
* Container image tag
* Service configuration

Example deployment command:

```bash
helm upgrade --install test-release ./helm/devops-task-api \
  --set image.tag=<BUILD_NUMBER>
```

This allows the same chart to deploy different application image versions.

---

## 🔢 Build-to-Deployment Traceability

The Jenkins build number is used as the Docker image tag.

For example:

```text
Jenkins Build #40
        ↓
Docker Image
akashfrancis/devops-task-api:40
        ↓
Docker Hub
        ↓
Helm
image.tag=40
        ↓
Kubernetes
```

This provides a simple traceability path from a Jenkins build to the deployed container version.

---

## 📁 Project Structure

```text
devops-end-to-end-project/
│
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── docker/
│   └── Dockerfile
│
├── helm/
│   └── devops-task-api/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
│           ├── deployment.yaml
│           └── service.yaml
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── tests/
│   └── test_app.py
│
├── Jenkinsfile
├── requirements-dev.txt
└── .gitignore
```

---

## 💻 Local Development

Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install application dependencies:

```bash
pip install -r app/requirements.txt
```

Run the application:

```bash
python app/app.py
```

The API will be available on:

```text
http://localhost:5000
```

Run tests:

```bash
pytest -v
```

---

## 🔧 Jenkins Environment

The current project was implemented in a local Windows-based Jenkins environment.

The Jenkins pipeline integrates:

* Python
* Docker
* Trivy
* kubectl
* Helm
* Kind Kubernetes cluster
* Docker Hub credentials

The Jenkins pipeline uses the user's Kubernetes kubeconfig to connect to the local Kind cluster.

This setup is intended as a learning and portfolio environment.

A production implementation would normally use dedicated Jenkins agents and managed infrastructure rather than developer-machine paths.

---

## 🧠 DevOps Concepts Demonstrated

This project demonstrates practical understanding of:

* CI/CD
* Continuous Integration
* Continuous Delivery
* Containerization
* Docker image versioning
* Container security scanning
* Artifact archiving
* Credential management
* Docker registry integration
* Kubernetes Deployments
* Kubernetes Services
* Helm charts
* Helm upgrades
* Kubernetes rollout verification
* Build-to-deployment traceability
* Infrastructure troubleshooting

---

## 🛠️ Troubleshooting Experience

During development, the project was used to troubleshoot real pipeline and deployment issues including:

* Python application errors
* HTTP 404 and 500 errors
* Docker image vulnerability findings
* Docker build issues
* Jenkins environment and PATH issues
* Kubernetes kubeconfig access
* Helm deployment issues
* Kubernetes rollout timeouts
* Kubernetes pod state verification
* Helm template selector configuration

These troubleshooting scenarios helped validate the pipeline beyond simply creating configuration files.

---

## ⚠️ Current Limitations

This project is intentionally focused on demonstrating DevOps fundamentals.

Current limitations include:

* Application data is stored in memory.
* No persistent database is configured.
* Kubernetes is running locally through Kind.
* Jenkins is running on a local Windows environment.
* No production cloud infrastructure is currently provisioned.
* No centralized monitoring or logging stack is configured.

These limitations are documented intentionally rather than hidden.

---

## 🚀 Future Improvements

Potential future improvements include:

* GitHub webhook-triggered Jenkins builds
* Dedicated Jenkins controller and agent architecture
* Remote/containerized Jenkins agents
* Terraform-managed cloud infrastructure
* AWS deployment
* Managed Kubernetes
* External database
* Ingress configuration
* HTTPS/TLS
* Prometheus and Grafana monitoring
* Centralized logging
* Environment-specific Helm values
* Automated rollback strategies

---

## 📌 Project Outcome

This project demonstrates an end-to-end DevOps / DevSecOps workflow:

```text
Source Code
    ↓
GitHub
    ↓
Jenkins
    ↓
Validation
    ↓
Automated Tests
    ↓
Docker Build
    ↓
Trivy Security Scan
    ↓
Docker Hub
    ↓
Helm
    ↓
Kubernetes
    ↓
Deployment Verification
```

The project is designed to demonstrate practical hands-on knowledge of application delivery, containerization, CI/CD automation, security scanning, Kubernetes deployment, Helm-based release management, and DevOps troubleshooting.

---

## 👤 Author

**Akash Francis**

DevOps / DevSecOps Engineer — Portfolio Project

## 🔗 GitHub Repository

**devops-end-to-end-project**

Built as part of a hands-on DevOps learning and portfolio journey.

