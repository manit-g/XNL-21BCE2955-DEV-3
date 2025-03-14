import pytest
from kubernetes import client, config
import requests
from web3 import Web3
import time

class TestCompleteSystem:
    @pytest.fixture(autouse=True)
    def setup(self):
        config.load_kube_config()
        self.k8s_client = client.CoreV1Api()
        self.w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
        
    def test_ml_system(self):
        # Test ML deployment
        deployment = self.k8s_client.read_namespaced_deployment(
            name='ml-scaling',
            namespace='ml-system'
        )
        assert deployment.status.ready_replicas == deployment.spec.replicas
        
        # Test prediction
        response = requests.post(
            'http://ml-scaling-service/predict',
            json={'features': [0.1, 0.2, 0.3]}
        )
        assert response.status_code == 200
        
    def test_blockchain_system(self):
        # Test smart contract
        tx_hash = self.contract.functions.createDeployment(
            'test',
            'test123',
            'QmTest'
        ).transact()
        receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        assert receipt.status == 1 