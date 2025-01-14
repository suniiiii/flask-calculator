from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Calculator!"

@app.route('/add', methods=['GET'])
def add():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    result = a + b
    return jsonify({"operation": "addition", "result": result})

@app.route('/subtract', methods=['GET'])
def subtract():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    result = a - b
    return jsonify({"operation": "subtraction", "result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
