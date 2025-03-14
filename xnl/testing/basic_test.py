import unittest
import requests

class TestBasicFunctionality(unittest.TestCase):
    def test_ml_scaling(self):
        response = requests.post(
            "http://ml-scaling-service/predict",
            json={"features": [0.1, 0.2, 0.3]}
        )
        self.assertEqual(response.status_code, 200)

    def test_blockchain_logging(self):
        # Test deployment logging
        response = requests.post(
            "http://blockchain-service/log",
            json={"deployment": "test", "version": "1.0"}
        )
        self.assertEqual(response.status_code, 200) 