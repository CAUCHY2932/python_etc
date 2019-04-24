# coding:utf-8
from app import create_app

__author__ = "young"


# from app.api.v1.blueprints import create_app


app = create_app()

#
# from flask import Flask
#
#
# app = Flask(__name__)


if __name__ == '__main__':

    app.run(debug=True)
