from flask import Flask, render_template
from flask_restful import Api, Resource
from count_only import request_number, files

app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
api = Api(app)

class Req(Resource):
    def get(self):
        num = request_number(files)
        return { "num" :str(num)}

api.add_resource(Req, "/api/req")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)