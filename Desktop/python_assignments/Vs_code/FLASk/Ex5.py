from flask import Flask, jsonify, request, render_template # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/addition')
def addition():
    a = request.args.get('num1', type=int)
    b = request.args.get('num2', type=int)
    
    if a is None or b is None:
        return jsonify({"error": "Please provide valid numbers"}), 400

    return jsonify({"result": f"The addition of {a} and {b} is {a + b}"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
