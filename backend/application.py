from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
from count_only import request_number
# from flask_cors import CORS
from raise_hand_count_only import raise_count
from img_base64 import files1, files2,files3, files4, files5, files6, files7, files8, files9



application = Flask(__name__, static_folder='./dist/static',
                    template_folder='./dist')

api = Api(application)

class Req(Resource):
    def get(self):
        num = request_number(files1)
        return { "num" :str(num)}

class Req_sub(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('key1', type=str)
        parser.add_argument('key2', type=float)

        query_data = parser.parse_args()
        print("input_data={}".format(query_data))
        return query_data

class RaiseReq(Resource):
    def get(self):
        raise_num = raise_count(files1)
        return {"raiseNum" : raise_num}

api.add_resource(Req, "/api/req")
api.add_resource(RaiseReq,"/api/raise")
api.add_resource(Req_sub,"/bar", endpoint = "bar")


@application.route('/', defaults={'path': ''})
@application.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == '__main__':
    application.run(debug=True)