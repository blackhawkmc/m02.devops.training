from flask import Flask, jsonify, request

app = Flask(__name__)

calculation_history = []


@app.route("/")
def home():
    return "Welcome to the Flask App!"


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    sum = a + b
    calculation_history.append({"operation": "add", "a": a, "b": b, "result": sum})
    return jsonify({"result": sum})


@app.route("/subtract", methods=["POST"])
def subtract():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    diff = a - b
    calculation_history.append({"operation": "subtract", "a": a, "b": b, "result": diff})
    return jsonify({"result": diff})


@app.route("/multiply", methods=["POST"])
def multiply():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    product = a * b
    calculation_history.append({"operation": "multiply", "a": a, "b": b, "result": product})
    return jsonify({"result": product})


@app.route("/divide", methods=["POST"])
def divide():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    if b == 0:
        return jsonify({"error": "Division by zero is not allowed"}), 400
    quotient = a / b
    calculation_history.append({"operation": "divide", "a": a, "b": b, "result": quotient})
    return jsonify({"result": quotient})

@app.route("/history", methods=["GET"])
def history():
    return jsonify({"history": calculation_history})



if __name__ == "__main__":
    app.run(debug=True)
