from flask import Blueprint, request, jsonify
import json

api = Blueprint("api", __name__)


@api.route('/', methods=['POST'])
def index():
    data = json.loads(request.data)
    time = data.get('time')
    print('hello')
    return jsonify(dict(
        time=time
    ))
