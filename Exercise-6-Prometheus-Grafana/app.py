from flask import Flask, Response
import random

app = Flask(__name__)


@app.route("/metrics")
def metrics():
    pending = random.randint(10, 20)
    on_the_way = random.randint(5, 20)
    total = random.randint(50, 100)
    average_time = round(random.uniform(28, 31), 2)
    requests = random.randint(100, 200)

    data = f"""
# HELP pending_deliveries Number of pending deliveries
# TYPE pending_deliveries gauge
pending_deliveries {pending}

# HELP on_the_way_deliveries Number of deliveries currently on the way
# TYPE on_the_way_deliveries gauge
on_the_way_deliveries {on_the_way}

# HELP total_deliveries Total number of deliveries
# TYPE total_deliveries gauge
total_deliveries {total}

# HELP average_delivery_time Average delivery time in minutes
# TYPE average_delivery_time gauge
average_delivery_time {average_time}

# HELP delivery_requests_total Total number of delivery requests
# TYPE delivery_requests_total counter
delivery_requests_total {requests}
"""

    return Response(data, mimetype="text/plain")


@app.route("/")
def home():
    return "Delivery Service is running!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)