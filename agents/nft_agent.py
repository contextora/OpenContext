from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/nft-info', methods=['POST'])
def nft_info():
    data = request.get_json()
    user = data.get('wallet')
    return jsonify({"wallet": user, "nfts": ["CryptoPunk #123", "BoredApe #45"]})

if __name__ == '__main__':
    app.run(debug=True)
