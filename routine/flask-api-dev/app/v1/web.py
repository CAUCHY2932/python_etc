# coding:utf-8

from flask import Blueprint


web = Blueprint("web", __name__)


@web.route('/')
def happy():
	return 'welcome to web!'
