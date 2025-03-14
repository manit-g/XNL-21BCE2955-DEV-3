import unittest
import requests
import numpy as np
from kubernetes import client, config

class TestMLSystem(unittest.TestCase):
    def setUp(self):
        config.load_kube_config()
        self.k8s_client = client.CoreV1Api()
        self.ml_service_url = "http://ml-scaling-service"
    
    def test_ml_service_health(self):
        response = requests.get(f"{self.ml_service_url}/health")
        self.assertEqual(response.status_code, 200)
    
    def test_pod_scaling(self):
        pods = self.k8s_client.list_namespaced_pod(namespace="ml-system")
        self.assertGreaterEqual(len(pods.items), 2)
    
    def test_prediction_endpoint(self):
        test_data = np.random.rand(1, 10).tolist()
        response = requests.post(
            f"{self.ml_service_url}/predict",
            json={"features": test_data}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("prediction", response.json()) 