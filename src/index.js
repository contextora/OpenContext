import { ethers } from 'ethers';

async function getBalance(address) {
  const provider = new ethers.JsonRpcProvider("https://mainnet.infura.io/v3/YOUR_INFURA_KEY");
  const balance = await provider.getBalance(address);
  console.log(`Balance: ${ethers.utils.formatEther(balance)} ETH`);
}

getBalance("0x742d35Cc6634C0532925a3b844Bc454e4438f44e");
