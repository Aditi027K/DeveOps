\# Exercise 10 - Multi-Node Kubernetes Cluster with Multiple Applications and Replicasets



\## Objective

Deploy two Flask applications on a 3-node Minikube Kubernetes cluster with multiple replicas distributed across nodes.



\## Applications



\### Product Catalog (App A)

\- Flask application

\- 2 replicas

\- Endpoint: `/products`

\- Returns a list of products



\### Shopping Cart (App B)

\- Flask application

\- 3 replicas

\- `GET /cart` retrieves the cart

\- `POST /cart` adds an item to the cart



\## Technologies Used

\- Python

\- Flask

\- Docker

\- Kubernetes

\- Minikube

\- kubectl



\## Kubernetes Configuration

\- 3-node Minikube cluster

\- Docker driver

\- Product Catalog: 2 replicas

\- Shopping Cart: 3 replicas

\- Pod anti-affinity used for distributing replicas across nodes

\- NodePort services used to expose both applications



\## Docker Images



```text

product-catalog:latest

shopping-cart:latest

Verification

The Kubernetes cluster successfully ran:

\- 2 Product Catalog pods

\- 3 Shopping Cart pods

The pods were distributed across the Minikube nodes.



Both applications were exposed using NodePort services.

API Testing

Product Catalog

GET /products



Successfully returned:

\- Laptop

\- Phone

\- Headphones

Shopping Cart

GET /cart

POST /cart



The GET request initially returned an empty cart, and the POST request successfully added a Laptop with quantity 1.

Result

Successfully deployed and tested two Flask applications with multiple replicas on a 3-node Kubernetes cluster.



\### Then



\*\*Save → close Notepad.\*\*



After that, run:



```powershell

dir





