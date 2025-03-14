from locust import HttpUser, task, between, events
import json
import logging

class MLSystemUser(HttpUser):
    wait_time = between(0.01, 0.05)  # High load testing
    
    def on_start(self):
        self.headers = {"Content-Type": "application/json"}
        
    @task(3)
    def predict_workload(self):
        payload = {
            "features": [0.1, 0.2, 0.3, 0.4, 0.5]
        }
        with self.client.post("/predict", 
            json=payload, 
            headers=self.headers,
            catch_response=True) as response:
            if response.status_code != 200:
                logging.error(f"Failed request: {response.text}")
                response.failure(f"Got {response.status_code}")

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    logging.info("Starting load test with 1M RPS target") 