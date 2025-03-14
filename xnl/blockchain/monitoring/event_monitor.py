from web3 import Web3
from eth_abi import decode_abi
import json
import logging
from prometheus_client import Counter, start_http_server

class BlockchainMonitor:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
        self.deployment_counter = Counter('blockchain_deployments_total', 'Total deployments')
        
    def monitor_events(self):
        deployment_filter = self.contract.events.DeploymentCreated.create_filter(fromBlock='latest')
        while True:
            for event in deployment_filter.get_new_entries():
                self.handle_deployment_event(event)
                
    def handle_deployment_event(self, event):
        self.deployment_counter.inc()
        logging.info(f"New deployment: {event.args}") 