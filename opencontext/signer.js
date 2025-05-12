export async function signWithMetaMask(message) {
  if (!window.ethereum) throw new Error("MetaMask not found");
  const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
  const signer = accounts[0];
  return await window.ethereum.request({
    method: 'personal_sign',
    params: [message, signer],
  });
}
