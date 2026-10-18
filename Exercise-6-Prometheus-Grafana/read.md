# Exercise 6 – Prometheus and Grafana Monitoring

## Objective

To containerize a Flask-based Delivery Service and monitor its metrics using Prometheus and Grafana.

## Technologies Used

- Python
- Flask
- Docker
- Docker Compose
- Prometheus
- Grafana

## Project Structure

```text
Exercise-6-Prometheus-Grafana/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── prometheus.yml
├── requirements.txt
└── README.md
Delivery Service
The Flask application runs on port 8000 and provides:
- / – Displays the service status.
- /metrics – Exposes delivery metrics in Prometheus format.
Metrics
The application exposes the following metrics:
- pending_deliveries – Number of pending deliveries.
- on_the_way_deliveries – Number of deliveries currently on the way.
- total_deliveries – Total number of deliveries.
- average_delivery_time – Average delivery time in minutes.
- delivery_requests_total – Total number of delivery requests.
The values are generated dynamically for demonstration purposes.
Docker Setup
Docker Compose is used to run three services:
1. Prometheus
Prometheus runs on:
http://localhost:9090

It collects metrics from the Delivery Service every 5 seconds.
2. Delivery Service
The Flask application runs on:
http://localhost:8000

Its Prometheus metrics endpoint is:
http://localhost:8000/metrics

3. Grafana
Grafana runs on:
http://localhost:3000

It can be used to visualize the metrics collected by Prometheus.
Prometheus Configuration
Prometheus is configured with two scrape targets:
prometheus:9090
delivery-service:8000

The Delivery Service is accessed using the Docker Compose service name:
delivery-service:8000

Running the Project
Build and start all containers using:
docker compose up -d --build

Check the running containers:
docker compose ps

To stop the services:
docker compose down

Verifying Prometheus
Open:
http://localhost:9090

Use PromQL queries such as:
pending_deliveries

on_the_way_deliveries

total_deliveries

average_delivery_time

delivery_requests_total

Prometheus should return the corresponding metric values.
Verifying Targets
Open:
http://localhost:9090/targets

Both targets should show the status:
UP

Expected targets:
delivery-service:8000
prometheus:9090

Grafana
Open:
http://localhost:3000

Grafana can be connected to Prometheus and used to create dashboards for the delivery metrics.
Result
The Delivery Service was successfully containerized using Docker Compose, monitored using Prometheus, and made available for visualization through Grafana.
The Prometheus targets are successfully scraped and the delivery metrics can be queried using PromQL.

### One small thing before you submit

If your teacher expects **screenshots**, include these 3 in the README:

1. **Docker Compose running** — `docker compose ps`
2. **Prometheus Targets** — both targets showing **UP**
3. **Prometheus query** — `delivery_requests_total` showing `199` (your current successful screenshot)

That will make the README/report much stronger.