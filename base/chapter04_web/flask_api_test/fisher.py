# coding:utf-8
__author__ = 'young'


from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world!'


if __name__ == "__main__":
    app.run(debug=True)
