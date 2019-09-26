from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/get")
def getReq():
    arr = [ 4, "silly", 6,"Json"]
    return jsonify(arr)

@app.route("/json")
def hello1():
    return jsonify({
    'KARAN':
    'KEEANU'})

if __name__ == "__main__":
    app.run()