from flask import Flask, jsonify
import os
import json

app = Flask(__name__)

def load_version_info():
    with open('app/version.json') as f:
        return json.load(f)

version_info = load_version_info()

@app.route('/version', methods=['GET'])
def version():
    return jsonify(version_info)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
