from flask import Flask, render_template

application = Flask(__name__, static_folder='./dist/static',
                    template_folder='./dist')


@application.route('/', defaults={'path': ''})
@application.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
