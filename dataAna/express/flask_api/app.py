# coding:utf-8

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world!'

# @app.route('/<name>')
# def hello():
#     return


if __name__ == '__main__':
    app.run(debug=True, port=8092)
