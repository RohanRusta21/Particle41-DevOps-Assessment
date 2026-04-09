from datetime import datetime
import os
from flask import Flask, request, jsonify

app = Flask(__name__)
app.json.sort_keys = False

@app.route('/')
def get_time_and_ip():
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if client_ip and ',' in client_ip:
        client_ip = client_ip.split(',')[0].strip()
    current_timestamp = datetime.now().isoformat()
    response = {
        "timestamp": current_timestamp,
        "ip": client_ip
    }
    return jsonify(response)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)