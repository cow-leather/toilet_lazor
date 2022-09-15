from flask import Flask, render_template
from flask_restful import Api, Resource
from count_only import request_number, files

application = Flask(__name__, static_folder='./dist/static',
                    template_folder='./dist')

api = Api(application)

class Req(Resource):
    def get(self):
        num = request_number(files)
        return { "num" :str(num)}

api.add_resource(Req, "/api/req")

@application.route('/', defaults={'path': ''})
@application.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == '__main__':
    application.run(debug=True)