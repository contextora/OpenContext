from flask import Flask, request, jsonify
from web3 import Web3
from eth_account.messages import encode_defunct
import os

app = Flask(__name__)
INFURA_URL = os.getenv("INFURA_URL", "https://mainnet.infura.io/v3/YOUR_INFURA_KEY")
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

@app.route('/')
def index():
    return "MetaMask MCP is running"

@app.route('/verify-signature', methods=['POST'])
def verify_signature():
    data = request.get_json()
    message = data.get('message')
    signature = data.get('signature')
    address = data.get('address')

    encoded = encode_defunct(text=message)
    recovered = w3.eth.account.recover_message(encoded, signature=signature)
    return jsonify({"valid": recovered.lower() == address.lower(), "recovered": recovered})

if __name__ == '__main__':
    app.run(debug=True)
