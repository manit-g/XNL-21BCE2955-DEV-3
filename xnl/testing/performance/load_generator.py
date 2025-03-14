from locust import HttpUser, task, between
import json

class LoadTest(HttpUser):
    wait_time = between(0.1, 0.5)
    
    @task
    def predict_workload(self):
        self.client.post("/predict", 
            json={"features": [0.1, 0.2, 0.3]}
        ) 