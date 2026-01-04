# Automated Data Engineering Pipeline
This project demonstrates a production-ready CI/CD pipeline using **Jenkins** and **Docker** to automate data preprocessing for NLP tasks.

### 🚀 Features:
- **True CI/CD Automation:** Fully automated workflow using **GitHub Webhooks**. Any code change (git push) instantly triggers a new build.
- **Containerized Execution:** Uses **Docker-outside-of-Docker** logic. The pipeline pulls a `python:3.9-slim` image to run scripts, ensuring zero dependency conflicts on the host server.
- **Data Validation & QA:** Includes a Python-based validation layer that checks for data consistency (lowercase conversion and whitespace stripping) and fails the build if quality standards aren't met.
- **Environment Management:** Demonstrates safe handling of environment-specific variables within the Jenkins pipeline.
- **Infrastructure as Code (IaC):** The entire build, test, and cleanup logic is version-controlled via a **Declarative Jenkinsfile**.

### 🛠 Tools & Technology Stack:
- **Jenkins:** Orchestrates the entire pipeline.
- **Docker:** Provides isolated, lightweight environments for script execution.
- **Python (NLP focused):** Custom script for data cleaning and string transformation.
- **AWS EC2:** Cloud infrastructure hosting the Jenkins master and Docker engine.
- **GitHub:** Source Control Management (SCM) and automation trigger source.

### 📊 Pipeline Flow:
1. **Developer Push:** Code is pushed to the GitHub `main` branch.
2. **Webhook Trigger:** GitHub sends a POST request to the AWS Jenkins server.
3. **Agent Provisioning:** Jenkins spins up a temporary Python Docker container.
4. **Data Processing:** The script cleans raw data and runs validation tests.
5. **Post-Build Actions:** Jenkins cleans up the container and reports the final status (Success/Failure).
