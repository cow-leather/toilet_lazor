from flask import Flask, render_template
from flask_restful import Api, Resource
from count_only import request_number, files
# from flask_cors import CORS
from raise_hand_count_only import raise_count, files1

application = Flask(__name__, static_folder='./dist/static',
                    template_folder='./dist')

api = Api(application)

class Req(Resource):
    def get(self):
        num = request_number(files)
        return { "num" :str(num)}

class RaiseReq(Resource):
    def get(self):
        raise_num = raise_count(files1)
        return {"raiseNum" : raise_num}

api.add_resource(Req, "/api/req")
api.add_resource(RaiseReq,"/api/raise")


@application.route('/', defaults={'path': ''})
@application.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == '__main__':
    application.run(debug=True)