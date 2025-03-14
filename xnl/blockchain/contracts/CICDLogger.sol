// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CICDLogger {
    struct DeploymentLog {
        address deployer;
        string commitHash;
        string environment;
        uint256 timestamp;
        bool success;
        string metadata;
    }
    
    DeploymentLog[] public deploymentLogs;
    mapping(address => bool) public authorizedDeployers;
    
    event DeploymentRecorded(
        address indexed deployer,
        string commitHash,
        string environment,
        uint256 timestamp,
        bool success
    );
    
    modifier onlyAuthorizedDeployer() {
        require(authorizedDeployers[msg.sender], "Unauthorized deployer");
        _;
    }
    
    function recordDeployment(
        string memory commitHash,
        string memory environment,
        bool success,
        string memory metadata
    ) external onlyAuthorizedDeployer {
        deploymentLogs.push(DeploymentLog({
            deployer: msg.sender,
            commitHash: commitHash,
            environment: environment,
            timestamp: block.timestamp,
            success: success,
            metadata: metadata
        }));
        
        emit DeploymentRecorded(
            msg.sender,
            commitHash,
            environment,
            block.timestamp,
            success
        );
    }
} 