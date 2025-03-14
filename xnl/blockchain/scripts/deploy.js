const { ethers } = require("hardhat");

async function main() {
    console.log("Deploying DeploymentManager contract...");
    
    // Deploy the contract
    const DeploymentManager = await ethers.getContractFactory("DeploymentManager");
    const deploymentManager = await DeploymentManager.deploy();
    await deploymentManager.deployed();
    
    console.log("DeploymentManager deployed to:", deploymentManager.address);
    
    // Verify the contract on Etherscan (if on testnet)
    if (network.name !== "hardhat") {
        console.log("Verifying contract...");
        await hre.run("verify:verify", {
            address: deploymentManager.address,
            constructorArguments: [],
        });
    }
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    }); 