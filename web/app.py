from flask import Flask, jsonify
from attack import attack

app = Flask(__name__)

@app.route('/attack/<apiKey>', methods=['GET'])
def hello_world(apiKey):
    return jsonify(attack(apiKey))


if __name__ == '__main__':
    app.run()
