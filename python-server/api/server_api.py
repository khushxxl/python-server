from flask import Flask, request, jsonify

app = Flask(__name__)
allowed_mac_addrs = ["08:97:98:b2:7e:83"]

@app.route('/mac', methods=['POST'])
def receive_mac_address():
    data = request.json
    mac_address = data.get('mac_address')
    if mac_address in allowed_mac_addrs:
        return jsonify("TRUE"), 200
    return jsonify("FALSE"), 403
