# Exercise 1 – Kubernetes Hello Pod

## Objective

Deploy an Nginx container as a Kubernetes Pod and expose it using a NodePort Service.

## Tools Used

- Docker Desktop
- Kubernetes
- kubectl
- Nginx

## Steps Performed

### 1. Create Kubernetes Pod

```bash
kubectl run hello-k8s --image=nginx --port=80
2. Verify Pod
kubectl get pods

The Pod was successfully running:
hello-k8s   1/1   Running

3. Expose Pod Using NodePort
kubectl expose pod hello-k8s --type=NodePort --port=80

4. Verify Service
kubectl get services

The service was created successfully as a NodePort service.
5. Access Application
The Nginx application was accessed through the assigned NodePort.
The browser displayed the:
Welcome to nginx!
Result
Successfully deployed an Nginx application on Kubernetes using Docker Desktop Kubernetes.
Kubernetes Flow
kubectl
   ↓
Kubernetes API Server
   ↓
hello-k8s Pod
   ↓
Nginx Container
   ↓
NodePort Service
   ↓
Browser
   ↓
Nginx Welcome Page