from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import requests, json

app = Flask(__name__)
api = Api(app)
client = MongoClient('mongodb://database:27017')
db = client.mk
posts = db.posts

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/get", methods=[ 'GET' ])
def getReq():
    arr = [ 4, "silly", 6,"Json"]
    return jsonify(arr)

@app.route("/retrieve", methods=[ 'GET' ])
def getRetreive():
    arr = []
    json = posts.find({})[0]['title']
    for obj in posts.find():
        arr.append(str(obj))
    resJSON = {
        "1": json,
        "2": arr
    }
    return jsonify(resJSON)

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

@app.route('/jsonplaceholder', methods=["GET"])
def google():
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    myschema = db["jsonplaceholder"]
    myschema.insert_many(r.json())
    return jsonify(r.json())

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
    app.run(host='0.0.0.0', debug=True)
