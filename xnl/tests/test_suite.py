import unittest
from unittest.mock import patch
import pytest
from ml.training.train_pipeline import MLTrainingPipeline
from blockchain.scripts.interact import BlockchainDeployer

class TestMLSystem(unittest.TestCase):
    def setUp(self):
        self.pipeline = MLTrainingPipeline()
        
    def test_data_preparation(self):
        df = self.pipeline.prepare_data()
        self.assertGreater(len(df), 0)
        self.assertIn('cpu_usage', df.columns)
        
    def test_model_training(self):
        self.pipeline.train()
        self.assertIsNotNone(self.pipeline.model)
        
@pytest.mark.integration
class TestBlockchainIntegration:
    def test_deployment_creation(self):
        deployer = BlockchainDeployer()
        receipt = deployer.create_deployment(
            version="test",
            commit_hash="test123",
            ipfs_hash="test"
        )
        assert receipt.status == 1

@pytest.mark.e2e
class TestE2E:
    def test_full_pipeline(self):
        # Test ML training
        pipeline = MLTrainingPipeline()
        pipeline.train()
        
        # Test deployment
        deployer = BlockchainDeployer()
        receipt = deployer.create_deployment(
            version="1.0.0",
            commit_hash="test",
            ipfs_hash="test"
        )
        assert receipt.status == 1 