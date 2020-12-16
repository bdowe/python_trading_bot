from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({'msg': 'Hello, World!'})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')