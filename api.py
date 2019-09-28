from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def checkdata(postedData, operation):
    if (operation == "div"):
        if "x" not in postedData or "y" not in postedData:
            return 305
        elif "x" == 0:
            return 306
        else:
            return 200

class firstApi(Resource):
     def post(self):

        req = request.get_json()

        x = req["x"]
        y = req["y"]

        response = {
            'result': x+y,
            'succes': 'true'
        }
        return jsonify(response)

class secondApi(Resource):
    def post(self):
        
        req = request.get_json()

        statusCode = checkdata(req, "div")
        if (statusCode == 305 or statusCode == 306):
            return "you ugly BS"
            
        x = req["x"]
        y = req["y"]

        response = {
            'result': x/y,
            'succes': 'true'
        }
        return jsonify(response)
            
api.add_resource(firstApi, "/Resource")
api.add_resource(secondApi, "/div")