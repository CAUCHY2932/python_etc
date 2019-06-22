from flask import Blueprint, url_for

__author__ = '七月'

web = Blueprint('web', __name__, template_folder='templates')

from app.web import auth
from app.web import main
from app.web import book
from app.web import errors
from app.web import wish
from app.web import gift
from app.web import drift
from app.web import passenger
from app.web import test
