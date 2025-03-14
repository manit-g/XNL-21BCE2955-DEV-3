import pytest
from kubernetes import client, config
import requests
import time
from web3 import Web3

class TestFullSystem:
    @pytest.fixture(autouse=True)
    def setup(self):
        config.load_kube_config()
        self.k8s_client = client.CoreV1Api()
        self.w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
        
    def test_ml_deployment(self):
        # Test ML service deployment
        deployment = self.k8s_client.read_namespaced_deployment(
            name='ml-scaling',
            namespace='ml-system'
        )
        assert deployment.status.ready_replicas == deployment.spec.replicas
        
        # Test prediction endpoint
        response = requests.post(
            'http://ml-scaling-service/predict',
            json={'features': [0.1, 0.2, 0.3]}
        )
        assert response.status_code == 200
        
    def test_blockchain_integration(self):
        # Test smart contract deployment
        contract = self.w3.eth.contract(
            address='CONTRACT_ADDRESS',
            abi=CONTRACT_ABI
        )
        
        # Create deployment
        tx_hash = contract.functions.createDeployment(
            'v1.0.0',
            'abc123',
            'QmXYZ'
        ).transact()
        
        # Wait for transaction
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        assert tx_receipt.status == 1 