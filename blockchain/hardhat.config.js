require("dotenv").config();
require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: {
    version: "0.8.20",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  },
  networks: {
    sepolia: {
      url: process.env.API_URL,
      accounts: [process.env.PRIVATE_KEY],
      gasPrice: 10000000000, // 10 gwei
    },
    hardhat: {
      chainId: 1337
    }
  },
  paths: {
    sources: "./",
    tests: "./test",
    cache: "./cache",
    artifacts: "./artifacts"
  }
};
