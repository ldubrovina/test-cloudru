from flask import Flask, jsonify
import os
import uuid

app = Flask(__name__)


@app.route('/hostname', methods=['GET'])
def get_hostname():
    return jsonify({'hostname': os.uname().nodename})


@app.route('/author', methods=['GET'])
def get_author():
    return jsonify({'author': os.getenv('AUTHOR', 'Unknown')})


@app.route('/id', methods=['GET'])
def get_id():
    return jsonify({'id': os.getenv('UUID', str(uuid.uuid4()))})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
