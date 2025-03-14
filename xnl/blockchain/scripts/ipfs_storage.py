import ipfsapi
import os
from typing import Dict

class IPFSStorage:
    def __init__(self):
        self.ipfs = ipfsapi.connect('127.0.0.1', 5001)
        
    def store_artifact(self, file_path: str) -> Dict:
        """Store artifact in IPFS"""
        res = self.ipfs.add(file_path)
        return {
            'hash': res['Hash'],
            'name': os.path.basename(file_path),
            'size': res['Size']
        }
        
    def retrieve_artifact(self, ipfs_hash: str, output_path: str):
        """Retrieve artifact from IPFS"""
        self.ipfs.get(ipfs_hash, output_path) 