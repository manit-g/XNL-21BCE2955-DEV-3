// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DeploymentManager {
    struct Deployment {
        string version;
        string commitHash;
        address deployer;
        uint256 timestamp;
        bool validated;
        string ipfsHash;  // IPFS hash of deployment artifacts
    }
    
    mapping(bytes32 => Deployment) public deployments;
    mapping(address => bool) public authorizedDeployers;
    
    event DeploymentCreated(
        bytes32 indexed deploymentId,
        string version,
        string commitHash,
        address deployer,
        uint256 timestamp
    );
    
    event DeploymentValidated(
        bytes32 indexed deploymentId,
        address validator,
        uint256 timestamp
    );
    
    modifier onlyAuthorized() {
        require(authorizedDeployers[msg.sender], "Not authorized");
        _;
    }
    
    constructor() {
        authorizedDeployers[msg.sender] = true;
    }
    
    function createDeployment(
        string memory version,
        string memory commitHash,
        string memory ipfsHash
    ) external onlyAuthorized returns (bytes32) {
        bytes32 deploymentId = keccak256(
            abi.encodePacked(version, commitHash, block.timestamp)
        );
        
        deployments[deploymentId] = Deployment({
            version: version,
            commitHash: commitHash,
            deployer: msg.sender,
            timestamp: block.timestamp,
            validated: false,
            ipfsHash: ipfsHash
        });
        
        emit DeploymentCreated(
            deploymentId,
            version,
            commitHash,
            msg.sender,
            block.timestamp
        );
        
        return deploymentId;
    }
    
    function validateDeployment(bytes32 deploymentId) external onlyAuthorized {
        require(deployments[deploymentId].timestamp > 0, "Deployment not found");
        require(!deployments[deploymentId].validated, "Already validated");
        
        deployments[deploymentId].validated = true;
        
        emit DeploymentValidated(
            deploymentId,
            msg.sender,
            block.timestamp
        );
    }
} 