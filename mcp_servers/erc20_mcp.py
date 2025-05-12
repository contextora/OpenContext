from flask import Flask, request, jsonify
from web3 import Web3
import json

app = Flask(__name__)
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_KEY"
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

ERC20_ABI = json.loads('[{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"type":"function"}]')

@app.route('/balance', methods=['POST'])
def get_balance():
    data = request.get_json()
    token_address = data['token_address']
    wallet = data['wallet']
    contract = w3.eth.contract(address=token_address, abi=ERC20_ABI)
    balance = contract.functions.balanceOf(wallet).call()
    return jsonify({"wallet": wallet, "balance": str(balance)})

if __name__ == '__main__':
    app.run(debug=True)
