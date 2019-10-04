from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

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

class firstApi(Resource):
     def post(self):

        req = request.get_json()

        x = req["x"]
        y = req["y"]
        z = x+y
        response = {
            'result': z,
            'check' : " Test ",
            'succes': 'true'
        }
        return jsonify(response)   

api.add_resource(firstApi, "/add")   

if __name__ == "__main__":
    app.run(host='0.0.0.0')
