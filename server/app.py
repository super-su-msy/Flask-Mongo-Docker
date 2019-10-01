from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/get", methods=[ 'GET' ])
def getReq():
    arr = [ 4, "silly", 6,"Json"]
    return jsonify(arr)

@app.route("/json", methods=[ 'GET' ])
def hello1():
    return jsonify({
    'KARAN':
    'KEEANU'})

if __name__ == "__main__":
    app.run()
@app.route("/post", methods=[ 'POST' ])
def helloPosty():
    dataDict = request.get_json()
    x = dataDict["x"]
    y = dataDict["y"]
    z=x+y

    JSON = {
        'result':x+y,
        'compiledRes':z
    }
    return jsonify(JSON), 200        

    # return "Hello, World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
