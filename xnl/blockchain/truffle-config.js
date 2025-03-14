module.exports = {
  networks: {
    testnet: {
      host: "127.0.0.1",
      port: 8545,
      network_id: "*",
      gas: 5500000
    }
  },
  compilers: {
    solc: {
      version: "0.8.0"
    }
  }
}; 