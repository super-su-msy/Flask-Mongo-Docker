from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

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
   

api.add_resource(firstApi, "/Resource")