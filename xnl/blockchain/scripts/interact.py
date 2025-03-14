from web3 import Web3
import json
import os
from dotenv import load_dotenv

class BlockchainDeployer:
    def __init__(self):
        load_dotenv()
        
        # Connect to Ethereum network (using Infura)
        self.w3 = Web3(Web3.HTTPProvider(os.getenv('ETHEREUM_RPC_URL')))
        
        # Load contract ABI and address
        with open('blockchain/artifacts/DeploymentManager.json') as f:
            contract_json = json.load(f)
        self.contract_abi = contract_json['abi']
        self.contract_address = os.getenv('CONTRACT_ADDRESS')
        
        # Initialize contract
        self.contract = self.w3.eth.contract(
            address=self.contract_address,
            abi=self.contract_abi
        )
        
        # Set up account
        self.account = self.w3.eth.account.from_key(os.getenv('PRIVATE_KEY'))
        
    def create_deployment(self, version, commit_hash, ipfs_hash):
        # Build transaction
        nonce = self.w3.eth.get_transaction_count(self.account.address)
        
        tx = self.contract.functions.createDeployment(
            version,
            commit_hash,
            ipfs_hash
        ).build_transaction({
            'from': self.account.address,
            'nonce': nonce,
            'gas': 2000000,
            'gasPrice': self.w3.eth.gas_price
        })
        
        # Sign and send transaction
        signed_tx = self.w3.eth.account.sign_transaction(tx, self.account.key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        # Wait for transaction receipt
        receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt

if __name__ == "__main__":
    deployer = BlockchainDeployer()
    receipt = deployer.create_deployment(
        version="1.0.0",
        commit_hash="abc123",
        ipfs_hash="QmXyz..."
    )
    print(f"Deployment created in transaction: {receipt.transactionHash.hex()}") 