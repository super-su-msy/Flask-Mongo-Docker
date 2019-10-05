from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from pymongo import MongoClient

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

@app.route("/insert", methods=[ 'GET' ])
def getMongo():
    post_1 = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
    }
    post_2 = {
    'title': 'Virtual Environments',
    'content': 'Use virtual environments, you guys',
    'author': 'Scott'
    }
    post_3 = {
    'title': 'Learning Python',
    'content': 'Learn Python, it is easy',
    'author': 'Bill'
    }
    new_result = posts.insert_many([post_1, post_2, post_3])
    print('Multiple posts: {0}'.format(new_result.inserted_ids))
    return jsonify("successfull"), 200

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
