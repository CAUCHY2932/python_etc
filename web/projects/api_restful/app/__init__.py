# coding:utf-8


from flask import Flask
from flask import Blueprint




def create_app():

	app = Flask(__name__)
	app.register_blueprint()


