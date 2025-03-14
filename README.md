# XNL-21BCE2955-DEV-3


# AI-Powered Kubernetes Auto-Scaling & Blockchain-Based CI/CD System

## **Project Overview**
This project is designed to automate and manage an AI-powered Kubernetes cluster for auto-scaling, CI/CD integration with blockchain, and secure, fault-tolerant architecture for modern cloud-native applications. It leverages Kubernetes, Istio service mesh, Kubeflow for ML pipelines, blockchain smart contracts for deployment validation, and a secure, self-healing system design.

---

## **Features**
- **AI-powered Auto-scaling**: Uses Machine Learning (ML) models to predict workloads and scale Kubernetes clusters dynamically using Horizontal Pod Autoscaler (HPA).
- **Blockchain-Based CI/CD**: Smart contracts validate deployments, ensuring secure and traceable builds and deployments with IPFS storage for artifacts.
- **Zero-Trust Security**: End-to-end encryption and role-based access controls (RBAC) ensure secure communications between services.
- **Fault Tolerant & Self-Healing**: Automated failover mechanisms and monitoring to ensure high availability.
- **Kubeflow Integration**: Streamlines ML pipelines to automate model training, prediction, and deployment.
- **Prometheus & Grafana Monitoring**: Real-time metrics and dashboards for system health, resource utilization, and performance.
- **Automated Testing**: Integration of chaos engineering, E2E testing with Playwright, performance testing with tools like Locust, and security testing with OWASP ZAP.

---

## **Project Components**

### 1. **Kubernetes Cluster Setup**
   - **Managed Kubernetes**: Cluster running on AWS using EKS (Elastic Kubernetes Service).
   - **Auto-Scaling**: Horizontal Pod Autoscaler (HPA) integrated with ML predictions to scale applications based on demand.

### 2. **Machine Learning for Auto-scaling**
   - **ML Model**: Built a model to predict system load and scale the Kubernetes cluster accordingly using custom metrics adapters.

### 3. **Blockchain-Based CI/CD**
   - **Smart Contracts**: Deployed smart contracts using Ethereum for validation and security of deployment pipelines.
   - **IPFS**: Integrated IPFS for decentralized storage of build artifacts, enhancing security and traceability.

### 4. **Service Mesh (Istio)**
   - **Istio Integration**: Used Istio to manage service-to-service communication securely with mutual TLS (mTLS), traffic routing, load balancing, and service discovery.

### 5. **Security Features**
   - **Zero-Trust Security**: Integrated Vault for secrets management, enforcing network policies, and leveraging Istio's security features for access control.
   - **RBAC**: Role-based access control ensures that only authorized services can communicate with each other.

### 6. **Monitoring and Metrics**
   - **Prometheus**: Collects system metrics for Kubernetes workloads.
   - **Grafana Dashboards**: Custom dashboards for real-time visualization of resource utilization and system performance.

### 7. **Automated Testing & Validation**
   - **Chaos Engineering**: Integrated chaos testing with tools like Locust and k6 to simulate failures and measure system resilience.
   - **E2E Testing**: Built automated end-to-end testing with Playwright.
   - **Performance & Security Tests**: Using OWASP ZAP for security vulnerabilities and performance testing with load testing tools.

---

## **Installation**

### Prerequisites
- Docker
- Kubernetes (Minikube, EKS, or GKE)
- Helm
- AWS CLI / GCP CLI (depending on the cloud provider)
- Terraform (for infrastructure automation)
- kubectl
- Istio CLI
- Kubeflow for ML pipeline management
- Node.js (for front-end components)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/XNL-21BCEXXXX-DEV-3.git
   cd XNL-21BCEXXXX-DEV-3
   ```

2. **Set Up the Cloud Environment**
   - **AWS (or other cloud provider)**: Configure your credentials and set up IAM roles as required.
   - **Terraform**: Initialize and apply infrastructure for the cloud provider.
   ```bash
   terraform init
   terraform apply
   ```

3. **Set Up Kubernetes Cluster**
   - Deploy the cluster using AWS EKS or another cloud provider.
   - Install Istio and Kubeflow using Helm:
   ```bash
   kubectl create namespace istio-system
   helm install istio istio/istio --namespace istio-system
   ```

4. **Deploy the Application**
   - Deploy the necessary workloads, services, and Helm charts.
   ```bash
   kubectl apply -f kubernetes/manifest.yml
   ```

5. **Configure CI/CD Pipeline**
   - Set up GitHub Actions (or other CI/CD tool) for automated deployments.
   - Integrate blockchain-based deployment validation smart contracts.

6. **Configure ML Auto-scaling**
   - Deploy the ML model for load prediction and auto-scaling.
   - Set up custom metrics adapters for scaling.

7. **Set Up Monitoring and Logging**
   - Install Prometheus and Grafana.
   - Deploy custom metrics adapters and dashboards.

8. **Run Tests**
   - Execute integration, performance, and security tests.
   ```bash
   npm run test
   ```

---

## **Testing**

- **Unit Tests**: 80%+ test coverage
- **Integration Tests**: Includes testing of all services in the deployment pipeline.
- **E2E Tests**: Using Playwright to test the entire user flow.
- **Performance Tests**: Using k6 and Locust.
- **Security Tests**: Using OWASP ZAP for vulnerability scanning.

---

## **Deployment**

### Cloud Provider
- **AWS**: Using Elastic Kubernetes Service (EKS) for scalable infrastructure.
- **Domain**: [URL of Deployed Application] (e.g., `https://yourapp.cloud.com`)

### Live Monitoring
- Real-time dashboard via Grafana.
- Prometheus metrics collection.

---

## **Architecture Diagram**
A detailed architecture diagram is provided below to visualize the system components and interactions:
- Kubernetes Cluster
- ML Model for Auto-scaling
- Blockchain CI/CD Pipeline
- Service Mesh (Istio)
- Prometheus & Grafana for monitoring

---

## **Future Improvements**
- **Multi-Cloud Support**: Add support for GCP and Azure to extend multi-cloud deployments.
- **Backup and Disaster Recovery**: Automate the backup of critical data and provide disaster recovery mechanisms.
- **Advanced Security**: Implement further security measures with stronger encryption and compliance tools.

---

## **Contributing**

Feel free to fork this repository, submit issues, and contribute with pull requests. For any bugs, suggestions, or feedback, please open an issue.

---


### **Contact**
For any questions or inquiries, contact us at:  
Manit Gera, 21BCE2955, manitgera@gmail.com

